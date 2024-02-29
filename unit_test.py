import os
import unittest
from unittest.mock import patch, Mock
from dict_flask import get_definition, app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter a word:', response.data)

    @patch('dict_flask.get_definition')
    def test_search_route_with_definition(self, mock_get_definition):
        mock_get_definition.return_value = ('test_id', 'test_definition')
        response = self.client.post('/', data={'word': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_id', response.data)
        self.assertIn(b'test', response.data)
        self.assertIn(b'test_definition', response.data)

    @patch('dict_flask.get_definition')
    def test_search_route_without_definition(self, mock_get_definition):
        mock_get_definition.return_value = (None, 'Word not found')
        response = self.client.post('/', data={'word': 'nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Word not found', response.data)

    @patch('dict_flask.requests.get')
    def test_get_definition_success(self, mock_requests_get):
        # Mocking the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'meta': {'id': 'test_id'}, 'shortdef': ['test_definition']}]
        mock_requests_get.return_value = mock_response

        word_id, definition = get_definition('test')
        self.assertEqual(word_id, 'test_id')
        self.assertEqual(definition, 'test_definition')

    @patch('dict_flask.requests.get')
    def test_get_definition_error(self, mock_requests_get):
        # Mocking a 404 error response from the API
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        word_id, definition = get_definition('test')
        self.assertIsNone(word_id)
        self.assertEqual(definition, 'Error fetching definition')

if __name__ == '__main__':
    unittest.main()
