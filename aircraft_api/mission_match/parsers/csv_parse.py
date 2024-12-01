
import csv
from pprint import pprint


# Mapping of data to row elements on PlanePHD
MAKE = 1
MODEL = 2
YEARS = 3
ANNUAL_COST = 4
TBO = 5
ENGINE = 6
ENGINE_HP = 7
FUEL_BURN = 8
CRUISE = 9
STALL = 10
CEILING = 11
TAKEOFF_DISTANCE = 12
LANDING_DISTANCE = 13
GEAR = 14
FLAPS = 15
GROSS_WEIGHT = 16
EMPTY_WEIGHT = 17
FUEL_CAPACITY = 17
RANGE = 20
HAS_AUTOPILOT = 22
ENGINE_MONITOR = 23


def read_aircraft_from_csv(input_file):
  aircraft_types = []
  with open(input_file, 'r') as data_sheet:
    reader = csv.reader(data_sheet)
    for row in reader:
      year_start, year_end = parse_model_year_range(row[YEARS])
      aircraft_types.append(dict(
        make=row[MAKE],
        model=row[MODEL],
        model_year_start=int(year_start),
        model_year_end=int(year_end),
        annual_cost=row[ANNUAL_COST],
        tbo=row[TBO],
        engine=row[ENGINE],
        engine_hp=row[ENGINE_HP],
        fuel_burn=row[FUEL_BURN],
        cruise=row[CRUISE],
        stall=row[STALL],
        ceiling=row[CEILING],
        takeoff_distance=row[TAKEOFF_DISTANCE],
        landing_distance=row[LANDING_DISTANCE],
        gear_type=row[GEAR],
        flaps=row[FLAPS],
        gross_weight=row[GROSS_WEIGHT],
        empty_weight=row[EMPTY_WEIGHT],
        range=row[RANGE],
        has_autopilot=row[HAS_AUTOPILOT],
        engine_monitor=row[ENGINE_MONITOR]
      ))

  return aircraft_types

def parse_model_year_range(years):
  return years.split('-')
