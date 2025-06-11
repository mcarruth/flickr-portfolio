import unittest
from unittest.mock import patch, Mock
import requests

from flickr_client import FlickrClient


class TestFlickrClient(unittest.TestCase):
    def setUp(self):
        self.client = FlickrClient(api_key="key", secret="sec", user_id="user")

    @patch("flickr_client.requests.get")
    def test_make_request_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"ok": True}
        mock_get.return_value = mock_response

        data = self.client._make_request("flickr.test.echo", param="value")
        self.assertEqual(data, {"ok": True})
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn("params", kwargs)
        self.assertEqual(kwargs["params"]["method"], "flickr.test.echo")
        self.assertEqual(kwargs["params"]["param"], "value")

    @patch("flickr_client.requests.get")
    def test_make_request_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("boom")
        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            self.client._make_request("flickr.test.echo")

    @patch.object(FlickrClient, "_make_request")
    def test_get_photos_search_query(self, mock_request):
        mock_request.return_value = {}
        self.client.get_photos(search_query="cats", page=2, per_page=5)
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "flickr.photos.search")
        self.assertEqual(kwargs["text"], "cats")
        self.assertEqual(kwargs["page"], 2)
        self.assertEqual(kwargs["per_page"], 5)


if __name__ == "__main__":
    unittest.main()
