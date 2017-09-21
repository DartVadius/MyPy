from flask import Flask
from app.database import db_session

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'None'
app.config['SECRET_KEY'] = 'very-very-secret-key'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from app import views, models
