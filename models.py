from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
metadata=MetaData(
    naming_convention={
         "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s",
        "pk": "pk_%(table_name)s"
    }
)

db=SQLAlchemy(metadata=metadata)

#models

class Design(db.Model, SerializerMixin):
    __tablename__=('designs')
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    image_url=db.Column(db.String)
    sales=db.Column(db.Integer)
    uses=db.Column(db.Integer)
    
    def __repr__(self):
        return f'{self.id},{self.name}, {self.image_url}, {self.sales}, {self.uses}'
    
class Category(db.Model, SerializerMixin):
    __tablename__='categories'
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.String)
    image_url_1=db.Column(db.String)
    image_url_2=db.Column(db.String)
    
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.description}, {self.image_url_1}, {self.image_url_2}'
    
class Caption(db.Model, SerializerMixin):
    __tablename__='captions'
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    
    def __repr__(self):
        return f'{self.name}, {self.id}'
    
class User(db.Model, SerializerMixin):
    __tablename__='users'
    
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    username=db.Column(db.String)
    email=db.Column(db.String)
    nationality=db.Column(db.String)
    password=db.Column(db.String)
    
    @validates('email')
    def validate_email(self,key, email):
        
        if not email.endswith ('@gmail.com'):
            raise ValueError("email address must end with @gmail.com")
        return email
    
    def __repr__(self):
        return f'<User {self.id}, {self.first_name}, {self.last_name}, {self.username}, {self.email}, {self.nationality} />'

    