from app import app
from model.field_model import field_model

obj = field_model()

@app.route('/field')
def field():
    return obj.filed_model_field()