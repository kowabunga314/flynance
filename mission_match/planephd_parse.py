
from lxml import html
from pprint import pprint
import requests


class PlanePHDParser:
  
  def get_aircraft_performance(self, url=None):
    plane_data = {}
    if url is None:
      # url = 'https://planephd.com/wizard/details/447/MOONEY-M20F-Executive-21-specifications-performance-operating-cost-valuation'
      url = 'https://planephd.com/wizard/details/445/MOONEY-M20E-Super-21-Chaparral-specifications-performance-operating-cost-valuation'
    response = requests.get(url)
    page = html.fromstring(response.content)

    for key in xpaths.keys():
      print(f'Key: {key}')
      print(f'Value: {page.xpath(xpaths[key])[0].text}')
      plane_data[key] = page.xpath(xpaths[key])[0].text

    pprint(plane_data)


class PlanePHDXPathStore:
  horsepower = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[1]/p'
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