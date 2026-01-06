import os
import sys
import logging
from flask import Flask, render_template, jsonify, request
from config import Config
from flickr_client import FlickrClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# region Configure logging
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
# endregion

# region Validate required environment variables
required_env_vars = ["FLICKR_API_KEY", "FLICKR_SECRET", "FLICKR_USER_ID"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
    logger.error("Please set these variables in your .env file or environment")
    logger.error("See .env.example for reference")
    sys.exit(1)
# endregion

# region Initialize Flickr client
flickr = FlickrClient(
    api_key=os.getenv("FLICKR_API_KEY"),
    secret=os.getenv("FLICKR_SECRET"),
    user_id=os.getenv("FLICKR_USER_ID"),
)
logger.info("Flickr client initialized successfully")
# endregion


# region Inject config variables into templates


@app.context_processor
def inject_config():
    return {"config": app.config}


# endregion


# region Routes
@app.route("/")
@app.route("/photos")
def get_photos():
    try:
        # Input validation with reasonable limits
        page = max(1, min(request.args.get("page", 1, type=int), 1000))
        per_page = max(1, min(request.args.get("per_page", app.config["MAX_PHOTOS"], type=int), 500))

        popular_param = request.args.get("popular")
        if popular_param is not None:
            popular = popular_param.lower() == "true"
        else:
            popular = app.config["PHOTO_FILTERS"]["popular"]

        tags = request.args.get("tags", app.config["PHOTO_FILTERS"]["tags"])
        album_id = request.args.get("album_id", app.config["PHOTO_FILTERS"]["album_id"])
        search_query = request.args.get("search", "")

        # Limit search query length
        if search_query and len(search_query) > 200:
            search_query = search_query[:200]

        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_photos(
            page=page,
            per_page=per_page,
            popular=popular,
            tags=tags,
            album_id=album_id,
            search_query=search_query,
        )

        photos = data.get("photos", {}).get("photo", []) or data.get(
            "photoset", {}
        ).get("photo", [])

        if debug:
            return jsonify(photos)
        return render_template("photos.html", photos=photos)
    except Exception as e:
        logger.error(f"Error fetching photos: {e}")
        return render_template("error.html", message="Unable to load photos"), 500


@app.route("/albums")
def get_albums():
    try:
        debug = request.args.get("debug", "false").lower() == "true"
        # Input validation with reasonable limits
        page = max(1, min(request.args.get("page", 1, type=int), 1000))
        per_page = max(1, min(request.args.get("per_page", 100, type=int), 500))

        data = flickr.get_photosets(page=page, per_page=per_page)

        if debug:
            return jsonify(data)
        return render_template("albums.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching albums: {e}")
        return render_template("error.html", message="Unable to load albums"), 500


@app.route("/map")
def get_map():
    try:
        # Input validation with reasonable limits
        page = max(1, min(request.args.get("page", 1, type=int), 1000))
        per_page = max(1, min(request.args.get("per_page", app.config["MAX_PHOTOS"], type=int), 500))
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_photos(page=page, per_page=per_page, has_geo=True)

        if debug:
            return jsonify(data)
        return render_template("map.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching map: {e}")
        return render_template("error.html", message="Unable to load places"), 500


@app.route("/photos/<photo_id>")
def get_photo_by_id(photo_id):
    try:
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_photo(photo_id=photo_id)

        if debug:
            return jsonify(data)
        return render_template("photo.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching photo: {e}")
        return render_template("error.html", message="Unable to load photo"), 500


# endregion

if __name__ == "__main__":
    # Use environment variables for configuration
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))

    if debug_mode:
        logger.warning("Running in DEBUG mode - do not use in production!")

    app.run(host=host, port=port, debug=debug_mode)
