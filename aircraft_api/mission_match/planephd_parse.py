from io import StringIO
from lxml import etree
from pprint import pprint
import re
import requests


class PlanePHDParser:
  host = 'https://planephd.com'

  def crawl_aircraft(self):
    models = []
    model_data = []

    manufacturers = self.identify_manufacturers()

    for manufacturer in manufacturers:
      print(f'Identifying {manufacturer.get("name")} models.')
      models = [*models, *self.identify_models(manufacturer)]

    for i in range(10):
      model_data.append(self.get_aircraft_performance(models[i]))

    pprint(model_data)

  def identify_manufacturers(self):
    parser = etree.HTMLParser()
    url_path = '/wizard/manufacturers/'
    url = ''.join([self.host, url_path])
    response = requests.get(url)
    tree = etree.parse(StringIO(str(response.content)), parser)
    
    # TODO: Get plane manufacturer URL
    manufacturer_xpath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/a'
    manufacturer_data = [{'name': e.text, 'url': e.attrib['href']} for e in tree.xpath(manufacturer_xpath)]
    return manufacturer_data

  def identify_models(self, manufacturer):
    parser = etree.HTMLParser()
    # Get manufacturer models pages
    response = requests.get(''.join([self.host, manufacturer.get('url')]))
    tree = etree.parse(StringIO(str(response.content)), parser)

    # Get plane model URLs
    # model_xpath = '/html/body/div[2]/div/div/div/div/div[2]/div/ul/li/span/button'
    model_xpath = '/html/body/div[1]/div/div/div/div/div[2]/div[2]/ul/li/div/div/ul/li/a'
    models = [
      {
        'manufacturer': manufacturer.get('name'),
        'name': e.text.replace('\\n', '').strip(),
        'url': e.attrib['href']
      }
      for e in tree.xpath(model_xpath)
    ]
      
    return models

  def get_basic_aircraft_data(self, url, tree):
    plane_data = dict(url=url)

    # Get make
    make_xpath = '/html/body/div[1]/div[1]/div[1]/div/ol/li[4]/a/text()'
    make = tree.xpath(make_xpath)[0]
    plane_data['make'] = make

    # Get model
    model_xpath = '/html/body/div[1]/div[1]/div[1]/div/ol/li[5]/text()'
    model = tree.xpath(model_xpath)[0]
    plane_data['model'] = model

    return plane_data
  
  def get_aircraft_performance(self, aircraft):
    url = aircraft.get('url')
    if url is None:
      url = f'{self.host}/wizard/details/445/MOONEY-M20E-Super-21-Chaparral-specifications-performance-operating-cost-valuation'
    elif self.host not in url:
      url = ''.join([self.host, url])
    response = requests.get(url)
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(str(response.content)), parser)

    plane_data = self.get_basic_aircraft_data(url, tree)
    
    for page_section in xpath_tree:
      # pt_keys = [k for k in tree.xpath(xpath_tree[page_section]['keys']['path']) if k in xpath_tree[page_section]['keys']['map']]
      pt_keys = tree.xpath(xpath_tree[page_section]['keys']['path'])
      pt_values = tree.xpath(xpath_tree[page_section]['values']['path'])

      # if len(pt_keys) != len(pt_values):
      #   raise ValueError('Key/Value count does not match on performance top scrape')
      
      for i, key in enumerate(pt_keys):
        if key not in xpath_tree[page_section]['keys']['map']:
          continue
        clean_key = xpath_tree[page_section]['keys']['map'][key]
        match = re.search(xpath_tree[page_section]['values']['map'][clean_key]['pattern'], pt_values[i])
        clean_value = xpath_tree[page_section]['values']['map'][clean_key]['type'](match.group(1).replace(',', ''))
        plane_data[clean_key] = clean_value

    return plane_data


