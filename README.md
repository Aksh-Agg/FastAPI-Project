# FastAPI Project

## Overview

This project is a web application built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. The application includes user authentication, CRUD operations for posts, and voting functionality.

## Features

- User authentication (login)
- CRUD operations for posts
- Voting on posts
- JWT token-based authentication
- SQLAlchemy ORM for database interactions
- Pydantic for data validation
- CORS middleware for handling cross-origin requests

## Project Structure

- **app/**: The main application directory.
  - **__init__.py**: Initializes the app package.
  - **main.py**: The entry point of the application. It initializes the FastAPI app and includes the routers.
  - **config.py**: Contains configuration settings for the application, such as database connection details and secret keys.
  - **database.py**: Sets up the database connection and session.
  - **models.py**: Defines the database models using SQLAlchemy.
  - **schema.py**: Defines the Pydantic models for request and response validation.
  - **oauth2.py**: Handles JWT token creation and verification.
  - **routers/**: Contains the route handlers for different parts of the application.
    - **__init__.py**: Initializes the routers package.
    - **posts.py**: Contains the route handlers for post-related operations.
    - **users.py**: Contains the route handlers for user-related operations.
    - **auth.py**: Contains the route handlers for authentication.
    - **votes.py**: Contains the route handlers for voting on posts.
- **.env**: Environment variables file (not included in the repository).
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: The documentation file for the project.

  ## Setup the environment variable
  Create a .env file in the root directory and add the following variables:

- DATABASE_HOSTNAME=localhost
- DATABASE_PORT=5432
- DATABASE_PASSWORD=yourpassword
- DATABASE_NAME=yourdatabase
- DATABASE_USERNAME=yourusername
- SECRET_KEY=your_secret_key
- ALGORITHM=HS256
- ACCESS_TOKEN_EXPIRE_MINUTES=30
