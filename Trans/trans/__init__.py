from pyramid.config import Configurator
from pyramid.events import NewRequest
from trans.Core.AutoHeader import add_cors_headers_response_callback

def main(global_config, **settings):
	""" This function returns a Pyramid WSGI application.
	"""
	config = Configurator(settings=settings)
	config.add_subscriber(add_cors_headers_response_callback, NewRequest)
	config.add_route('usr', '/usr/{id}')
	config.scan()
	return config.make_wsgi_app()