xpath_tree = {
  'performance_top': {
    'keys': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dt/p/text()',
      'map': {
        'Thrust:': 'thrust',
        'Best Cruise Speed:': 'cruise',
        'Best Range (i):': 'range',
        'Ceiling:': 'ceiling',
        'Ceiling (1 engine out):': 'ceiling_eo',
        'Fuel Burn:': 'fuel_burn',
        'Fuel Burn @ 75%:': 'fuel_burn_cruise',
        'Horsepower:': 'engine_hp',
        'Landing distance over 50ft obstacle:': 'landing_distance_50',
        'Landing distance:': 'landing_distance',
        'Rate of climb:': 'rate_of_climb',
        'Rate of climb (1 engine out):': 'rate_of_climb_eo',
        'Stall Speed:': 'stall_speed',
        'Takeoff distance over 50ft obstacle:': 'takeoff_distance_50',
        'Takeoff distance:': 'takeoff_distance'
      }
    },
    'values': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd/p/text()',
      'map': {
        'thrust': {
          'pattern': r'\d+ x ([\d,]+) N',
          'type': int
        },
        'cruise': {
          'pattern': r'([\d,]+) KIAS',
          'type': int
        },
        'range': {
          'pattern': r'([\d,]+) NM',
          'type': int
        },
        'ceiling': {
          'pattern': r'([\d,]+) FT',
          'type': int
        },
        'ceiling_eo': {
          'pattern': r'([\d,]+) FT',
          'type': int
        },
        'fuel_burn': {
          'pattern': r'([\d\.]+) GPH',
          'type': float
        },
        'fuel_burn_cruise': {
          'pattern': r'([\d\.]+) GPH',
          'type': float
        },
        'engine_hp': {
          'pattern': r'\d x ([\d,]+) HP',
          'type': int
        },
        'landing_distance_50': {
          'pattern': r'([\d,]+) FT',
          'type': int
        },
        'landing_distance': {
          'pattern': r'([\d,]+) FT',
          'type': int
        },
        'rate_of_climb': {
          'pattern': r'([\d,]+) FPM',
          'type': int
        },
        'rate_of_climb_eo': {
          'pattern': r'([\d,]+) FPM',
          'type': int
        },
        'stall_speed': {
          'pattern': r'([\d,]+) KIAS',
          'type': int
        },
        'takeoff_distance_50': {
          'pattern': r'([\d,]+) FT',
          'type': int
        },
        'takeoff_distance': {
          'pattern': r'([\d,]+) FT',
          'type': int
        }
      }
    }
  },
  'performance_specifications': {
    'keys': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dt/p/text()',
      'map': {
        'Gross Weight:': 'gross_weight',
        'Empty Weight:': 'empty_weight',
        'Maximum Payload:': 'max_payload',
        'Fuel capacity:': 'fuel_capacity'
      }
    },
    'values': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd/p/text()',
      'map': {
        'gross_weight': {
          'pattern': r'([\d,]+) LBS',
          'type': int
        },
        'empty_weight': {
          'pattern': r'([\d,]+) LBS',
          'type': int
        },
        'max_payload': {
          'pattern': r'([\d,]+) LBS',
          'type': int
        },
        'fuel_capacity': {
          'pattern': r'([\d,]+) [GAL|LBS]',
          'type': int
        }
      }
    }
  },
  'ownership_costs_header': {
    'keys': {
      'path': '//*[@id="ownership_costs_top"]/div/dl/dt/h4/text()',
      'map': {
        'Total Cost of Ownership:': 'total_cost_of_ownership',
        'Total Fixed Cost': 'total_fixed_cost',
        '\\n                                                    Total Variable Cost (': 'total_variable_cost'
      }
    },
    'values': {
      'path': '//*[@id="ownership_costs_top"]/div/dl/dd/h4/span/text()',
      'map': {
        'total_cost_of_ownership': {
          'pattern': r'^[\\n\s]+\$([\d,\.]+)[\\n\s]+$',
          'type': float
        },
        'total_fixed_cost': {
          'pattern': r'^[\\n\s]+\$([\d,\.]+)[\\n\s]+$',
          'type': float
        },
        'total_variable_cost': {
          'pattern': r'^[\\n\s]+\$([\d,\.]+)[\\n\s]+$',
          'type': float
        }
      }
    }
  },
  # 'ownership_costs_detail': {
  #   'keys': {
  #     'path': '//*[@id="ownership_costs_top"]/div/dl/dt/p/text()',
  #     'map': {
  #       'Annual inspection cost:': 'annual_inspection_cost',
  #     }
  #   },
  #   'values': {
  #     'path': '//*[@id="ownership_costs_top"]/div/dl/dd/p/text()',
  #     'map': {
  #       'annual_inspection_cost': {
  #         'pattern': r'^[\\n\s]+\$([\d,\.]+)[\\n\s]+$',
  #         'type': float
  #       }
  #     }
  #   }
  # },
  'engines': {
    'keys': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dt/p/text()',
      'map': {
        'Manufacturer:': 'engine_manufacturer',
        'Model:': 'engine_model',
        'Horsepower:': 'engine_hp',
        'Overhaul (HT):': 'engine_tbo',
        'Years before overhaul:': 'engine_tbo_years'
      }
    },
    'values': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd/p/text()',
      'map': {
        'engine_manufacturer': {
          'pattern': r'^([\w\W]+)$',
          'type': str
        },
        'engine_model': {
          'pattern': r'^([\w\W]+)$',
          'type': str
        },
        'engine_hp': {
          'pattern': r'([\d,]+) HP',
          'type': int
        },
        'engine_tbo': {
          'pattern': r'([\d,]+) Hrs',
          'type': int
        },
        'engine_tbo_years': {
          'pattern': r'([\d,]+)',
          'type': int
        }
      }
    }
  }
}