# Backend — Project Athena

The backend of **Project Athena** provides the API and application logic for the Memory-Aware Retrieval-Augmented Generation (RAG) system for personalized PCOS lifestyle recommendations.

It is built with FastAPI and Python, with PostgreSQL for persistent application data, SQLAlchemy for database operations, and Alembic for database schema migrations.

## Tech Stack

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| Python       | Backend programming language              |
| FastAPI      | REST API development                      |
| Pydantic     | Request validation and data serialization |
| SQLAlchemy 2 | ORM and database operations               |
| PostgreSQL   | Persistent relational data storage        |
| Alembic      | Database schema migrations                |
| Uvicorn      | ASGI server                               |
| Pytest       | Automated testing                         |

Redis, vector search, embedding generation, and LLM orchestration are part of the planned architecture and will be documented here as they are integrated.

## Backend Architecture

The backend follows a modular structure that separates API endpoints, business logic, database operations, validation schemas, and application configuration.

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       └── users.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── database.py
│   │   └── base.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   └── services/
├── migrations/
├── tests/
├── alembic.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

_The tree illustrates the intended organization. File names may differ slightly depending on the current implementation._

### Component Responsibilities

- **`main.py`** — Initializes the FastAPI application and registers the API router.
- **`api/`** — Defines HTTP endpoints and handles incoming requests.
- **`core/`** — Manages application configuration and environment settings.
- **`db/`** — Provides database connectivity, session management, and the ORM base.
- **`models/`** — Defines SQLAlchemy models representing database entities.
- **`schemas/`** — Defines Pydantic schemas for request validation and response serialization.
- **`services/`** — Contains reusable business logic and database operations.
- **`migrations/`** — Stores Alembic database migration scripts.
- **`tests/`** — Contains automated backend tests.

Models and schemas serve different purposes: models represent persisted database entities, while schemas define the data accepted and returned by the API.

## Prerequisites

Before setting up the backend, install:

- Python version supported by the project's dependencies.
- PostgreSQL.
- Git.
- A code editor such as Visual Studio Code.

Ensure PostgreSQL is running and that a development database and database user have been configured.

## Local Setup

### 1. Navigate to the Backend Directory

```bash
cd backend
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it using the appropriate command.

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```bat
.venv\Scripts\activate.bat
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Use the project's `requirements.txt` as the source of truth for dependencies.

### 4. Configure Environment Variables

Create or update the `.env` file using the variable names expected by the backend configuration.

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=athena_dev
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
```

Replace the example values with your local PostgreSQL configuration. Never commit real credentials or production secrets to version control.

### 5. Initialize the Database Schema

The backend uses SQLAlchemy models and Alembic to manage database schema changes.

If Alembic is already initialized and the migration scripts are available, apply the existing migrations:

```bash
alembic upgrade head
```

If you are setting up a fresh development environment, follow the database initialization instructions in the root README and the existing migration history. Do not create a second Alembic configuration or duplicate migration history.

## Running the Backend

Start the FastAPI development server from the `backend/` directory:

```bash
uvicorn app.main:app --reload
```

This command assumes that `app/main.py` exposes the FastAPI application as `app`.

The default local addresses are:

- **API base URL:** http://127.0.0.1:8000
- **Interactive API documentation:** http://127.0.0.1:8000/docs
- **Alternative API documentation:** http://127.0.0.1:8000/redoc

The API documentation lists the endpoints registered in the running application.

## Database and Migrations

PostgreSQL is used for persistent relational data. SQLAlchemy manages database operations, while Alembic tracks schema changes over time.

After modifying SQLAlchemy models, generate a migration when the change requires a database schema update:

```bash
alembic revision --autogenerate -m "describe schema change"
```

Review the generated migration before applying it:

```bash
alembic upgrade head
```

For more information about database creation, initialization, and schema management, refer to the database setup section in the root README.

## API Testing

The backend is designed to support automated tests using Pytest.

Run the test suite from the `backend/` directory:

```bash
pytest
```

Tests may require a configured test database or other test-specific environment variables. Use isolated test resources rather than running destructive tests against development or production data.

## Development Guidelines

- Use a virtual environment for Python dependencies.
- Keep secrets in environment variables rather than source code.
- Add new database schema changes through migrations.
- Separate database models, API schemas, endpoints, and business logic.
- Add automated tests for new API and service functionality.
- Keep generated files, caches, virtual environments, and local configuration out of Git.
- Update this README when setup commands, dependencies, or architecture change.

## Scope and Safety

The backend is being developed for personalized, evidence-informed PCOS lifestyle guidance. It is not intended to diagnose PCOS, generate diagnostic risk scores, or prescribe medication.

Medical knowledge retrieval, persistent memory, and LLM response generation must be integrated and evaluated before the complete system can be considered operational.
