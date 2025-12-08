# Portfolio Project

A minimalist Django portfolio for two professionals.

## Quick Start

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## Edit Content

```bash
python manage.py shell
>>> from myapp.models import Person
>>> p = Person.objects.first()
>>> p.bio = "New bio"
>>> p.about = "New about section"
>>> p.save()
```

See README.md for full documentation.
