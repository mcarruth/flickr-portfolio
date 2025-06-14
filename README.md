# Flickr Portfolio

Flickr Portfolio is a web application designed to showcase your Flickr photos in an elegant, mobile-friendly portfolio. It syncs with your Flickr account, displaying your recent photos, albums, and geotagged images on your hosted site. Flickr portfolio allows professional photographers and hobbyists to host their own custom portfolio site while still using Flickr as their online storage solution.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Recent Photos**: Automatically display up to 500 of your most recent public photos.
- **Albums**: Browse and view your Flickr albums.
- **Search**: Find photos by title, description, or tags.
- **Geotagging**: Explore your geotagged photos on an interactive map.
- **Photo Details**: View detailed photo information, including EXIF data and statistics.
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices.

---

### Screenshots
![Homepage](/images/home.png)
![Album View](/images/albums.png)
![Map View](/images/map.png)
![Photo Detail](/images/photo.png)

---

## Installation

To run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/mcarruth/flickr-portfolio.git
   cd flickr-portfolio
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables and customize the site (see [Configuration](#configuration)).

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`.

For deployment instructions, see the [Configuration](#configuration) section.

---

## Configuration

1. **Flickr API**
    - Get your API key and secret from [Flickr API Manager](https://www.flickr.com/services/apps/create/apply/).
    - Set your Flickr API key, secret, and user id in the following environment variables.
     ```bash
     export FLICKR_API_KEY=your_api_key
     export FLICKR_SECRET=your_api_secret
     export FLICKR_USER_ID=your_user_id
     ```

2. **Configure Site Settings (Optional)**
    - Edit `config.py` to customize the app.

3. **Upload Site icons (Optional)**
    - Create your site icons.
    ```bash
    static/android-chrome-192x192.png
    static/android-chrome-512x512.png
    static/apple-touch-icon.png
    static/favicon-16x16.png
    static/favicon-32x32.png
    static/favicon.ico
    static/site.webmanifest
    ```

4. **Deployment**
    - Deploy to your hosting provider. Ensure your environment variables are set during deployment.

---

## Usage

- **Search**: Use the search bar to find photos by title, description, or tags.
- **Albums**: Navigate to the Albums section to explore and view individual albums.
- **Geotagged Photos**: View your geotagged photos on the interactive map.
- **Details**: Click on a photo to see its statistics, EXIF data, and other details.

---

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **APIs**: Flickr API, Map API

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For feedback or support, contact:
- **GitHub**: [mcarruth](https://github.com/mcarruth)

---

## Acknowledgments

- [Flickr API](https://www.flickr.com/services/api/)
- [Bootstrap Framework](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/)
- [MDBootstrap](https://mdbootstrap.com/)
- [Leaflet](https://leafletjs.com/)

---

Feel free to customize this template further based on your preferences or the specifics of your project.
