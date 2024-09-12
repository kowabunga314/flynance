from . import db

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    models = db.relationship('Model', backref='manufacturer', lazy=True)

class Model(db.Model):
    __tablename__ = 'models'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'), nullable=False)
    fixed_gear = db.Column(db.Boolean, nullable=False, default=False)
    manual_gear = db.Column(db.Boolean, nullable=False, default=False)
    auto_gear = db.Column(db.Boolean, nullable=False, default=False)
    manual_flaps = db.Column(db.Boolean, nullable=False, default=False)
    auto_flaps = db.Column(db.Boolean, nullable=False, default=False)
    no_flaps = db.Column(db.Boolean, nullable=False, default=False)
    analog_em = db.Column(db.Boolean, nullable=False, default=False)
    digital_em = db.Column(db.Boolean, nullable=False, default=False)
    model_year_start = db.Column(db.Integer, nullable=False)
    model_year_end = db.Column(db.Integer, nullable=False)
    estimated_value = db.Column(db.Float, nullable=False)
    total_cost_of_ownership = db.Column(db.Float, nullable=False)
    total_fixed_cost = db.Column(db.Float, nullable=False)
    total_variable_cost = db.Column(db.Float, nullable=False)
    annual_inspection_cost = db.Column(db.Float, nullable=False)
    tbo = db.Column(db.Integer, nullable=False)
    fuel_burn = db.Column(db.Float, nullable=False)
    fuel_burn_cruise = db.Column(db.Float, nullable=False)
    fuel_capacity = db.Column(db.Float, nullable=False)
    fuel_unit = db.Column(db.String(20), nullable=False)
    cruise = db.Column(db.Integer, nullable=False)
    stall_speed = db.Column(db.Integer, nullable=False)
    ceiling = db.Column(db.Integer, nullable=False)
    ceiling_eo = db.Column(db.Integer, nullable=True)
    takeoff_distance = db.Column(db.Integer, nullable=False)
    landing_distance = db.Column(db.Integer, nullable=False)
    takeoff_distance_50 = db.Column(db.Integer, nullable=False)
    landing_distance_50 = db.Column(db.Integer, nullable=False)
    gross_weight = db.Column(db.Integer, nullable=False)
    empty_weight = db.Column(db.Integer, nullable=False)
    max_payload = db.Column(db.Integer, nullable=False)
    range = db.Column(db.Integer, nullable=False)
    rate_of_climb = db.Column(db.Integer, nullable=False)
    rate_of_climb_eo = db.Column(db.Integer, nullable=True)
    has_autopilot = db.Column(db.Boolean, nullable=False, default=False)
    engines = db.relationship('Engine', backref='model', lazy=True)

    @property
    def useful_load(self):
        return self.gross_weight - self.empty_weight

    @property
    def endurance(self):
        return self.fuel_burn * self.fuel_capacity

class Engine(db.Model):
    __tablename__ = 'engines'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'), nullable=False)
    engine_manufacturer = db.Column(db.String(80), nullable=False)
    engine_model = db.Column(db.String(80), nullable=False)
    engine_hp = db.Column(db.Integer, nullable=False)
    engine_tbo = db.Column(db.Integer, nullable=False)
    engine_tbo_years = db.Column(db.Integer, nullable=False)
