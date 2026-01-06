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

### Prerequisites

- Python 3.8 or higher
- Flickr API credentials ([Get them here](https://www.flickr.com/services/apps/create/apply/))

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mcarruth/flickr-portfolio.git
   cd flickr-portfolio
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Flickr API credentials
   ```

5. **Customize the site (optional):**
   - Edit `config.py` to customize appearance and behavior
   - Add site icons to the `static/` directory (see `static/README.md`)

6. **Run the application:**
   ```bash
   python app.py
   ```

7. **Open your browser:**
   Navigate to `http://localhost:5000`

For deployment instructions, see the [Deployment](#deployment) section.

---

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Required - Get from https://www.flickr.com/services/apps/create/apply/
FLICKR_API_KEY=your_api_key_here
FLICKR_SECRET=your_api_secret_here
FLICKR_USER_ID=your_flickr_user_id_here

# Optional - Flask Configuration
FLASK_DEBUG=False          # Never set to True in production
FLASK_HOST=127.0.0.1       # Use 127.0.0.1 for local only
FLASK_PORT=5000

# Optional - Logging
LOG_LEVEL=INFO             # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

**Finding Your Flickr User ID:**
- Visit [idGettr](https://www.webfx.com/tools/idgettr/) and enter your Flickr URL

### Site Customization

Edit `config.py` to customize:
- **Portfolio title** and copyright text
- **Theme** (light, dark, primary, secondary, etc.)
- **Navigation links** and social media links
- **Photo filters** (tags, albums, popular photos)
- **Search functionality** (enable/disable)

### Site Icons (Optional)

Generate and add icons to the `static/` directory:
- `favicon.ico`
- `favicon-16x16.png` and `favicon-32x32.png`
- `apple-touch-icon.png`
- `android-chrome-192x192.png` and `android-chrome-512x512.png`
- `site.webmanifest`

Use tools like [RealFaviconGenerator](https://realfavicongenerator.net/) or [Favicon.io](https://favicon.io/) to generate these.

### Deployment

For production deployment:

1. **Set environment variables** on your hosting provider
2. **Never enable debug mode** in production (`FLASK_DEBUG=False`)
3. **Use a production WSGI server** like Gunicorn (included in requirements):
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 main:app
   ```
4. **Consider using a reverse proxy** (nginx, Apache) for better performance
5. **Enable HTTPS** for secure communication

**Popular Hosting Options:**
- [Heroku](https://www.heroku.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- [Google Cloud Run](https://cloud.google.com/run)

---

## Usage

- **Search**: Use the search bar to find photos by title, description, or tags.
- **Albums**: Navigate to the Albums section to explore and view individual albums.
- **Geotagged Photos**: View your geotagged photos on the interactive map.
- **Details**: Click on a photo to see its statistics, EXIF data, and other details.

---

## Technologies Used

- **Backend**: Python 3.8+, Flask 3.1.0
- **Frontend**: HTML5, CSS3, MDBootstrap 6.3.1
- **APIs**: Flickr API
- **Mapping**: Leaflet.js 1.9.4 with OpenStreetMap
- **Production Server**: Gunicorn
- **Environment Management**: python-dotenv

## Security Features

- Environment variable validation on startup
- Input sanitization and validation
- Request timeout protection
- Configurable debug mode (disabled by default)
- Secure localhost binding for development
- Type hints for improved code safety
- No hardcoded credentials

---

## Troubleshooting

### Missing Environment Variables
If you see an error about missing environment variables:
1. Ensure your `.env` file exists in the project root
2. Verify all required variables are set (see `.env.example`)
3. Check that variable names match exactly

### Flickr API Errors
- Verify your API credentials are correct
- Check that your Flickr User ID matches your account
- Ensure your API app has the correct permissions

### Port Already in Use
If port 5000 is already in use:
- Change `FLASK_PORT` in your `.env` file to another port (e.g., 5001)
- Or stop the other service using port 5000

### Static Files Not Loading
- Ensure the `static/` directory exists
- Check that favicon files are in the correct location
- Missing favicons will show 404 errors but won't break the app

---

## Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the app locally to test
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

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
