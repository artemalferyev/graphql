# FastAPI & GraphQL API

This project is a simple FastAPI application integrated with Strawberry GraphQL. It includes a SQLite in-memory database and allows querying and mutating user data through GraphQL endpoints. The repository also includes automated tests and a Docker setup.

## Features
- **FastAPI** as the backend framework
- **Strawberry GraphQL** for query and mutation handling
- **SQLAlchemy** for database management
- **SQLite (in-memory)** as the database
- **Docker support** for containerization
- **Automated testing** using `pytest`

## Installation

### Prerequisites
- Python 3.10+
- pip
- Docker (optional, for containerized execution)

### Setup & Running Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   uvicorn GraphQL:app --host 0.0.0.0 --port 8000
   ```

## API Usage

### Accessing GraphQL Playground
Once the server is running, open your browser and navigate to:
```
http://127.0.0.1:8000/graphql
```

### Example Queries
#### Fetch Users
```graphql
query {
    users {
        id
        name
        email
    }
}
```
#### Add a New User
```graphql
mutation {
    addUser(name: "John Doe", email: "john@example.com") {
        id
        name
        email
    }
}
```

## Running Tests
To run the test suite, execute:
```sh
pytest
```

## Docker Setup
To build and run the application using Docker:
1. Build the Docker image:
   ```sh
   docker build -t fastapi-graphql-app .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 fastapi-graphql-app
   ```

##   License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

