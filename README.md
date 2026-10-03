# jsondemo

Minimal Django project showing three ways to get data from a view into a template.

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Open http://127.0.0.1:8000/ (JSON endpoint: http://127.0.0.1:8000/api/sales/).

Files to read: `dashboard/views.py`, `dashboard/urls.py`, `dashboard/templates/dashboard/index.html`.
