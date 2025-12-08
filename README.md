# Portfolio

A minimalist two-person portfolio Django web application showcasing professional profiles with separate bio and about sections.

## Features

- Clean, minimalist design
- Two featured professionals with customizable profiles
- Separate bio (short) and about (detailed) sections
- Contact links and website URLs
- Responsive layout (mobile-friendly)
- Projects section for each person

## Project Structure

```
myproject/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
├── README.md
├── myproject/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── myapp/                  # Main app
    ├── models.py           # Person model
    ├── views.py            # Index and detail views
    ├── urls.py             # URL routing
    ├── admin.py
    ├── migrations/
    └── templates/
        └── myapp/
            ├── index.html  # Portfolio listing
            └── detail.html # Person detail page
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd myproject
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser to `http://127.0.0.1:8000/`

## Editing Content

### Add/Edit Person Entries

Use the Django shell to add or modify people:

```bash
python manage.py shell
>>> from myapp.models import Person
>>> p = Person.objects.get(pk=1)
>>> p.bio = "Your new bio"
>>> p.about = "Your detailed about section"
>>> p.save()
>>> exit()
```

Or delete the database and let the app recreate sample data:

```bash
# Delete db.sqlite3, then restart the server
python manage.py runserver
```

### Customize Person Model

Edit `myapp/models.py` to add fields like:
- Photo/image field
- Skills or expertise
- Social media links
- Location

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Styling

CSS is embedded in the templates for simplicity:
- `myapp/templates/myapp/index.html` — portfolio listing styles
- `myapp/templates/myapp/detail.html` — detail page styles

To move CSS to external files:
1. Create `myapp/static/myapp/style.css`
2. Move CSS from templates
3. Add `{% load static %}` and reference with `<link rel="stylesheet" href="{% static 'myapp/style.css' %}">`

## Deployment

For production:

1. Update `DEBUG = False` in `myproject/settings.py`
2. Set `ALLOWED_HOSTS` to your domain
3. Use a production database (PostgreSQL recommended)
4. Collect static files: `python manage.py collectstatic`
5. Use a WSGI server like Gunicorn or uWSGI

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

## Technologies

- Python 3.8+
- Django 5.2
- HTML5 & CSS3

## License

MIT or your preferred license

## Author

Censon & Johann Marqueta
