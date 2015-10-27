from pyramid.view import view_config
from pyramid.response import Response
import json

User = {
    'test': {
        'id': 'testID',
        'password': 'testPassword'
    }
}

@view_config(route_name='usr', request_method='GET')
@view_config(route_name='usr', request_method='OPTIONS')
def get_city(request):
    id = request.matchdict['id']
    resp = Response(json.dumps(User[id]))
    print(resp)
    return resp