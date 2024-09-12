from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from marshmallow_sqlalchemy.convert import ModelConverter
from .models import Manufacturer, Model, Engine


# class ManufacturerConverter(ModelConverter):
#     pass


class ManufacturerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Manufacturer
        # converter = ManufacturerConverter
        include_relationships = True
        load_instance = True

    models = fields.List(fields.Nested(lambda: ModelSchema(only=("id", "name"))))



class ModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Model
        include_fk = True
        load_instance = True

    engines = fields.List(fields.Nested(lambda: EngineSchema(only=("id", "type"))))
    useful_load = fields.Method("get_useful_load")
    endurance = fields.Method("get_endurance")

    def get_useful_load(self, obj):
        return obj.useful_load

    def get_endurance(self, obj):
        return obj.endurance

class EngineSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Engine
        include_fk = True
        load_instance = True
