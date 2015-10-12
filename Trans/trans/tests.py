import unittest
from pyramid import testing
from trans.Dialogue.DialogueView import DialogueView

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        request = testing.DummyRequest()
        createTest = DialogueView.create(request)
        readTest = DialogueView.read(request)
        updateTest = DialogueView.update(request)
        deleteTest = DialogueView.delete(request)
        self.assertEqual(createTest['test'], 'createSuccess')
        self.assertEqual(readTest['test'], 'readSuccess')
        self.assertEqual(updateTest['test'], 'updateSuccess')
        self.assertEqual(deleteTest['test'], 'deleteSuccess')
