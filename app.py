from flask import Flask,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'schema': 'tasks'}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.id = id
        self.email = email

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def hello():
    return 'Hello, Yo!'

@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


if __name__ == '__main__':
    db.create_all()
    app.run()
