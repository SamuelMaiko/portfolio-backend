# Portfolio Backend · [![license](https://img.shields.io/github/license/peaceiris/actions-gh-pages.svg)](LICENSE)

This is the backend for my portfolio site, built using **Django** and **Django REST Framework (DRF)**.  
It serves API endpoints for my portfolio during build time.

## Technologies Used

- Django
- Django REST Framework (DRF)
- MySQL.

## Setup & Installation

- Clone the repository and install dependencies:

  ```
  https://github.com/SamuelMaiko/portfolio-backend.git
  ```

- Then navigate to the project directory and create a virtual environment and activate it:

  ```
  cd your-backend-repo
  python -m venv venv
  ```

  - On Windows

    ```
    venv\Scripts\activate
    ```

  - On macOS/Linux

    ```
    source venv/bin/activate
    ```

- Install dependencies

  ```
  pip install -r requirements.txt
  ```

- Apply migrations
  ```
  python manage.py migrate
  ```
- Create a super user
  ```
  python manage.py createsuperuser
  ```
- Run development server

  ```
  python manage.py runserver
  ```

  Then visit: 🔗 http://127.0.0.1:8000

  ## API Endpoints

  | Method | Endpoint                        | Description                                                                         |
  | ------ | ------------------------------- | ----------------------------------------------------------------------------------- |
  | GET    | `/api/portfolio/`               | Fetches all portfolio data such as projects, skills, contact details, education etc |
  | POST   | `/api/contactme/receive-email/` | Receives email from frontend stores it and sends it to owner email                  |

  ⚡ **All these endpoints generate JSON data used by the frontend during build time.**

  ***

## Deployment

This backend is deployed on **[PythonAnywhere](https://www.pythonanywhere.com/)** 🚀

You can access the live API at:  
🔗 https://maikoportfolio.pythonanywhere.com/admin/
