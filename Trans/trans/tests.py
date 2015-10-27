import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_cities(self):
        from .views import get_city
        from .views import CITIES
        request = testing.DummyRequest()
        request['name'] = "Paris"
        info = get_city(request)
        print(info["name"])
