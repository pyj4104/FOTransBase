import trans.Flags

class CRUDBase():
    @staticmethod
    def create(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    def read(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    def update(request):
        raise NotImplementedError("Cannot use base abstract method")

    @staticmethod
    def delete(request):
        raise NotImplementedError("Cannot use base abstract method")