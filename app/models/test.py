"""
Create test model
"""
from app import db, ma

class Test(db.Model):
    """Test data model"""
    _tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class TestSchema(ma.ModelSchema):
    """Marshmallow scheam for test"""
    class Meta:
        model = Test