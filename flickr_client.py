import logging
import requests
from functools import lru_cache
from urllib.parse import urlencode

class FlickrClient:
    BASE_URL = 'https://api.flickr.com/services/rest/'
    
    def __init__(self, api_key, secret, user_id):
        self.api_key = api_key
        self.secret = secret
        self.user_id = user_id
        self.logger = logging.getLogger(__name__)

    def _make_request(self, method, **params):
        default_params = {
            'method': method,
            'api_key': self.api_key,
            'format': 'json',
            'nojsoncallback': 1,
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
    def get_photos(self, page=1, per_page=100, tags=None, album_id=None):
        params = {
            'user_id': self.user_id,
            'page': page,
            'per_page': per_page,
            'extras': 'description,date_taken,geo,tags,url_sq,url_m,url_l'
        }
        
        if tags:
            params['tags'] = ','.join(tags)
        
        if album_id:
            method = 'flickr.photosets.getPhotos'
            params['photoset_id'] = album_id
        else:
            method = 'flickr.people.getPublicPhotos'
        
        return self._make_request(method, **params)

    @lru_cache(maxsize=100)
    def get_photo_info(self, photo_id):
        params = {'photo_id': photo_id}
        info = self._make_request('flickr.photos.getInfo', **params)
        
        # Get EXIF data
        exif = self._make_request('flickr.photos.getExif',
                                photo_id=photo_id).get('photo', {})
        
        # Combine info with EXIF data
        info['photo']['exif'] = exif.get('exif', [])
        return info

    @lru_cache(maxsize=1)
    def get_geotagged_photos(self):
        params = {
            'user_id': self.user_id,
            'has_geo': 1,
            'extras': 'geo,url_sq,url_m',
            'per_page': 500
        }
        return self._make_request('flickr.photos.search', **params)
