import os

class Config:
    # Flask configuration
    SECRET_KEY = 'your-secret-key-here'  # Change this to a random secret key

    # Portfolio configuration
    PORTFOLIO_TITLE = 'Your Portfolio Name'  # Change this to your desired title
    MAX_PHOTOS = 500  # Maximum number of photos to display
    CACHE_TIMEOUT = 3600  # Cache timeout in seconds (1 hour)

    # Flickr API configuration
    FLICKR_API_KEY = 'your-flickr-api-key'  # Required
    FLICKR_USER_ID = 'your-flickr-user-id'  # Required
    FLICKR_SECRET = 'your-flickr-secret'    # Required

    # Photo filtering configuration
    PHOTO_FILTERS = {
        'tags': [],        # Optional: Add specific tags to filter photos
        'album_ids': [],   # Optional: Add specific album IDs to show
    }
