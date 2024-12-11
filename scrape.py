import asyncio
from datetime import datetime
import os
import json
from typing import List, Dict
from tqdm.asyncio import tqdm
import aiohttp

from parsers.architect_parser import ArchitectParser
from config.search_config import COUNTRY

def save_to_json(data: List[Dict], country: str) -> str:
    """
    Saves the scraped data to a JSON file in the 'output' directory.

    The filename is generated using the country name and the current timestamp.

    Args:
        data: The list of dictionaries containing the scraped data.
        country: The country for which the data was scraped.

    Returns:
        The path to the generated JSON file.
    """
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{output_dir}/architects_{country.lower().replace(' ', '_')}_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return filename

async def main():
    """
    Main function to run the architect scraper.

    Initializes the ArchitectParser with the specified country,
    scrapes the data, and saves the results to a JSON file.
    """
    try:
        parser = ArchitectParser(country=COUNTRY)
        
        # Create a single session for all requests
        async with aiohttp.ClientSession() as session:
            # Get total pages
            total_pages = await parser.get_total_pages(session)
            print(f"\nFound {total_pages} pages to scrape for {COUNTRY}")
            
            # Show progress during scraping using the same session
            print("\nScraping architects data...")
            architects = await tqdm.gather(
                *[parser.fetch_page_data(session, page) for page in range(total_pages)],
                desc="Scraping pages"
            )
            
            # Flatten the list of lists into a single list
            flattened_architects = [
                architect 
                for sublist in architects 
                for architect in (sublist or [])
            ]

            if flattened_architects:
                output_file = save_to_json(flattened_architects, COUNTRY)
                print(f"\nSuccessfully scraped {len(flattened_architects)} architects total.")
                print(f"Data saved to: {output_file}")
            else:
                print("\nNo architects found.")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())