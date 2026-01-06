import logging
import requests
from functools import lru_cache
from typing import Optional, Dict, Any

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
    REQUEST_TIMEOUT = 10  # seconds

    def __init__(self, api_key: str, secret: str, user_id: str):
        self.api_key = api_key
        self.secret = secret
        self.user_id = user_id
        self.logger = logging.getLogger(__name__)

    def _make_request(self, method: str, **params) -> Dict[str, Any]:
        """Make a request to the Flickr API with timeout and error handling."""
        default_params = {
            "method": method,
            "api_key": self.api_key,
            "format": "json",
            "nojsoncallback": 1,
        }
        params.update(default_params)

        try:
            response = requests.get(
                self.BASE_URL, params=params, timeout=self.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            self.logger.error(f"Flickr API request timed out for method: {method}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Flickr API error: {str(e)}")
            raise

    def get_photos(
        self,
        page: int = 1,
        per_page: int = 100,
        popular: bool = False,
        tags: Optional[str] = None,
        album_id: Optional[str] = None,
        has_geo: bool = False,
        search_query: Optional[str] = None,
    ) -> Dict[str, Any]:
        params = {
            "user_id": self.user_id,
            "page": page,
            "per_page": per_page,
            "extras": "description,license,date_taken,owner_name,geo,tags,url_sq,url_q,url_t,url_s,url_n,url_m,url_z,url_c,url_l,url_o",
        }

        if has_geo:
            params["has_geo"] = 1

        photos = []

        if search_query:
            method = "flickr.photos.search"
            params["text"] = search_query
            photos = self._make_request(method, **params)
        elif tags:
            method = "flickr.photos.search"
            params["tags"] = tags
            photos = self._make_request(method, **params)
        elif album_id:
            method = "flickr.photosets.getPhotos"
            params["photoset_id"] = album_id
            photos = self._make_request(method, **params)
        elif popular:
            method = "flickr.photos.getPopular"
            photos = self._make_request(method, **params)
        elif has_geo:
            method = "flickr.photos.search"
            photos = self._make_request(method, **params)
        else:
            method = "flickr.people.getPublicPhotos"
            photos = self._make_request(method, **params)

        return photos

    def get_photosets(self, page: int = 1, per_page: int = 100) -> Dict[str, Any]:
        params = {
            "user_id": self.user_id,
            "page": page,
            "per_page": per_page,
            "primary_photo_extras": "license,date_taken,owner_name,geo,tags,url_sq,url_q,url_t,url_s,url_n,url_m,url_z,url_c,url_l,url_o",
        }
        return self._make_request("flickr.photosets.getList", **params)

    def get_photo(self, photo_id: str) -> Optional[Dict[str, Any]]:
        params = {"photo_id": photo_id, "secret": self.secret}
        info = self._make_request("flickr.photos.getInfo", **params)
        exif = self._make_request("flickr.photos.getExif", **params)
        sizes = self._make_request("flickr.photos.getSizes", **params)

        if not info or not exif or not sizes:
            return None

        # Merge additional data into the main info
        merged_data = info
        merged_data["photo"]["exif"] = exif.get("photo", {}).get("exif", [])
        merged_data["photo"]["sizes"] = sizes.get("sizes", {}).get("size", [])

        # Find the largest available size
        largest_img_url = None
        size_order = ["Large 2048", "Large 1600", "Large", "Medium 640", "Medium"]
        for size_label in size_order:
            for size in merged_data["photo"]["sizes"]:
                if size["label"] == size_label:
                    largest_img_url = size["source"]
                    break
            if largest_img_url:
                break

        # Add the largest image URL to the URLs array
        if largest_img_url:
            merged_data["photo"]["urls"]["img_url"] = largest_img_url

        return merged_data
