import os

class Config:

    # Portfolio configuration
    PORTFOLIO_TITLE = 'Your Portfolio Name'  # Change this to your desired title
    MAX_PHOTOS = 500  # Maximum number of photos to display
    CACHE_TIMEOUT = 3600  # Cache timeout in seconds (1 hour)

    # Photo filtering configuration
    PHOTO_FILTERS = {
        'tags': [],        # Optional: Add specific tags to filter photos
        'album_ids': [],   # Optional: Add specific album IDs to show
    }
