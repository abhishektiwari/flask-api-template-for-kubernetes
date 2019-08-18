"""
Flasky
"""
import os
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models.test import Test

app = create_app(os.getenv('FLASK_ENV') or 'default') # pylint: disable-msg=C0103
migrate = Migrate(app, db) # pylint: disable-msg=C0103


# Run flask shell
@app.shell_context_processor
def make_shell_context():
    """
    Shell context
    """
    return dict(app=app, db=db, Test=Test)

@app.cli.command()
def deploy():
    """Custom deploy"""
    upgrade()

@app.cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    from faker import Faker
    fake = Faker()
    for _ in range(10):
        db.session.add(Test(name=fake.name(), email=fake.email())) # pylint: disable=maybe-no-member
    db.session.commit()

@app.cli.command('recreate_db')
def recreate_db():
    """Run only in dev environment"""
    from utils.colorprint import ColorPrint as _
    env = os.getenv('FLASK_ENV') or 'default'
    if env == 'development' or env == 'default':
        _.print_warn('⚠ Recreating database ⚠')
        db.drop_all()
        db.create_all()
        db.session.commit()
    else:
        _.print_fail('☢ You should not run this in production ☢')

