from unittest import TestCase
from app import app 
from models import db, Cupcake

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_cupcakedb'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

db.drop_all()
db.create_all()

cupcake_data = {
    "flavor": "test_Flavor",
    "size": "test_Size",
    "rating": 7,
}

cupcake_data_2 {
    'flavor': 'test_flavor_2',
    'size': 'test_size_2',
    'rating': 4
}

class CupcakeTestCases(TestCase):
    def start(self):
        Cupcake.query.delete()
        cupcake = Cupcake(**cupcake_data)
        db.session.add(cupcake)
        db.session.commit()

        self.cupcake = cupcake
    
    def end(self):
        db.session.rollback()

    def list_test(self):
        with app.test_client() as client:
            resp = client.get('/api/cupcakes')

            self.assertEqual(resp/status_code, 200)

             data = resp.json
            self.assertEqual(data, {
                "cupcakes": [
                    {
                        "id": self.cupcake.id,
                        "flavor": "test_Flavor",
                        "size": "test_Size",
                        "rating": 7,
                    }
                ]
            })

    def delete_test(self):
        cupcake = Cupcake(flavor = 'test_Flavor', size = 'test_Size', rating = 7)
        db.session.add(cupcake)
        db.session.commit()

            response = self.app.delete(f'/api/cupcakedb/{cupcake.id}')
            self.assertEqual(resp/status_code, 200)
            
            delete_cupcake = Cupcake.query.get(cupcake.id)
            self.assertIsNone(delete_cupcake)

            expected_message = {'message': 'The cupcake has been deleted.'}
            self.assertEqual(response.get_json(), expected_message)