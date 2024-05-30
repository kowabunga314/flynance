from io import StringIO
from lxml import etree
from pprint import pprint
import re
import requests


class PlanePHDParser:
  
  def get_aircraft_performance(self, url=None):
    plane_data = {}
    if url is None:
      # url = 'https://planephd.com/wizard/details/447/MOONEY-M20F-Executive-21-specifications-performance-operating-cost-valuation'
      url = 'https://planephd.com/wizard/details/445/MOONEY-M20E-Super-21-Chaparral-specifications-performance-operating-cost-valuation'
    response = requests.get(url)
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(str(response.content)), parser)

    # Get performance top
    pt_keys = tree.xpath(xpath_tree['performance_top']['keys']['path'])
    pt_values = tree.xpath(xpath_tree['performance_top']['values']['path'])

    if len(pt_keys) != len(pt_values):
      raise ValueError('Key/Value count does not match on performance top scrape')
    
    for page_section in xpath_tree:
      for i, key in enumerate(pt_keys):
        if key not in xpath_tree[page_section]['keys']['map']:
          continue
        clean_key = xpath_tree[page_section]['keys']['map'][key]
        match = re.search(xpath_tree[page_section]['values']['map'][clean_key]['pattern'], pt_values[i])
        clean_value = xpath_tree[page_section]['values']['map'][clean_key]['type'](match.group(1).replace(',', ''))
        # clean_value = clean_value.replace(',', '')
        plane_data[clean_key] = clean_value

    pprint(plane_data)


class PlanePHDXPathStore:
  horsepower = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[1]/p/text()'
  cruise_speed = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[2]/p'
  best_range= '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[3]/p'
  fuel_burn = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[4]/p'
  stall_speed = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[5]/p'
  rate_of_climb = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[6]/p'
  ceiling = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[7]/p'
  takeoff_distance = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[8]/p'
  landing_distance = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[9]/p'
  takeoff_distance_50 = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[10]/p'
  landing_distance_50 = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[11]/p'
  gross_weight = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[1]/p'
  empty_weight = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[2]/p'
  max_payload = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[3]/p'
  fuel_capacity = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[4]/p'
  ownership_cost = '//*[@id="ownership_costs_top"]/div/dl/dd[1]/h4/span'
  engine_man = '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[1]/p'
  engine_model = '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[2]/p'
  engine_hp = '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[3]/p'
  engine_tbo = '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[4]/p'
  engine_years_tbo = '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[5]/p'


xpaths = {
  'horsepower': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[1]/p',
  'cruise_speed': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[2]/p',
  'best_range': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[3]/p',
  'fuel_burn': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[4]/p',
  'stall_speed': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[5]/p',
  'rate_of_climb': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[6]/p',
  'ceiling': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[7]/p',
  'takeoff_distance': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[8]/p',
  'landing_distance': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[9]/p',
  'takeoff_distance_50': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[9]/p',
  'landing_distance_50': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[11]/p',
  'gross_weight': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[1]/p',
  'empty_weight': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[2]/p',
  'max_payload': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[3]/p',
  'fuel_capacity': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[2]/dd[4]/p',
  'ownership_cost': '//*[@id="ownership_costs_top"]/div/dl/dd[1]/h4/span',
  'engine_man': '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[1]/p',
  'engine_model': '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[2]/p',
  'engine_hp': '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[3]/p',
  'engine_tbo': '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[4]/p',
  'engine_years_tbo': '//*[@id="perforance_top"]/div[1]/div[3]/div/dl/dd[5]/p',
}

xpath_tree = {
  'performance_top': {
    'keys': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dt/p/text()',
      'map': {
        'Best Cruise Speed:': 'cruise',
        'Best Range (i):': 'range',
        'Ceiling:': 'ceiling',
        'Fuel Burn @ 75%:': 'fuel_burn',
        'Horsepower:': 'engine_hp',
        'Landing distance over 50ft obstacle:': 'landing_distance_50',
        'Landing distance:': 'landing_distance',
        'Rate of climb:': 'rate_of_climb',
        'Stall Speed:': 'stall_speed',
        'Takeoff distance over 50ft obstacle:': 'takeoff_distance_50',
        'Takeoff distance:': 'takeoff_distance'
      }
    },
    'values': {
      'path': '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd/p/text()',
      'map': {
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
        'fuel_burn': {
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
          'pattern': r'([\d,]+) GAL',
          'type': int
        }
      }
    }
  },
  'ownership_costs': {
    'keys': {
      'path': '//*[@id="ownership_costs_top"]/div/dl/dt/p/text()',
      'map': {
        'Annual inspection cost:': 'annual_inspection_cost',
      }
    },
    'values': {
      'path': '//*[@id="ownership_costs_top"]/div/dl/dd/p/text()',
      'map': {
        'annual_cost': {
          'pattern': r'^[\\n\s]+\$([\d,\.]+)[\\n\s]+$',
          'type': float
        }
      }
    }
  },
  'engines': {
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
          'pattern': r'([\d,]+) GAL',
          'type': int
        }
      }
    }
  }
}