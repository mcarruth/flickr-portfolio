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
def index():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", app.config["MAX_PHOTOS"], type=int)
        tags = request.args.get("tags", app.config["PHOTO_FILTERS"]["tags"])
        album_id = request.args.get("album_id", app.config["PHOTO_FILTERS"]["album_id"])
        search_query = request.args.get("search")
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_photos(
            page=page,
            per_page=per_page,
            tags=tags,
            album_id=album_id,
            search_query=search_query,
        )

        if debug:
            return jsonify(data)
        return render_template("photos.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching photos: {e}")
        return render_template("error.html", message="Unable to load photos"), 500


@app.route("/albums")
def albums():
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


@app.route("/tags")
def tags():
    try:
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_tags()

        if debug:
            return jsonify(data)
        return render_template("tags.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching tags: {e}")
        return render_template("error.html", message="Unable to load tags"), 500


@app.route("/map")
def map():
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


@app.route("/about")
def about():
    try:
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_profile()

        if debug:
            return jsonify(data)
        return render_template("about.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching about: {e}")
        return render_template("error.html", message="Unable to load about"), 500


@app.route("/exif/<photo_id>")
def exif(photo_id):
    try:
        debug = request.args.get("debug", "false").lower() == "true"

        data = flickr.get_exif(photo_id)

        if debug:
            return jsonify(data)
        return render_template("exif.html", data=data)
    except Exception as e:
        logger.error(f"Error fetching photo: {e}")
        return render_template("error.html", message="Unable to load photo"), 500


# endregion

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
