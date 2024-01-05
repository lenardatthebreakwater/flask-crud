from app import app, db

try:
    app.app_context().push()
    db.create_all()
    print("Database was successfully created!")
except:
    print("There was an error creating the database!")

