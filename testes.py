from main import app, database
from models import Usuario, Post

# with app.app_context():
#     database.create_all()
#
# with app.app_context():
#     usuario = Usuario(username="Italo", email="italo3040@gmail.com", senha="123456")
#
#     database.session.add(usuario)
#
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.email)

with app.app_context():
    database.drop_all()
    database.create_all()