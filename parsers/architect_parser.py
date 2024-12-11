import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from config.request_config import create_request_payload, get_request_headers
from config.search_config import DELAY


class ArchitectParser:
    BASE_URL = "https://www.architects-register.org.uk"
    
    def __init__(self, country: str, concurrent_requests: int = 5):
        self.country = country
        self.semaphore = asyncio.Semaphore(concurrent_requests)
        self.headers = get_request_headers()
        
    async def fetch_page_data(self, session: aiohttp.ClientSession, page: int) -> Optional[List[Dict]]:
        """Fetches and parses a single page of architect data."""
        async with self.semaphore:
            url = f"{self.BASE_URL}/registrant/list"
            payload = create_request_payload(self.country, page)
            
            try:
                async with session.post(url, headers=self.headers, json=payload) as response:
                    if response.status != 200:
                        print(f"Error fetching page {page}: {response.status}")
                        return None
                    
                    content = await response.text()
                    return self._parse_page_content(content, page)
            except Exception as e:
                print(f"Error processing page {page}: {e}")
                return None
            finally:
                # Add a delay between requests
                await asyncio.sleep(DELAY)
    
    def _parse_page_content(self, content: str, page: int) -> List[Dict]:
        """Parses the HTML content of a page."""
        soup = BeautifulSoup(content, 'html.parser')
        architects = []
        
        for li in soup.find_all('li', class_='media mb-3 border-bottom pb-3'):
            architect_data = self._parse_architect_entry(li)
            if architect_data:
                architects.append(architect_data)
        
        return architects
    
    def _parse_architect_entry(self, li: BeautifulSoup) -> Optional[Dict]:
        """Parses a single architect entry from the HTML."""
        try:
            media_body = li.find('div', class_='media-body')
            if not media_body:
                return None
            
            strong = media_body.find('strong', class_='mt-0 mb-1 title-font')
            if not strong or ' (' not in strong.text:
                return None
            
            view_link = li.find('a', class_='btn btn-primary')
            profile_url = f"{self.BASE_URL}{view_link['href']}" if view_link else None
            
            name = strong.text.split(' (')[0]
            registration_number = strong.text.split(' (')[1].strip(')')
            
            text_content = media_body.get_text(separator='|').split('|')
            filtered_content = [t.strip() for t in text_content if t.strip()]
            
            company = filtered_content[1] if len(filtered_content) > 1 else "N/A"
            address = filtered_content[2] if len(filtered_content) > 2 else "N/A"
            
            return {
                'name': name,
                'registration_number': registration_number,
                'company': company,
                'address': address,
                'country': self.country,
                'profile_url': profile_url
            }
        except Exception as e:
            print(f"Error processing architect entry: {e}")
            return None
    
    async def get_total_pages(self, session: aiohttp.ClientSession) -> int:
        """Gets the total number of pages available."""
        url = f"{self.BASE_URL}/registrant/list"
        payload = create_request_payload(self.country, 0)
        
        async with session.post(url, headers=self.headers, json=payload) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            try:
                page_text = soup.find('p', class_='d-block text-right mt-4').text.strip()
                return int(page_text.split('of')[-1].strip())
            except Exception as e:
                print(f"Error getting total pages: {e}")
                return 0
    
    async def scrape_all(self) -> List[Dict]:
        """Scrapes all architects data asynchronously."""
        async with aiohttp.ClientSession() as session:
            total_pages = await self.get_total_pages(session)
            print(f"Found {total_pages} pages to scrape for {self.country}")
            
            tasks = [self.fetch_page_data(session, page) for page in range(total_pages)]
            results = await asyncio.gather(*tasks)
            
            # Flatten results and remove None values
            all_architects = [
                architect 
                for page_results in results 
                if page_results is not None
                for architect in page_results
            ]
            
            return all_architects 