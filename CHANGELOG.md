# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-01-06

### Added
- `.gitignore` file for Python projects with comprehensive exclusions
- `.env.example` file as a template for environment variables
- Environment variable validation on application startup
- Type hints throughout `flickr_client.py` for improved code safety
- Request timeout protection (10 seconds) for all Flickr API calls
- Input validation and sanitization for all route parameters
- Configurable logging level via `LOG_LEVEL` environment variable
- Configurable Flask host and port via environment variables
- `static/` directory with README for site icons
- Security features section in README
- Troubleshooting section in README
- Contributing guidelines in README
- Improved deployment instructions with popular hosting options

### Changed
- Updated `main.py` to use python-dotenv for environment variable management
- Improved logging configuration with formatted output
- Refactored debug and host settings to use environment variables
- Enhanced error handling with specific timeout exceptions
- Updated `error.html` template to extend `base.html` for consistency
- Improved README with detailed installation, configuration, and deployment instructions
- Limited search query length to 200 characters to prevent abuse
- Added reasonable limits to pagination parameters (max page: 1000, max per_page: 500)
- Updated `config.py` with better documentation and docstrings
- Social media links now default to `visible: False` until configured

### Security
- **CRITICAL**: Changed default `FLASK_DEBUG` from `True` to `False`
- **CRITICAL**: Changed default host from `0.0.0.0` to `127.0.0.1` for local development
- Added environment variable validation to prevent running without required credentials
- Removed `@lru_cache` decorators that could cause issues with security updates
- Added request timeouts to prevent hanging connections
- Added input validation to prevent excessive API calls

### Dependencies
- Added `python-dotenv==1.0.1` for environment variable management

## Notes

This update focuses on security hardening, code modernization, and improved documentation. The application now follows security best practices and provides a better developer experience.
