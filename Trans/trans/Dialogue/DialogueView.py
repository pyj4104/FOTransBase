from pyramid.view import view_config
from trans.Base import CRUDBase

class DialogueView(CRUDBase.CRUDBase):
    def __init__(self):
        super().__init__(self)

    @staticmethod
    @view_config(route_name='DialogueCreate', renderer='json')
    def create(request):
        return {'test': 'createSuccess'}

    @staticmethod
    @view_config(route_name='DialogueRead', renderer='json')
    def read(request):
        return {'test': 'readSuccess'}

    @staticmethod
    @view_config(route_name='DialogueUpdate', renderer='json')
    def update(request):
        return {'test': 'updateSuccess'}

    @staticmethod
    @view_config(route_name='DialogueDelete', renderer='json')
    def delete(request):
        return {'test': 'deleteSuccess'}