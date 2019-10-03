from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,FileField
from wtforms.validators import Required,Email
from wtforms import ValidationError
from ..models import User,Product,Role

class productForm(FlaskForm):
    productName = TextAreaField('Product Name',validators = [Required()])
    productPrice = TextAreaField('Product Price(RWF)',validators = [Required()])
    productCategory = RadioField('Label', choices=[('adultMale', 'Adult male'), ('adultFemale', 'Adult female'),('childFemale', 'Child female'),('childMale', 'Child male')])
    productQuantity = TextAreaField('Product Quantity',validators = [Required()])
    productSize=StringField('Product size',validators=[Required()])
    productPicPath=FileField('Upload Product',validators=[Required()])
    submit = SubmitField('Post Product')

    
