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
    
    for page_section in xpath_tree:
      pt_keys = [k for k in tree.xpath(xpath_tree[page_section]['keys']['path']) if k in xpath_tree[page_section]['keys']['map']]
      pt_values = tree.xpath(xpath_tree[page_section]['values']['path'])

      # if len(pt_keys) != len(pt_values):
      #   raise ValueError('Key/Value count does not match on performance top scrape')
      
      for i, key in enumerate(pt_keys):
        if key not in xpath_tree[page_section]['keys']['map']:
          continue
        clean_key = xpath_tree[page_section]['keys']['map'][key]
        match = re.search(xpath_tree[page_section]['values']['map'][clean_key]['pattern'], pt_values[i])
        clean_value = xpath_tree[page_section]['values']['map'][clean_key]['type'](match.group(1).replace(',', ''))
        # clean_value = clean_value.replace(',', '')
        plane_data[clean_key] = clean_value

    pprint(plane_data)


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