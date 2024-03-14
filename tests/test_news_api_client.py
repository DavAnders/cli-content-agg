from pathlib import Path
import sys

# issues with import, this works right now. running main with (python -m src.main)
root_dir = str(Path(__file__).resolve().parent.parent)
if root_dir not in sys.path:
    sys.path.append(root_dir)

import unittest
from unittest.mock import patch, MagicMock
from src.news_api_client import fetch_everything

class NewsAPIClientTestCase(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_everything(self, mock_get):
        # mock to return a response with example article data
        example_response = {
            'status': 'ok',
            'articles': [
                {
                    'title': 'Test Article',
                    'content': 'Test content',
                    'url': 'http://google.com',
                    'publishedAt': '2024-03-14T12:25:33Z',
                }
            ]
        }
        mock_get.return_value = MagicMock(status_code=200, json=lambda: example_response)

        # function call
        result = fetch_everything('test')

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], 'Test Article')
        self.assertEqual(result[0]['content'], 'Test content')
        self.assertEqual(result[0]['url'], 'http://google.com')

if __name__ == '__main__':
    unittest.main()
