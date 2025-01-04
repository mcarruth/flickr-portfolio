import os


class Config:

    # General settings
    PORTFOLIO_TITLE = ""  # Change this to your desired title
    COPYRIGHT_TEXT = ""  # Change this to your desired copyright
    MAX_PHOTOS = 500  # Maximum number of photos to display
    CACHE_TIMEOUT = 3600  # Cache timeout in seconds (1 hour)
    SITE_THEME = "dark"  # Options: light, dark, primary, secondary, success, danger, warning, info
    ENABLE_SEARCH = True  # Enable search functionality

    # Photo filters
    # Note: You can filter photos by multiple tags (OR'd together)
    # or album ID, but not both.  Tags will take priority over album ID.
    PHOTO_FILTERS = {
        "tags": "",  # Filter photos by tags (comma-separated list)
        "album_id": "",  # Filter photos by album ID
    }

    # Navigation bar links
    NAVBAR_LINKS = [
        {"name": "Photos", "url": "/photos", "visible": True},
        {"name": "Albums", "url": "/albums", "visible": True},
        {"name": "Map", "url": "/map", "visible": True},
    ]

    # Social media links
    SOCIAL_LINKS = [
        {
            "name": "Twitter",
            "url": "https://twitter.com",
            "icon": "fab fa-twitter",
            "visible": True,
        },
        {
            "name": "Facebook",
            "url": "https://facebook.com",
            "icon": "fab fa-facebook",
            "visible": True,
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com",
            "icon": "fab fa-instagram",
            "visible": True,
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com",
            "icon": "fab fa-linkedin",
            "visible": True,
        },
    ]
