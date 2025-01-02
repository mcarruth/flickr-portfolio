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

---

## Step-by-Step Setup Guide

### 1. Getting Your Flickr API Keys (One-Time Setup)

1. Go to [Flickr App Garden](https://www.flickr.com/services/apps/create/).
2. Click **"Get an API Key"**.
3. Choose **"Apply for a Non-Commercial Key"**.
4. Fill in the form:
   - **Application Name**: Your Portfolio
   - **Description**: Personal photo portfolio website
5. After approval, you'll receive:
   - **API Key**
   - **API Secret**

Save these somewhere safe!

---

### 2. Finding Your Flickr User ID

1. Visit [idGettr](https://www.webfx.com/tools/idgettr/).
2. Enter your Flickr username.
3. Copy your Flickr ID (it looks like `12345678@N00`).

---

### 3. Downloading the Code

1. Visit the GitHub repository page.
2. Click the green **"Code"** button.
3. Choose **"Download ZIP"**.
4. Extract the ZIP file on your computer.

---

### 4. Setting Up Your Environment Variables

1. **Locate the `example.env` File**:
   - In the downloaded project folder, locate the file named `example.env`.

2. **Create Your `.env` File**:
   - Make a copy of `example.env` and rename it to `.env`.

3. **Update the `.env` File**:
   - Open `.env` in a text editor and replace the placeholder values with your Flickr API details:
     ```plaintext
     FLICKR_API_KEY=your_api_key
     FLICKR_SECRET=your_api_secret
     FLICKR_USER_ID=your_user_id
     ```

---

### 5. Setting Up Your Website

1. **Basic Configuration**:
   - Find the file named `example.config.py`.
   - Make a copy and rename it to `config.py`.
   - Open `config.py` in a text editor (like Notepad).
   - Update these settings:
     ```python
     PORTFOLIO_TITLE = 'Your Name Photography'  # Change to your desired title
     ```

2. **Optional: Filter Which Photos to Display**:
   - In the same `config.py` file, you can filter displayed photos:
     ```python
     PHOTO_FILTERS = {
         'tags': ['wedding', 'portrait'],  # Only show photos with these tags
         'album_ids': ['72157712345678'],  # Only show photos from these albums
     }
     ```
   - To find an album ID:
     1. Open your album on Flickr.
     2. Look at the web address: `flickr.com/photos/username/albums/72157712345678`.
     3. The last number is your album ID.

   - Leave these fields empty (`[]`) to show all your public photos.

---

### 6. Running the Application

#### **Option 1: Run Locally for Testing**

1. **Install Python**:
   - Ensure Python 3.11 or newer is installed. Download it from [python.org](https://www.python.org/).

2. **Install Dependencies**:
   - Open a terminal in the project directory.
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
     Activate the virtual environment:
     - On Windows:
       ```cmd
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

     Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   - Start the application:
     ```bash
     python app.py
     ```
   - Open a web browser and visit `http://127.0.0.1:5000`.

#### **Option 2: Deploy to a Web Host**

1. **Check Hosting Requirements**:
   - Ensure your hosting provider supports Python 3.11 or newer.

2. **Upload Your Files**:
   - Use an FTP program (e.g., FileZilla) to upload the application files to your web host's directory (e.g., `public_html`).

3. **Install Dependencies on the Server**:
   - If your web host provides SSH access:
     ```bash
     pip install -r requirements.txt --user
     ```

4. **Start the Application**:
   - Follow your hosting provider's instructions for running Python web applications.

5. **Access Your Website**:
   - Visit your domain (e.g., `https://yourdomain.com`) to see your live portfolio.

---

## Requirements for Your Web Host

Your web hosting needs to support:
- Python 3.11 or newer
- The ability to run Python web applications

---

## Need Help?

If you run into any issues:
1. Double-check your Flickr API keys and user ID.
2. Ensure all files were uploaded to your web host.
3. Contact your web hosting provider's support for assistance with FTP access or Python configuration.

---

This application creates a professional portfolio website that automatically stays in sync with your Flickr photos. Any new photos you add to Flickr will automatically appear on your website!
