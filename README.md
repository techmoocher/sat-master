# SAT Master

A comprehensive web application for SAT preparation, providing resources, practice problems, and study plans for students.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository or download the project files

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   If requirements.txt doesn't exist, install Flask:
   ```
   pip install flask
   ```

### Launching the Website

1. Navigate to the project directory:
   ```
   cd "c:\Users\ndvph\OneDrive\Desktop\Programming\Personal Projects\SAT-Master"
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your web browser and go to:
   - Local access: http://127.0.0.1:5000 or http://localhost:5000
   - Network access: http://{your-ip-address}:5000

The website will be available and the Flask development server will automatically reload when you make changes to the code.

## Project Structure

- `app.py` - Flask application entry point
- `templates/` - HTML templates
  - `base.html` - Base template with universal settings
  - `index.html` - Homepage template
  - Other page templates
- `static/` - Static files
  - `css/` - CSS stylesheets
  - `js/` - JavaScript files
  - `images/` - Image resources

## Development

The Flask application is set to run in debug mode, which provides:
- Automatic reloading when code changes
- Detailed error messages
- Debug console for errors

To deploy in a production environment, set `debug=False` and use a production WSGI server like Gunicorn or uWSGI.
