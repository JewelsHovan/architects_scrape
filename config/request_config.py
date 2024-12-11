from typing import Dict

def create_request_payload(country: str, page: int) -> Dict:
    """Creates the request payload for the API."""
    return {
        "filters": [
            {"IndexFilterId": "Architect", "Column": "RegistrationNumber", "Display": "Registration number", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "ArchitectForename", "Display": "Forename", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "ArchitectSurname", "Display": "Surname", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "CompanyName", "Display": "Company name", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "Address", "Display": "Address (contains)", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": True, "WildcardEnd": True, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "Country", "Display": "Country", "AdditionalText": None, "AllowMultiple": None, "Type": "select", "WildcardStart": True, "WildcardEnd": True, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": country},
            {"IndexFilterId": "Architect", "Column": "Website", "Display": "Website", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "Email", "Display": "Email", "AdditionalText": None, "AllowMultiple": None, "Type": "text", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
            {"IndexFilterId": "Architect", "Column": "Geography", "Display": "Distance from UK postcode", "AdditionalText": None, "AllowMultiple": None, "Type": "radius", "WildcardStart": False, "WildcardEnd": False, "SoundsLike": False, "SoundsLikeEnabled": False, "SoundsLikeDefault": False, "SelectItems": None, "Value": None},
        ],
        "sorting": "",
        "bounds": None,
        "indexFilterId": "Architect",
        "page": page
    }

def get_request_headers() -> Dict:
    """Returns the headers for the API request."""
    return {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'cookiesession1=678A3E181E47A176CDDC81B55A4DC52E',
        'DNT': '1',
        'Origin': 'https://www.architects-register.org.uk',
        'Referer': 'https://www.architects-register.org.uk/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
    }