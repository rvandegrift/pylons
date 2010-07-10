import unittest

class LegacyViewTests(unittest.TestCase):
    def _makeOne(self, app):
        from pylons.views import LegacyView
        return LegacyView(app)

    def test_with_subpath_and_view_name(self):
        request = DummyRequest()
        request.traversed = ['a', 'b']
        request.virtual_root_path = ['a']
        request.subpath = ['subpath']
        request.view_name = 'view_name'
        request.environ = {'SCRIPT_NAME':'/foo'}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/subpath/view_name')
        self.assertEqual(request.environ['SCRIPT_NAME'], '/foo/b')
        
    def test_with_subpath_no_view_name(self):
        request = DummyRequest()
        request.traversed = ['a', 'b']
        request.virtual_root_path = ['a']
        request.subpath = ['subpath']
        request.view_name = ''
        request.environ = {'SCRIPT_NAME':'/foo'}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/subpath/')
        self.assertEqual(request.environ['SCRIPT_NAME'], '/foo/b')

    def test_no_subpath_with_view_name(self):
        request = DummyRequest()
        request.traversed = ['a', 'b']
        request.virtual_root_path = ['a']
        request.subpath = []
        request.view_name = 'view_name'
        request.environ = {'SCRIPT_NAME':'/foo'}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/view_name')
        self.assertEqual(request.environ['SCRIPT_NAME'], '/foo/b')

    def test_traversed_empty_with_view_name(self):
        request = DummyRequest()
        request.traversed = []
        request.virtual_root_path = []
        request.subpath = []
        request.view_name = 'view_name'
        request.environ = {'SCRIPT_NAME':'/foo'}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/view_name')
        self.assertEqual(request.environ['SCRIPT_NAME'], '/foo')

    def test_traversed_empty_no_view_name(self):
        request = DummyRequest()
        request.traversed = []
        request.virtual_root_path = []
        request.subpath = []
        request.view_name = ''
        request.environ = {'SCRIPT_NAME':'/foo'}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/')
        self.assertEqual(request.environ['SCRIPT_NAME'], '/foo')

    def test_traversed_empty_no_view_name_no_script_name(self):
        request = DummyRequest()
        request.traversed = []
        request.virtual_root_path = []
        request.subpath = []
        request.view_name = ''
        request.environ = {'SCRIPT_NAME':''}
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)
        self.assertEqual(request.environ['PATH_INFO'], '/')
        self.assertEqual(request.environ['SCRIPT_NAME'], '')

def dummyapp(environ, start_response):
    """ """

class DummyRequest:
    def get_response(self, application):
        return application
