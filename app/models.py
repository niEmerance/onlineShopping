from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    # productId = db.relationship('Product',backref = 'user',lazy = "dynamic")
    # orderId = db.relationship('Order',backref = 'product',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(20))
    productPrice = db.Column(db.Integer)
    productCategory = db.Column(db.String(25))
    productQuantity= db.Column(db.Integer)
    productSize=db.Column(db.String(25))
    productPicPath = db.Column(db.String(120))
    # userId = db.Column(db.Integer,db.ForeignKey("users.id"))
    # productId = db.Column(db.Integer,db.ForeignKey("products.id"))
    

    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def getProduct(cls,id):
        product = product.query.filter_by(userId=id).all()
        return product

class Role(db.Model):
    __tablename__='roles'

    id=db.Column(db.Integer,primary_key=True)
    admin=db.Column(db.String(255))
    user=db.Column(db.String(255))
    # userId = db.Column(db.Integer,db.ForeignKey("users.id"))


     


 

