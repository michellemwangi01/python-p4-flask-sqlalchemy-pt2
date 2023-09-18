from models import db, Pet, Owner
from app import app



with app.app_context():
    Pet.query.all()