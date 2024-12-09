# FastAPI Mini Boilerplate with Basic Auth

Welcome to the FastAPI Mini Boilerplate! This project provides a simple yet powerful backend setup using FastAPI, complete with basic authentication features. Whether you're building a new application or looking to learn more about FastAPI, this boilerplate is a great starting point.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLite**: Lightweight, disk-based database with minimal setup.
- **Authentication**: Basic user authentication with hashed passwords and JWT tokens.
- **User Management**: Create, read, update, and delete users.
- **Environment Configuration**: Easy configuration using `.env` files.

## Getting Started

### Prerequisites

- Python 3.7+
- SQLite

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/fastapi-mini-boilerplate.git
    cd fastapi-mini-boilerplate
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python database/setupdb.py
    ```

5. **Create a `.env` file**:
    ```sh
    echo "SALT=your_secret_salt" > .env
    ```

### Running the Application

1. **Start the FastAPI server**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the interactive API documentation.

## API Endpoints

- **Sign Up**: `POST /signup` - Create a new user.
- **Login**: `POST /token` - Authenticate and receive a JWT token.
- **Get Current User**: `GET /users/me` - Retrieve the authenticated user's details.
- **Delete User**: `GET /users/me/signoff` - Delete the authenticated user.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

---

Happy coding! 🚀