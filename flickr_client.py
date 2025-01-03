import logging
import requests
from functools import lru_cache
from urllib.parse import urlencode

# url_sq : s	small square 75x75
# url_q  : q	large square 150x150
# url_t  : t	thumbnail, 100 on longest side
# url_s  : m	small, 240 on longest side
# url_n  : n	small, 320 on longest side
# url_m  : -	medium, 500 on longest side
# url_z  : z	medium 640, 640 on longest side
# url_c  : c	medium 800, 800 on longest side†
# url_l  : b	large, 1024 on longest side*
# url_o  : o	original image, either a jpg, gif or png, depending on source format


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
    def get_photos(
        self,
        page=1,
        per_page=100,
        tags=None,
        album_id=None,
        has_geo=False,
        search_query=None,
    ):
        params = {
            "user_id": self.user_id,
            "page": page,
            "per_page": per_page,
            "extras": "description,license,date_taken,owner_name,geo,tags,url_sq,url_q,url_t,url_s,url_n,url_m,url_z,url_c,url_l,url_o",
        }

        if has_geo:
            params["has_geo"] = 1

        photos = []

        if tags:
            method = "flickr.photos.search"
            params["tags"] = tags
            photos = self._make_request(method, **params)
        elif album_id:
            method = "flickr.photosets.getPhotos"
            params["photoset_id"] = album_id
            photos = self._make_request(method, **params)
        elif has_geo:
            method = "flickr.photos.search"
            photos = self._make_request(method, **params)
        elif search_query:
            method = "flickr.photos.search"
            params["text"] = search_query
            photos = self._make_request(method, **params)
        else:
            method = "flickr.people.getPublicPhotos"
            photos = self._make_request(method, **params)

        return photos

    @lru_cache(maxsize=100)
    def get_photosets(self, page=1, per_page=100):
        params = {
            "user_id": self.user_id,
            "page": page,
            "per_page": per_page,
            "primary_photo_extras": "license,date_taken,owner_name,geo,tags,url_sq,url_q,url_t,url_s,url_n,url_m,url_z,url_c,url_l,url_o",
        }
        return self._make_request("flickr.photosets.getList", **params)

    @lru_cache(maxsize=100)
    def get_tags(self):
        params = {"user_id": self.user_id, "count": 1000}
        return self._make_request("flickr.tags.getListUserPopular", **params)

    @lru_cache(maxsize=100)
    def get_profile(self):
        params = {"user_id": self.user_id}
        return self._make_request("flickr.profile.getProfile", **params)

    @lru_cache(maxsize=100)
    def get_exif(self, photo_id):
        params = {"photo_id": photo_id, "secret": self.secret}
        return self._make_request("flickr.photos.getExif", **params)
