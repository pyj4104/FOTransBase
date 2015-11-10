import hashlib
from pyramid.view import view_config
from pyramid.response import Response
from .models import DBSession, Usr
from .Core.Salt import Salt
import json

@view_config(route_name='usr', request_method='OPTIONS')
def OptionUsr(request):
	return request.response

@view_config(route_name='usr', request_method='GET')
def GetUsr(request):
	data = {}
	data['id'] = request.matchdict['id']
	data['success'] = True
	resp = Response(json.dumps(data))
	print(resp)
	return resp

@view_config(route_name='usr', request_method='POST')
def RegisterUsr(request):
	controls = self.request.POST
	ID = request.matchdict['id']
	password = controls['password']
	DBSession.add(Usr(ID, hashlib.sha512(password).hexdigest(), Salt.GenerateSalt()))
