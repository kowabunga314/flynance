from flask import Blueprint, jsonify, request
from .models import Manufacturer, Model, Engine
from . import db
from .schemas import ManufacturerSchema, ModelSchema, EngineSchema

bp = Blueprint('api', __name__)

manufacturer_schema = ManufacturerSchema()
manufacturers_schema = ManufacturerSchema(many=True)
model_schema = ModelSchema()
models_schema = ModelSchema(many=True)
engine_schema = EngineSchema()
engines_schema = EngineSchema(many=True)

@bp.route('/manufacturers', methods=['GET'])
def get_manufacturers():
    manufacturers = Manufacturer.query.all()
    return manufacturers_schema.dump(manufacturers)

@bp.route('/manufacturers', methods=['POST'])
def create_manufacturer():
    data = request.get_json()
    manufacturer = manufacturer_schema.load(data)
    db.session.add(manufacturer)
    db.session.commit()
    return manufacturer_schema.dump(manufacturer), 201

@bp.route('/models', methods=['GET'])
def get_models():
    models = Model.query.all()
    return models_schema.dump(models)

@bp.route('/models', methods=['POST'])
def create_model():
    data = request.get_json()
    model = model_schema.load(data)
    db.session.add(model)
    db.session.commit()
    return model_schema.dump(model), 201

@bp.route('/engines', methods=['GET'])
def get_engines():
    engines = Engine.query.all()
    return engines_schema.dump(engines)

@bp.route('/engines', methods=['POST'])
def create_engine():
    data = request.get_json()
    engine = engine_schema.load(data)
    db.session.add(engine)
    db.session.commit()
    return engine_schema.dump(engine), 201
