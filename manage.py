import sys
import unittest
import os

import coverage

from flask_script import Manager

from app import create_app, db

manager = Manager(create_app)


@manager.command
def createdb(drop_first=False):
    """Creates the database."""
    if drop_first:
        db.drop_all()
    db.create_all()


@manager.command
def test():
    """Runs unit tests."""
    os.environ['FLACK_CONFIG'] = 'testing'
    omit_items = [
        'manage.py',
        '*venv*/*',
        '*/serverapp351/*'
    ]

    # start coverage engine
    cov = coverage.Coverage(branch=True)
    cov.start()

    # run tests
    tests = unittest.TestLoader().discover('.')
    ok = unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()

    # print coverage report
    cov.stop()
    cov.report(omit=omit_items)

    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    manager.run()
