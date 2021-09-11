""" Seed file to make sample data to pets_db """
from models import Pet, db 
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

barsik = Pet(name="Barsik", species="cat", age=3)
pushkin = Pet(name="Pushkin", species="dog", photo_url="https://images.unsplash.com/photo-1608831540955-35094d48694a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=753&q=80", age=5)
tesla = Pet(name="Tesla", species="dog", photo_url="https://images.unsplash.com/photo-1589642344659-02a33f7d9f25?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80")
murka = Pet(name="Murka", species="cat", age=3, available=False)
pitt = Pet(name="Pitt", species="dog", photo_url="https://images.unsplash.com/photo-1598875706250-21faaf804361?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=663&q=80", age=7, available=False)
lucky = Pet(name="Lucky", species="dog", photo_url="https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=639&q=80")

db.session.add_all([barsik, pushkin, tesla, murka, pitt, lucky])
db.session.commit()

