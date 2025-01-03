import logging
import requests
from functools import lru_cache
from urllib.parse import urlencode


class FlickrClient:
    BASE_URL = "https://api.flickr.com/services/rest/"

    def __init__(self, api_key, secret, user_id):
        self.api_key = api_key
        self.secret = secret
        self.user_id = user_id
        self.logger = logging.getLogger(__name__)

    def _make_request(self, method, **params):
        default_params = {
            "method": method,
            "api_key": self.api_key,
            "format": "json",
            "nojsoncallback": 1,
        }
        params.update(default_params)

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Flickr API error: {str(e)}")
            raise

    @lru_cache(maxsize=100)
    def get_photos(self, page=1, per_page=100, tags=None, album_id=None, has_geo=None):
        params = {
            "user_id": self.user_id,
            "page": page,
            "per_page": per_page,
            "extras": "description,license,date_taken,owner_name,geo,url_sq,url_o,url_sq,url_m,url_l,tags",
        }
        if has_geo is not None:
            params["has_geo"] = 1

        if tags:
            method = "flickr.photos.search"
            params["tags"] = tags
        elif album_id:
            method = "flickr.photosets.getPhotos"
            params["photoset_id"] = album_id
        else:
            method = "flickr.people.getPublicPhotos"

        return self._make_request(method, **params)

    @lru_cache(maxsize=100)
    def get_photo_info(self, photo_id):
        params = {"photo_id": photo_id}
        info = self._make_request("flickr.photos.getInfo", **params)

        # Get EXIF data
        exif = self._make_request("flickr.photos.getExif", photo_id=photo_id).get(
            "photo", {}
        )

        # Get direct photo URLs
        sizes = self._make_request("flickr.photos.getSizes", photo_id=photo_id).get(
            "sizes", {}
        )
        info["photo"]["sizes"] = {
            size["label"]: size["source"]
            for size in sizes.get("size", [])
            if size["label"] in ["Thumbnail", "Small", "Medium", "Large"]
        }

        # Combine info with EXIF data
        info["photo"]["exif"] = exif.get("exif", [])
        return info
