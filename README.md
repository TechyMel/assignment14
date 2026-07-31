# Assignment 14 – Complete BREAD Functionality for Calculations

## Overview

This project extends the JWT-authenticated Calculations API by implementing full BREAD (Browse, Read, Edit, Add, Delete) functionality for calculations. Users can register, log in, create calculations, view calculation history, update existing calculations, and delete calculations through both the REST API and the front-end interface.

## Features

- User registration and login with JWT authentication
- Password hashing using bcrypt
- Browse all calculations for the logged-in user
- Read individual calculation details
- Add new calculations
- Edit existing calculations
- Delete calculations
- PostgreSQL database with SQLAlchemy ORM
- Pydantic validation
- Docker and Docker Compose support
- Automated testing with pytest
- GitHub Actions CI/CD pipeline
- Docker Hub deployment

---

## Technologies Used

- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Docker
- Docker Compose
- pytest
- GitHub Actions

---

## Running the Application

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### Build and start the containers

```bash
docker compose up --build
```

The application will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## Running Tests

Run all tests inside the Docker container:

```bash
docker compose exec web pytest --no-cov
```

Expected result:

```
99 passed, 1 skipped
```

---

## Manual Testing

1. Open

```
http://localhost:8000
```

2. Register a new user.

3. Log in.

4. Create a calculation.

5. Verify that the calculation appears in the calculation history.

6. Click **View** to display the calculation details.

7. Click **Edit** to modify the calculation.

8. Click **Delete** to remove the calculation.

---

## Docker Hub

Docker Hub Repository:

```
https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/assignment14
```

---

## GitHub Repository

```
https://github.com/YOUR_USERNAME/YOUR_REPO
```

---

## Project Structure

```
app/
├── auth/
├── core/
├── models/
├── schemas/
├── templates/
├── static/
├── main.py

tests/
├── unit/
├── integration/
└── e2e/
```

---

## BREAD Operations

| Operation | Endpoint |
|-----------|----------|
| Browse | GET /calculations |
| Read | GET /calculations/{id} |
| Add | POST /calculations |
| Edit | PUT /calculations/{id} |
| Delete | DELETE /calculations/{id} |

---

## CI/CD

GitHub Actions automatically:

- Runs pytest
- Builds the Docker image
- Pushes the image to Docker Hub after all tests pass

---

## Author

Melvina Temu

Business Information Systems

New Jersey Institute of Technology

## Docker link
https://hub.docker.com/repository/docker/lilmel/601_module14/general 