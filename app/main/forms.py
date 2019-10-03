from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from wtforms import ValidationError
from ..models import User,Order,Role

class OrderForm(FlaskForm):
    productName = TextAreaField('Product Name',validators = [Required()])
    productPrice = TextAreaField('Price',validators = [Required()])
    productCategory = TextAreaField('Product Category',validators = [Required()])
    productQuantity = TextAreaField('Product Quantity',validators = [Required()])
    submit = SubmitField('Oder Now')

    
