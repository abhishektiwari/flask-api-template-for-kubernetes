"""
Extensions module. 
Each extension is initialized in the app factory located in app.py.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy() #pylint: disable=invalid-name
ma = Marshmallow() #pylint: disable=invalid-name
mg = Migrate() #pylint: disable=invalid-name
