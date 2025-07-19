# LibraryProject

LibraryProject is a Django-based web application designed to help you manage a library system. It allows users to add, view, update, and delete books, authors, and other library resources.

## Features

- User authentication (login, logout, registration)
- Manage books and authors
- Search and filter library resources
- Responsive web interface

## Requirements

- Python 3.8+
- Django 4.x

## Setup Instructions

1. **Clone the repository:**

git clone <repository-url> cd LibraryProject

python -m venv venv venv\Scripts\activate

pip install django

python manage.py migrate

2. **Create a superuser:**

```bash
python manage.py createsuperuser
```
3. **Run the development server:**

```bash
python manage.py runserver
```
4. **Access the application:**
Open your web browser and go to `http://127.0.0.1:8000/`
5. **Admin Interface:**
Access the admin interface at `http://127.0.0.1:8000/admin/`