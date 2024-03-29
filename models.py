from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)

    def to_dict(self):
        return {
            'id': self'id,
            'flavor': self.flavor,
            'size' = self.size,
            'rating': self.rating,
        }
        
def connect_db(app):
    db.app = app
    db.init_app(app)