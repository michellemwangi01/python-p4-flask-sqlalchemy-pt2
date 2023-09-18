#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet, Owner

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # connects the db to the app before it runs


migrate = Migrate(app, db)

# with app.app_context():
    # pet = Pet(name="Bensson", species="Dog")
    # db.session.add(pet)
    # db.session.commit()
    # print(pet.id)
    #
    # owner = Owner(name="sharky")
    # db.session.add(owner)
    # db.session.commit()
    # print(owner)
    #
    # pet.owner = owner
    # db.session.add(pet)
    # db.session.commit()
    # print(pet.owner)

    # print(Pet.query.all())
    # print(Owner.query.filter(Owner.name >= 'Ben').all())
    # print(Owner.query.filter(Owner.name <= 'Ben').limit(2).all())


@app.route('/')
def index():
    text = '<h1>Welcome to the pet/owner directory!</h1>'
    status_code = 200
    response = make_response(text, status_code)
    return response


@app.route('/pets/<int:id>')
def pets_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    response_body = f'''
     <h1>Information for {pet.name}</h1>
        <h2>Pet Species is {pet.species}</h2>
        <h2>Pet Owner is {pet.owner.name}</h2>
    '''
    response = make_response(response_body, 200)
    return response


@app.route('/owners/<int:id>')
def owners_by_id(id):
    owner = Owner.query.filter(Owner.id == id).first()
    pets = [pet for pet in owner.pets]
    response_body = f'<h1>Information for {owner.name}</h1>'
    if pets:
        for pet in pets:
            response_body += f'<h2>Has pet named {pet.name} of species {pet.species}</h2>'
    else:
        response_body += f'<h2>Has No Pets Yet.</h2>'

    response = make_response(response_body,200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
