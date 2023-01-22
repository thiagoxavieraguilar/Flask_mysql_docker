from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#conexão bd
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://root:root@localhost/cadastros')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
db = SQLAlchemy(app)
