# LibraryProject

LibraryProject is a Django-based web application for managing a library system. It allows users to add, view, and delete books, manage user profiles, and handle permissions for different user roles.

## Features

- User authentication and custom user model
- Add, view, and delete books
- Custom permissions (`can_create`, `can_delete`)
- Admin interface for managing users and books

## Requirements

- Python 3.8+
- Django 4.x

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd LibraryProject
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate
   ```
3. **Install the requirements:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser (admin account):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Visit the `/admin` URL to access the Django admin interface.
- Use the superuser account to log in and manage users and books.
- Regular users can register, log in, and manage their profiles.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
