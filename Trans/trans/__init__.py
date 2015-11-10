from pyramid.config import Configurator
from pyramid.events import NewRequest
from sqlalchemy import engine_from_config
from .models import DBSession, Base
from trans.Core.AutoHeader import add_cors_headers_response_callback

def main(global_config, **settings):
	""" This function returns a Pyramid WSGI application."""
	engine = engine_from_config(settings, 'sqlalchemy.')
	DBSession.configure(bind=engine)
	Base.metadata.bind = engine
	config = Configurator(settings=settings)
	config.add_subscriber(add_cors_headers_response_callback, NewRequest)
	config.add_route('usr', '/usr/{id}')
	config.scan('.views')
	return config.make_wsgi_app()
