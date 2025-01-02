# Photographer's Portfolio Web Application

A simple, elegant way to showcase your Flickr photos on your own website. This application automatically displays your Flickr photos in a beautiful gallery format, complete with:

- Photo galleries with smooth transitions
- Detailed photo information display
- Location mapping for geotagged photos
- Tag-based organization
- Mobile-friendly design

## What You'll Need

1. A Flickr account with your photos
2. A web hosting account
3. FTP or SSH access to your web hosting (your host will provide this)

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

### 3. Setting Environment Variables

Set the required environment variables for your application:

#### **Locally (For Testing)**

1. Open a terminal in your project directory.
2. Set the variables in your terminal session:
   ```bash
   export FLICKR_API_KEY=your_api_key
   export FLICKR_SECRET=your_api_secret
   export FLICKR_USER_ID=your_user_id
   ```
3. These variables will only persist for the current terminal session. To make them persistent, you can add them to your shell configuration file (e.g., `.bashrc`, `.zshrc`).

#### **On the Server (For Deployment)**

1. Access your server via SSH or your hosting provider's control panel.
2. Set the environment variables in the server's environment configuration.
   - For Linux servers, you can add the variables to the `.bashrc` or `.bash_profile` file for the user running the application:
     ```bash
     export FLICKR_API_KEY=your_api_key
     export FLICKR_SECRET=your_api_secret
     export FLICKR_USER_ID=your_user_id
     ```
   - Alternatively, if your hosting platform allows you to define environment variables via a control panel, add the following:
     ```
     FLICKR_API_KEY    your_api_key
     FLICKR_SECRET     your_api_secret
     FLICKR_USER_ID    your_user_id
     ```
3. Restart your application to ensure the variables are loaded.

---

### 4. Downloading the Code

1. Visit the GitHub repository page.
2. Click the green **"Code"** button.
3. Choose **"Download ZIP"**.
4. Extract the ZIP file on your computer.

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
   - Use an FTP or SSH program (e.g., FileZilla or your terminal) to upload the application files to your web host's directory (e.g., `public_html`).

3. **Install Dependencies on the Server**:
   - If your web host provides SSH access:
     ```bash
     pip install -r requirements.txt --user
     ```

4. **Set Environment Variables on the Server**:
   - Ensure the environment variables for `FLICKR_API_KEY`, `FLICKR_SECRET`, and `FLICKR_USER_ID` are correctly set (as described in Step 3: Setting Environment Variables).

5. **Start the Application**:
   - Follow your hosting provider's instructions for running Python web applications.

6. **Access Your Website**:
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
3. Contact your web hosting provider's support for assistance with FTP or Python configuration.

---

This application creates a professional portfolio website that automatically stays in sync with your Flickr photos. Any new photos you add to Flickr will automatically appear on your website!