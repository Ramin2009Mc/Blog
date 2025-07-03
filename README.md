# ramin.me(blog)

A minimalist personal website for publishing my articles and thoughts. Built with Django and Python, this site is a space for sharing ideas, reflections, and personal projects.

## Features
- Clean, distraction-free design
- Responsive layout for all devices
- Articles and thoughts published in a simple format

---

## Technical Details
- Built with Django 5.1 and Python 3.13
- Uses Whitenoise for static file serving (`STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`)
- Environment variables are loaded via python-dotenv (`.env` file)
- All settings are in `blog/settings.py`
- Articles are implemented as a separate Django app (`article`)
- Templates and static files are organized inside the app
- On mobile devices, the site is blocked with a special message (see CSS and base.html)
- Minimalist design, custom styles, favicon support

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Ramin2009Mc/Blog.git
   cd ramin.me
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add variables:
   ```env
   SECRET_KEY=your_secret_key
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```

The site will be available at http://127.0.0.1:8000/

---

Created by Ramin Kiyamov  
📧 Email: raminkiyamov@gmail.com
