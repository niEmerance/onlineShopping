from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Product
from .. import db,photos
from .forms import productForm
from werkzeug.utils import secure_filename
# from flask_login import login_required,current_user
import datetime
# from ..email import mail_subscribemessage

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    product=Product.query.all()
    title = 'Home - Welcome to product website'
    adultMale = Product.query.filter_by(productCategory='adultMale')
    adultFemale= Product.query.filter_by(productCategory='adultFemale')
    childMale = Product.query.filter_by(productCategory='childMale')
    childFemale = Product.query.filter_by(productCategory='childFemale')


    return render_template('index.html',title = title,adultMale=adultMale,adultFemale=adultFemale,childMale=childMale,childFemale=childFemale)



@main.route('/product/new', methods = ['GET','POST'])
def newProduct():
    form = productForm()
    # order= Order.query.filter_by(id=id).first()
    if form.validate_on_submit():
        productName = form.productName.data
        productPrice= form.productPrice.data
        productCategory = form.productCategory.data
        productSize=form.productSize.data
        productQuantity = form.productQuantity.data
        productPicPath=form.productPicPath.data
        filename=photos.save(form.productPicPath.data)
        path=f'photos/{filename}'
        newProduct = Product(productName=productName,productPrice=productPrice,productCategory=productCategory,productSize=productSize,productQuantity=productQuantity,productPicPath=path)
        
        # newBlog.saveBlog()
        db.session.add(newProduct)
        db.session.commit()
        return redirect(url_for('.newProduct'))
    title = 'New Product'
    return render_template('product.html',title = title,form=form)










    