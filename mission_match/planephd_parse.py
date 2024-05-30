
from lxml import html
import requests


class PlanePHDParser:
  pass


class XPathStore:
  horsepower = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[1]/p'
  cruise_speed = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[2]/p'
  best_range= '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[3]/p'
  fuel_burn = '//*[@id="perforance_top"]/div[1]/div[1]/div/dl[1]/dd[4]/p'
  stall_speed = ''
  rate_of_climb = ''
  ceiling = ''
  takeoff_distance = ''
  landing_distance = ''
  takeoff_distance_50 = ''
  landing_distance_50 = ''
  gross_weight = ''
  empty_weight = ''
  max_payload = ''
  fuel_capacity = ''
  ownership_cost = ''
  engine_man = ''
  engine_model = ''
  engine_hp = ''
  engine_tbo = ''
  engine_years_tbo = ''