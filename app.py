from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from models import db, Design, Category, Caption, User
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token, jwt_required, unset_jwt_cookies
from flask_migrate import Migrate
import os
from flask_cors import CORS
from flask_bcrypt import Bcrypt



app=Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URI')
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config ['JWT_SECRET_KEY']= os.urandom(32).hex()
app.json.compact=False

migrate=Migrate(app, db)
jwt=JWTManager(app)
db.init_app(app)
api=Api(app)
cors=CORS(app)
bcrypt=Bcrypt(app)

class Index(Resource):
    def get(self):
        return jsonify({"message":"Welcome to postermywall suggested upgrade server"})
    
#user registration

class User_register(Resource):
    def post(self):
        data=request.json
        
        if data['password'] != data['confirm_password']:
            return jsonify({"message" : "passwords do not match!"})
        
        hashed_password=bcrypt.generate_password_hash(data['password'].encode('utf-8'))
        
        new_user=User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'],
            email=data['email'],
            nationality=data['nationality'],
            password=hashed_password,
            
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        response_message={"message":"user registered successfully"}
        response=make_response(response_message, 201)
        return response
    
api.add_resource(User_register, '/users/register')

class UserLogin(Resource):
    def post(self, id):
        
        data=request.json
        username=data['username']
        password=data['password']
        
        user_exists=User.query.filter(id==id).first()
        
        if user_exists:
            access_token=create_access_token(identity='username')
            
            token={
                "id":user_exists.id,
                "username":user_exists.username,
                "first_name":user_exists.first_name,
                "last_name":user_exists.last_name,
                "email":user_exists.email,
                "nationality":user_exists.nationality,
                "access_token":access_token
            }
            
            return jsonify(token)
        response=make_response("successfully logged in", 200)
        return response
api.add_resource(UserLogin, '/users/login/<int:id>')

class LogOut(Resource):
    @jwt_required
    def post(self):
        unset_jwt_cookies()
        return jsonify({"message ":"successfully logged out!"})
    
api.add_resource(LogOut, '/users/logout')
          
class Designs(Resource):
    def get(self):
        designs=[design.to_dict() for design in Design.query.all()]
        response=make_response(designs, 200)
        return response
    
    def post(self):
        
        data=request.json
        
        new_design=Design(
            name=data.get('name'),
            sales=data.get('sales'),
            uses=data.get('uses'),
            image_url=data.get('image_url')
        )
        
        db.session.add(new_design)
        db.session.commit()
        
        new_design_dict=new_design.to_dict()
        response=make_response(new_design_dict, 201)
        return response
api.add_resource(Designs, '/designs')


class CategorizeDesign(Resource):
    
    def get(self, id):   
        design_by_id=Design.query.filter(Design.id==id).first()
        response_dict=design_by_id.to_dict()
        response=make_response(response_dict, 200)
        return response
        
        
    def patch(self, id):
        
        design_to_categorize=Design.query.filter(Design.id==id).first()
        
        for attr in request.json:
            setattr(design_to_categorize, attr, request.json[attr])
            
        response_dict=design_to_categorize.to_dict()
        db.session.add(design_to_categorize)
        db.session.commit()
            
            
        response=make_response(response_dict, 203)
        return response
api.add_resource(CategorizeDesign, '/design_by_id/<int:id>')   

class Categories(Resource):
    def get(self):
        categories=[category.to_dict() for category in Category.query.all()]
        response=make_response(categories, 200)
        return response
    
api.add_resource(Categories, '/categories')

if __name__ == '__main__':
    app.run(port=5555, debug=True)