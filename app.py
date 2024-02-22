from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET KEY'] = 'bluprint'

connect_db(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/api/cupcakedb')
def cupcake_list():
    cupcakes = [cupcake.to_dict() for cupcake in cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)

@app.route('/api/cupcakedb', methods = ['POST'])
def make_cupcake():
    data = request.json 
    
    cupcake = Cupcake(
        flavor = data['flavor'],
        rating = data['rating'],
        size = data['size'],
        image = data['image'] or None
    )
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake = cupcake.to_dict()), 201)

@app.route('/api/cupcakedb/<int:cupcake_id>')
def retrieve_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.to_dict())

@app.route("/api/cupcakedb/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    data = request.json 
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = 'The cupcake has been deleted.')