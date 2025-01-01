import logging
from flask import Flask, render_template, jsonify, request
from config import Config
from flickr_client import FlickrClient

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flickr client
flickr = FlickrClient(
    api_key=app.config["FLICKR_API_KEY"],
    secret=app.config["FLICKR_SECRET"],
    user_id=app.config["FLICKR_USER_ID"],
)


@app.context_processor
def inject_portfolio_title():
    return {"portfolio_title": app.config["PORTFOLIO_TITLE"]}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/photos")
def get_photos():
    page = request.args.get("page", 1, type=int)
    per_page = min(100, request.args.get("per_page", 50, type=int))

    # Get filters from configuration
    tags = app.config["PHOTO_FILTERS"]["tags"]
    album_ids = app.config["PHOTO_FILTERS"]["album_ids"]

    try:
        all_photos = []

        # Get photos for each album ID if specified
        if album_ids and album_ids[0]:  # Check if there are any non-empty album IDs
            for album_id in album_ids:
                photos = flickr.get_photos(
                    page=page, per_page=per_page, album_id=album_id
                )
                if "photos" in photos and "photo" in photos["photos"]:
                    all_photos.extend(photos["photos"]["photo"])

        # Get photos with tags if specified
        if tags and tags[0]:  # Check if there are any non-empty tags
            photos = flickr.get_photos(page=page, per_page=per_page, tags=tags)
            if "photos" in photos and "photo" in photos["photos"]:
                all_photos.extend(photos["photos"]["photo"])

        # If no filters are set, get all public photos
        if not (tags and tags[0]) and not (album_ids and album_ids[0]):
            photos = flickr.get_photos(page=page, per_page=per_page)
            if "photos" in photos and "photo" in photos["photos"]:
                all_photos.extend(photos["photos"]["photo"])

        # Sort photos by date taken (most recent first)
        all_photos.sort(key=lambda x: x.get("datetaken", ""), reverse=True)

        # Limit the number of photos to prevent memory issues
        all_photos = all_photos[: app.config["MAX_PHOTOS"]]

        return jsonify({"photos": {"photo": all_photos}})
    except Exception as e:
        logger.error(f"Error fetching photos: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/photo/<photo_id>")
def photo_detail(photo_id):
    try:
        photo = flickr.get_photo_info(photo_id)
        return render_template("photo_detail.html", photo=photo)
    except Exception as e:
        logger.error(f"Error fetching photo details: {str(e)}")
        return render_template("photo_detail.html", error=str(e))


@app.route("/photo/<photo_id>/info")
def photo_info(photo_id):
    try:
        photo = flickr.get_photo_info(photo_id)
        return jsonify(photo["photo"])
    except Exception as e:
        logger.error(f"Error fetching photo info: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
