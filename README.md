# Blog Site

# Project Setup

**1. Clone the repository:**
```bash
git clone https://github.com/gmutafov/Blog-Site.git
```
**2. Open the project**

**3. Install dependencies**
  ```bash
  pip install -r requirements.txt
```
**4. Change DB settings in settings.py**
```bash

     DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "your_db_name",
          "USER": "your_username",
          "PASSWORD": "your_pass",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }
  ```

**5. Run the migration**
 ```bash
  python manage.py migrate
```
**6. Run the project**
  ```bash
  python manage.py runserver
```


# 📖 Overview

The Blog Site is a web application built with Django, allowing users to easily create, manage, and interact with blog posts. This application includes the essential features for a blogging platform such as user registration, post creation, comment functionality, and user interaction through likes.
# 🛠Key Features
- User Accounts:

    - User registration, login, and logout functionality.
    - Profile management.

- Blog Posts:

    - Create, read, update, and delete posts.
    - Rich-text support for blog content.

- Interactions:

    - Add comments to posts.
    - Like or unlike posts.

- Responsive Design:
    - Styled with Bootstrap for a clean and user-friendly interface.


# Additional Information

**🧑‍💻Technologies Used**

- Backend: Django, Python
- Frontend: HTML, Bootstrap
- Database: PostgreSQL
