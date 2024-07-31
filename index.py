from inicio import app
from utils.repositorios.sqlAlchemy.conexionBd import db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
