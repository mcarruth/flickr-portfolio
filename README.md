# Photographer's Portfolio Web Application

A simple, elegant way to showcase your Flickr photos on your own website. This application automatically displays your Flickr photos in a beautiful gallery format, complete with:

- Photo galleries with smooth transitions
- Detailed photo information display
- Location mapping for geotagged photos
- Tag-based organization
- Mobile-friendly design

## What You'll Need

1. A Flickr account with your photos
2. A web hosting account (like GoDaddy, Bluehost, etc.)
3. FTP access to your web hosting (your host will provide this)

## Step-by-Step Setup Guide

### 1. Getting Your Flickr API Keys (One-time setup)

1. Go to [Flickr App Garden](https://www.flickr.com/services/apps/create/)
2. Click "Get an API Key"
3. Choose "Apply for a Non-Commercial Key"
4. Fill in the form:
   - Application Name: Your Portfolio
   - Description: Personal photo portfolio website
5. After approval, you'll receive:
   - API Key
   - API Secret
   Save these somewhere safe!

### 2. Finding Your Flickr User ID

1. Visit [idGettr](https://www.webfx.com/tools/idgettr/)
2. Enter your Flickr username
3. Copy your Flickr ID (it looks like "12345678@N00")

### 3. Setting Up Your Website

1. Download this code:
   - Visit the GitHub repository page
   - Click the green "Code" button
   - Choose "Download ZIP"
   - Extract the ZIP file on your computer

2. Basic Configuration:
   - Find the file named `config.example.py`
   - Make a copy and rename it to `config.py`
   - Open `config.py` in a text editor (like Notepad)
   - Update these settings:
     ```python
     PORTFOLIO_TITLE = 'Your Name Photography'  # Change to your desired title
     FLICKR_API_KEY = 'paste-your-api-key-here'
     FLICKR_USER_ID = 'paste-your-flickr-id-here'
     FLICKR_SECRET = 'paste-your-api-secret-here'
     ```

3. Optional: Filter Which Photos to Display
   - In the same `config.py` file, you can choose to show only specific photos:
     ```python
     PHOTO_FILTERS = {
         'tags': ['wedding', 'portrait'],  # Only show photos with these tags
         'album_ids': ['72157712345678'],  # Only show photos from these albums
     }
     ```
   - To find an album ID:
     1. Open your album on Flickr
     2. Look at the web address, it will look like: flickr.com/photos/username/albums/72157712345678
     3. The last number is your album ID
   - Leave these empty (`[]`) to show all your photos

### 4. Uploading to Your Web Host

1. Open your FTP program (like FileZilla - free download at filezilla-project.org)
2. Connect using the FTP details from your web host
3. Upload all the files to your website's folder (usually called 'public_html' or 'www')
4. Important: Make sure `config.py` contains your correct Flickr information

### 5. Testing Your Site

1. Visit your website's address in a web browser
2. You should see your Flickr photos displayed in a gallery
3. Click on photos to view them larger
4. Try the map view to see where photos were taken

## Need Help?

If you run into any issues:
1. Double-check your Flickr API keys and user ID
2. Make sure all files were uploaded to your web host
3. Contact your web hosting provider's support for help with FTP access

## Requirements for Your Web Host

Your web hosting needs to support:
- Python 3.11 or newer
- The ability to run Python web applications

Most modern web hosts support these requirements. When in doubt, ask your hosting provider if they support Python web applications.

---

Note: This application creates a professional portfolio website that automatically stays in sync with your Flickr photos. Any new photos you add to Flickr will automatically appear on your website!
