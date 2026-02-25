import pytest
from app import create_app
from app.extensions import db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()
    _db.create_all()
    yield app
    _db.drop_all()
    ctx.pop()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db(app):
    yield _db
    _db.session.rollback()
