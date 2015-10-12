import abc

class CRUDBase():
    __metadata__ = abc.ABCMeta

    @staticmethod
    @abc.abstractstaticmethod
    def create(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    @abc.abstractstaticmethod
    def read(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    @abc.abstractstaticmethod
    def update(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    @abc.abstractstaticmethod
    def delete(request):
        raise NotImplementedError("Cannot use base abstract method")