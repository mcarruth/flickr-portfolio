# Deploying Flickr Portfolio to Render.com

This guide walks you through deploying flickr-portfolio to Render's free tier with automatic deploys from GitHub.

## Prerequisites

- GitHub account with flickr-portfolio repository pushed
- Render.com account (free) - sign up at https://render.com
- Flickr API credentials:
  - API Key
  - API Secret
  - Get them at https://www.flickr.com/services/apps/create/apply/
- Your Flickr User ID - look it up at https://www.webfx.com/tools/idgettr/

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

Make sure all files including `render.yaml` are committed and pushed to your GitHub repository.

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main  # or master, depending on your branch
```

### 2. Sign Up for Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with your GitHub account (recommended for easier integration)

### 3. Create a New Web Service

1. From the Render dashboard, click "New +" → "Web Service"
2. Click "Connect" next to your GitHub account if not already connected
3. Find and select your `flickr-portfolio` repository
4. Render will detect the `render.yaml` file automatically

### 4. Configure the Service

Render should auto-populate these from `render.yaml`:

- **Name**: `flickr-portfolio` (or change to `portfolio-demo`, etc.)
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT main:app`
- **Plan**: Free

### 5. Add Environment Variables

Click "Advanced" to add environment variables:

**Required:**
- `FLICKR_API_KEY` = `your_flickr_api_key`
- `FLICKR_SECRET` = `your_flickr_api_secret`
- `FLICKR_USER_ID` = `your_flickr_user_id` (e.g., `95137114@N00`)

**Optional (already set in render.yaml):**
- `FLASK_DEBUG` = `False` (NEVER set to True in production)
- `LOG_LEVEL` = `INFO` (or DEBUG, WARNING, ERROR)

Click "Create Web Service"

### 6. Wait for Deployment

Render will:
1. Pull your code from GitHub
2. Install Python dependencies (takes 1-3 minutes)
3. Start Gunicorn server
4. Deploy to a public URL like `https://flickr-portfolio.onrender.com`

Watch the deployment logs in real-time.

### 7. Set Up Custom Domain (Optional)

Once deployed successfully:

1. Go to your service settings
2. Click "Custom Domain"
3. Add your subdomain: `portfolio.mikecarruth.org`
4. Render will provide DNS instructions:
   - Add a CNAME record in your domain registrar:
     - Name: `portfolio`
     - Value: `flickr-portfolio.onrender.com` (or whatever Render provides)
5. SSL certificate is automatically provisioned (free via Let's Encrypt)

### 8. Enable Auto-Deploy

By default, Render auto-deploys when you push to your main branch:

1. Go to Settings → Build & Deploy
2. Ensure "Auto-Deploy" is set to "Yes"
3. Select your main branch (usually `main` or `master`)

Now every `git push` will trigger a new deployment!

## Deployment Architecture

```
GitHub (main/master branch)
    ↓ (auto-deploy on push)
Render.com
    ↓ (builds Python environment)
Gunicorn (4 workers) + Flask
    ↓ (serves on dynamic port)
https://portfolio.mikecarruth.org
```

## Free Tier Limitations

Render's free tier includes:

- ✅ 750 hours/month (enough for 24/7 uptime)
- ✅ Automatic SSL certificates
- ✅ Custom domains
- ✅ Auto-deploy from GitHub
- ⚠️ Spins down after 15 minutes of inactivity (cold starts take ~30 seconds)
- ⚠️ 512MB RAM limit

The spin-down means the first visitor after inactivity will wait ~30 seconds for the service to wake up.

## Performance Notes

### Gunicorn Configuration

The default configuration uses 4 workers:
```bash
gunicorn -w 4 -b 0.0.0.0:$PORT main:app
```

On the free tier (512MB RAM), you might want to reduce this to 2 workers if you encounter memory issues:
```bash
gunicorn -w 2 -b 0.0.0.0:$PORT main:app
```

Edit the `startCommand` in `render.yaml` if needed.

### Cold Start Optimization

To minimize cold start impact:
- Consider using a simple uptime monitoring service (like UptimeRobot) to ping your site every 10 minutes
- Or upgrade to paid tier ($7/month) for always-on service

## Troubleshooting

### Build Fails

Check the logs in Render dashboard. Common issues:
- Missing dependencies in `requirements.txt`
- Python version mismatch
- Syntax errors in code

### Container Starts But Shows Error

- Check environment variables are set correctly
- Verify FLICKR_API_KEY and FLICKR_SECRET are valid
- Ensure FLICKR_USER_ID is correct
- Look at application logs in Render dashboard

### Photos Not Loading

- Verify your Flickr photos are public
- Check Flickr API credentials have proper permissions
- Look at browser console for errors
- Check Render logs for API errors

### Out of Memory Errors

Free tier has 512MB RAM limit. To reduce memory:
- Reduce Gunicorn workers from 4 to 2
- Check for memory leaks in your code

### Service Keeps Spinning Down

This is normal on free tier. Options:
- Use an uptime monitor to keep it alive
- Upgrade to paid tier ($7/month) for always-on

## Monitoring & Debugging

From the Render dashboard you can:
- **View Logs**: Real-time application logs
- **Metrics**: CPU and memory usage
- **Shell Access**: SSH into the container for debugging
- **Deploy History**: Rollback to previous versions

### Viewing Logs

```bash
# From Render dashboard > Logs tab
# Or via Render CLI:
render logs -s flickr-portfolio
```

## Updating Your Deployment

Just push changes to GitHub:

```bash
git add .
git commit -m "Update portfolio styling"
git push origin main
```

Render automatically rebuilds and deploys within 1-3 minutes.

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `FLICKR_API_KEY` | ✅ Yes | - | Your Flickr API key |
| `FLICKR_SECRET` | ✅ Yes | - | Your Flickr API secret |
| `FLICKR_USER_ID` | ✅ Yes | - | Your Flickr user ID |
| `FLASK_DEBUG` | ❌ No | `False` | Debug mode (NEVER True in production) |
| `LOG_LEVEL` | ❌ No | `INFO` | Logging level (DEBUG/INFO/WARNING/ERROR) |

## Cost

- **Free tier**: $0/month (with spin-down after 15 min inactivity)
- **Starter tier**: $7/month (always-on, no spin-down, more resources)

## Security Best Practices

✅ **DO:**
- Keep `FLASK_DEBUG=False` in production
- Use environment variables for all secrets
- Monitor logs for suspicious activity
- Keep dependencies updated

❌ **DON'T:**
- Never commit `.env` file to git
- Never expose API secrets in client-side code
- Don't use weak API credentials

## Next Steps

Once flickr-portfolio is deployed:

1. Test all features:
   - Homepage photo grid
   - Albums view
   - Map view (geotagged photos)
   - Individual photo pages
   - Search functionality

2. Update your README.md with the live demo URL

3. Share your portfolio with the world!

## Support

Questions? Contact mikecarruth@gmail.com or open an issue on GitHub.

## Additional Resources

- [Render Python Deployment Guide](https://render.com/docs/deploy-flask)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Flask Production Deployment](https://flask.palletsprojects.com/en/stable/deploying/)
