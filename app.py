from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "something_very_secret_here"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """ Renders list of pets and their availability """
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/new', methods=["GET", "POST"])
def add_pet_form():
    """Renders add pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm()

    # if we need to add choices dinamically: 
    #########################################
    # species = db.session.query(Pet.species)
    # form.species.choices = species

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)  


@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """ Shows pet info and allows edit the pet """
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    
    # debugging:
    ########################
    # if form.is_submitted():
    #     print("submitted")
    # if form.validate():
    #     print("valid")
    # print(form.errors)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet_info.html", form=form, pet=pet)
