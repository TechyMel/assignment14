# Final Project - FastAPI Calculations Application

## Overview

This project is a full-stack calculator web application built with FastAPI, SQLAlchemy, PostgreSQL, Docker, and Jinja2 templates. Users can register, log in with JWT authentication, perform calculations, and manage their calculation history.

For the final project, a new **Exponentiation** calculation feature was added. Users can calculate powers (e.g., 2^3 = 8), save the result, and manage it using the application's BREAD (Browse, Read, Edit, Add, Delete) functionality.

---

## Features

- User Registration
- User Login (JWT Authentication)
- Password Hashing
- Calculation History
- BREAD Functionality
  - Browse Calculations
  - Read Calculation
  - Add Calculation
  - Edit Calculation
  - Delete Calculation
- Supported Operations
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - **Exponentiation (New Feature)**

---

## Technologies Used

- Python 3.10
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- Jinja2 Templates
- Pytest
- Playwright
- GitHub Actions

---

# Running the Application

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/final_project.git
cd final_project
```

Build and start the containers

```bash
docker compose up --build -d
```

Open the application

```
http://localhost:8000
```

Stop the application

```bash
docker compose down
```

---

# Running Tests

Run all tests

```bash
docker compose exec web pytest --no-cov
```

Run only unit tests

```bash
docker compose exec web pytest tests/unit --no-cov
```

Run only integration tests

```bash
docker compose exec web pytest tests/integration --no-cov
```

Run only E2E tests

```bash
docker compose exec web pytest tests/e2e --no-cov
```

---

# Docker Hub

Docker Image

```
https://hub.docker.com/r/YOUR_DOCKER_USERNAME/final_project
```

Pull the image

```bash
docker pull YOUR_DOCKER_USERNAME/final_project:latest
```

Run the image

```bash
docker run -p 8000:8000 YOUR_DOCKER_USERNAME/final_project:latest
```

---

# GitHub Repository

```
https://github.com/YOUR_USERNAME/final_project
```

---

# Project Structure

```
app/
├── auth/
├── core/
├── models/
├── operations/
├── schemas/
├── templates/
├── static/
└── main.py

tests/
├── unit/
├── integration/
└── e2e/
```

---

# Testing Summary

The application includes:

- Unit tests for calculation logic
- Integration tests for API endpoints and database interactions
- End-to-End tests for authentication and application workflows
- GitHub Actions CI pipeline for automated testing

---

# Final Project Feature

The new feature implemented for the final project is **Exponentiation**.

Users can:

- Select Exponentiation from the calculator.
- Enter two numbers.
- Calculate powers (example: 2^3 = 8).
- Save the calculation.
- View saved calculations.
- Edit calculations.
- Delete calculations.

The feature is integrated with the existing authentication system, database, user interface, and automated tests.

---

## Author

Melvina Temu

Business Information Systems

New Jersey Institute of Technology
## Docker link
https://hub.docker.com/repository/docker/lilmel/final_project/general 