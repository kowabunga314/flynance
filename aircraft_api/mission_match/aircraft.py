

class AircraftType():
  """
  AircraftType This class models an aircraft type (i.e. Cessna 172SP).

  The AircraftType class represents all of the data that should be considered when purchasing
    an aircraft. Default data laid out in this class can be used to drive field data in the
    Aircraft class.
  """
  FIXED_GEAR = 'fixed'
  MANUAL_GEAR = 'manual'
  AUTO_GEAR = 'auto'
  GEAR_TYPES = (FIXED_GEAR, MANUAL_GEAR, AUTO_GEAR)

  MANUAL_FLAPS = 'manual'
  AUTO_FLAPS = 'auto'
  NO_FLAPS = None
  FLAP_TYPES = (MANUAL_FLAPS, AUTO_FLAPS, NO_FLAPS)

  ANALOG_EM = 'analog'
  DIGITAL_EM = 'digital'
  EM_TYPES = (ANALOG_EM, DIGITAL_EM)

  make = 'Mooney'
  model = 'M20F'
  model_year_start = 1960
  model_year_end = 1970
  estimated_value = 100000
  total_cost_of_ownership = 10000
  total_fixed_cost = 5000
  total_variable_cost = 5000
  annual_inspection_cost = 2000
  tbo = 2000
  fuel_burn = 10
  fuel_burn_cruise = 10
  fuel_capacity = 50
  fuel_unit = 'gallon'
  cruise = 150
  stall_speed = 50
  ceiling = 15000
  ceiling_eo = None
  takeoff_distance = 1000
  landing_distance = 1000
  takeoff_distance_50 = 1500
  landing_distance_50 = 1500
  gear_type = FIXED_GEAR
  flaps = AUTO_FLAPS
  gross_weight = 2500
  empty_weight = 1500
  max_payload = 1000
  range = 500
  rate_of_climb = 1000
  rate_of_climb_eo = None
  has_autopilot = False
  engine_manufacturer = 'Engine Designation'
  engine_model = 'Engine Designation'
  engine_hp = 180
  engine_tbo = 1800
  engine_tbo_years = 12
  
  def __init__(self, *args, **kwargs):
    for key in kwargs.keys():
      if hasattr(self, key):
        setattr(self, key, kwargs[key])

  @property
  def useful_load(self):
    return self.gross_weight - self.empty_weight

  @property
  def endurance(self):
    return self.fuel_burn * self.fuel_capacity
  

class Aircraft(AircraftType):
  """
  Aircraft This class represents an instance of an AircraftType.

  The Aircraft class corresponds to a specific aircraft (e.g. a physical object).
  """
  VISUAL_RULES = 'VFR'
  INSTRUMENT_RULES = 'IFR'
  FLIGHT_RULES = (VISUAL_RULES, INSTRUMENT_RULES)

  listing = 'https://controller.com/airplane'
  value = 100000
  airframe_hours = 2500
  engine_hours = 250
  prop_hours = 250
  exterior_rating = 5
  interior_rating = 5
  avionics_rating = 5
  upgrades_rating = 5
  coj_rating = 5
  flight_rules = VISUAL_RULES
  upgrade_notes = ''
  general_notes = ''

  def aggregate_point_ratings(self) -> float:
    return (
      self.exterior_rating
      + self.interior_rating
      + self.avionics_rating
      + self.upgrades_rating
      + self.coj_rating
    ) / 5
