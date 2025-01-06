import os
import logging
from flask import Flask, render_template, jsonify, request
from config import Config
from flickr_client import FlickrClient


# region Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
# endregion

# region Initialize Flickr client
flickr = FlickrClient(
    api_key=os.getenv("FLICKR_API_KEY"),
    secret=os.getenv("FLICKR_SECRET"),
    user_id=os.getenv("FLICKR_USER_ID"),
)
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
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", app.config["MAX_PHOTOS"], type=int)
        popular = request.args.get("popular", app.config["PHOTO_FILTERS"]["popular"])
        tags = request.args.get("tags", app.config["PHOTO_FILTERS"]["tags"])
        album_id = request.args.get("album_id", app.config["PHOTO_FILTERS"]["album_id"])
        search_query = request.args.get("search")
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
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 100, type=int)

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
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", app.config["MAX_PHOTOS"], type=int)
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
    app.run(host="0.0.0.0", port=5000, debug=True)
