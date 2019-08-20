"""
Create test model
"""
from marshmallow import ValidationError, validates_schema, post_load
from app import db, ma

class Test(db.Model):
    """Test data model"""
    _tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_json(self):
        """
        Convert to JSON object
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class TestSchema(ma.ModelSchema):
    """Marshmallow scheam for test"""
    class Meta:
        """
        Strict for loading
        """
        model = Test
        strict =True

    @post_load
    def make_instance(self, data): #pylint: disable=arguments-differ
        """
        Return as dict or model
        """
        # return Test(**data)
        return data

    @validates_schema
    def validate_name(self, data):
        """
        Validate name
        """
        try:
            data['name']
        except Exception:
            raise ValidationError({'name': 'Missing name'})

    @validates_schema
    def validate_email(self, data):
        """
        Validate email
        """
        try:
            data['email']
        except Exception:
            raise ValidationError({'email': 'Missing email'})
