import unittest
from pyramid import testing


class TestLoginView(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_login_view(self):
        from pythonpackages.views import login
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        response = login(request)
        self.assertEqual(response, {'greeting': 'hello'})
