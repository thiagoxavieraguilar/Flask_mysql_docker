from config import db,app

class Accounts(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
with app.app_context():
    db.create_all()