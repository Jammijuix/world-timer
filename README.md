# Timezone Web Application

This is a Django web application that helps users find their country's official name, continent, timezone, and current local time. It was recently upgraded from a series of basic terminal scripts to a fully functional web interface.

## How it works

The application presents a web form that accepts three inputs:
- First Name
- Country
- Present City

Upon submission, it processes the information and displays the exact timezone and the current time for the provided location.

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## How to Run Locally

1. **Clone the repository** (if you haven't already).
2. **Navigate to the root directory**.
3. **Install the required dependencies**:
   ```bash
   pip install django pycountry pycountry-convert pytz
   ```
   *(Alternatively, if you use a virtual environment, activate it before installing).*
4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
6. **Access the application**: Open your web browser and go to `http://127.0.0.1:8000/`.

## Running Tests

To ensure the application is functioning correctly, you can run the test suite:
```bash
python manage.py test
```

## Limitations
While the web app improves upon the original scripts, matching a city to a specific timezone still relies on a best-effort string match against the `pytz` country timezones list. If a city isn't found exactly, it defaults to the primary timezone for the country.
