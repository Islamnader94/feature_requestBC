from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_fixtures import load_fixtures
app = Flask(__name__)
# Set up the SQLAlchemy Database to be a local file 'features.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///features.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
from views import *
import os
import json
import argparse
import models


description = """Utility function for running various flask commands."""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('command', nargs="?")
    args = parser.parse_args()

    if args.command == 'runserver':
        app.run(host='0.0.0.0')
    elif args.command == 'drop_db':
        models.db.drop_all()
    elif args.command == 'create_db':
        models.db.create_all()
    elif args.command == 'init_db':
        # we know that no dirs are there in the fixtures path, so safe to
        # iterate
        for fixture in os.listdir('fixtures'):
            fixture_path = os.path.join('fixtures', fixture)
            with open(fixture_path, 'r') as infile:
                load_fixtures(models.db, json.loads(infile.read()))
