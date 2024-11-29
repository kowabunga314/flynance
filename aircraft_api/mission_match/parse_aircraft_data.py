from bs4 import BeautifulSoup 
import re
import requests


def get_aircraft_data(url: str=None) -> dict:
    if url is None:
        url = 'https://planephd.com/wizard/details/445/MOONEY-M20E-Super-21-Chaparral-specifications-performance-operating-cost-valuation'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    foo = soup.findAll('dl')

    data = {}
    errors = {}
    for table in foo:
        keys = table.findAll('dt')
        values = table.findAll('dd')
        for i in range(len(keys)):
            try:
                key = keys[i].p.get_text(strip=True).strip(':')
                # Get value from plain paragraph element
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
            data[key] = value

    return {
        'data': data,
        'errors': errors
    }