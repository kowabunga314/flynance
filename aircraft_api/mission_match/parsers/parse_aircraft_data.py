from bs4 import BeautifulSoup 
import re
import requests


def get_aircraft_data(url: str) -> dict:
    """
    get_aircraft_data Parses data from the PlanePHD page for a given aircraft model.

    Uses BeautifulSoup to pull data out of a webpage.

    Args:
        url (str, optional): URL of page to crawl.

    Returns:
        dict: Data fields and accumulated warnings
    """
    # Validate URL has data
    if url is None:
        raise ValueError('The argument "url" cannot be None.')
    # Get page content and parse with bs4
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table_data = soup.findAll('dl')

    data = {}
    errors = {}
    # Iterate over key/value pairs in table data
    for table in table_data:
        keys = table.findAll('dt')
        values = table.findAll('dd')
        for i in range(len(keys)):
            try:
                # Parse key
                if keys[i].find('h4'):
                    key = keys[i].h4.get_text(strip=True).strip(':')
                else:
                    key = keys[i].p.get_text(strip=True).strip(':')
                print(f'Key value: {key}')
                # Parse value
                if values[i].find('p'):
                    value = values[i].p.get_text(strip=True)
                else:   # Try looking in H4 elements
                    ele = values[i].find('h4')
                    if ele and ele.find('span'):
                        value = ele.span.get_text(strip=True)
                    elif ele and ele.find('small'):
                        value = ele.small.get_text(strip=True)
            except AttributeError as e:
                if key is not None:
                    errors[key] = {
                        'message': str(e),
                        'value': str(values[i])
                    }
                else:
                    errors[i] = {
                        'message': str(e),
                        'value': str(values[i])
                    }
            # Save key/value pair in data accumulator
            data[key] = value

    return {
        'data': data,
        'errors': errors
    }