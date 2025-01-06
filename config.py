"""
flickr-portfolio/config.py

All user site customizations and configurations should be defined here.
Note: These are all optional and can be left as-is.

IMPORTANT:
- Do not expose sensitive keys in public repositories.
- Refer to the README or documentation for further guidance.
"""


class Config:

    # -------------------------------------------------------------------
    # General Settings
    # -------------------------------------------------------------------

    PORTFOLIO_TITLE = ""  # Used on every page and as the page title ex. MICHAEL CARRUTH
    COPYRIGHT_TEXT = ""  # Included in the footer ex. © Michael Carruth
    SITE_THEME = "dark"  # Options: light, dark, primary, secondary, success, danger, warning, info
    ENABLE_SEARCH = True  # False will hide the site search box

    # -------------------------------------------------------------------
    # Photo Settings
    # -------------------------------------------------------------------

    PHOTO_FILTERS = {
        "popular": True,  # Show popular photos on home page
        "tags": "",  # Show photos with specific tags on home page ex. "trains, planes, automobiles"
        "album_id": "",  # Show photos from a specific album ex. "72157601424097768"
        # Note: Only one of the above filters can be active at a time.  They are listed in order of priority.
    }

    # -------------------------------------------------------------------
    # Navigation Settings
    # -------------------------------------------------------------------

    NAVBAR_LINKS = [
        {
            "name": "Photos",
            "url": "/photos",
            "visible": True,  # Set visible to False to hide
        },
        {
            "name": "Albums",
            "url": "/albums",
            "visible": True,  # Set visible to False to hide
        },
        {"name": "Map", "url": "/map", "visible": True},  # Set visible to False to hide
    ]

    # -------------------------------------------------------------------
    # Social Media Links Settings
    # -------------------------------------------------------------------

    SOCIAL_LINKS = [
        {
            "name": "Twitter",
            "url": "https://twitter.com",  # Update with your Twitter URL
            "icon": "fab fa-twitter",
            "visible": True,  # Set visible to False to hide
        },
        {
            "name": "Facebook",
            "url": "https://facebook.com",  # Update with your Facebook URL
            "icon": "fab fa-facebook",
            "visible": True,  # Set visible to False to hide
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com",  #
            "icon": "fab fa-instagram",
            "visible": True,  # Set visible to False to hide
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com",  # Update with your LinkedIn URL
            "icon": "fab fa-linkedin",
            "visible": True,  # Set visible to False to hide
        },
    ]

    # -------------------------------------------------------------------
    # Flickr API Settings
    # -------------------------------------------------------------------

    MAX_PHOTOS = 500  # Maximum number of photos to display
    CACHE_TIMEOUT = 3600  # Cache timeout in seconds (1 hour)
