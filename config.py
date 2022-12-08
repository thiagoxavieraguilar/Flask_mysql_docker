from flask_sqlalchemy import SQLAlchemy
from run import app


app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://root:root@localhost/cadastros')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Accounts(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    
with app.app_context():
    db.create_all()