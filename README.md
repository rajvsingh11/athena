# Project Athena

## Personalized PCOS Lifestyle Recommendation system using Memory-aware RAG

- A Conversational AI assistant for women with PCOS thet provides **personalized** lifestyle guidance (Eg. Diet, Exercise, sleep, stress, cycle-aware suggestions) using **Retrieval Augmented Generation**, user memory, ans optionally a PCOS risk/diagnosis module.

## Goals:

1. To provide a solution that offers personalized recommendations instead of just vague LLM responses.
2. Solve the current problem of Hallucination in LLMs.
3. A single checkpoint solution for PCOS diagnoised women.

## Tech Stack:

| Service           | Technology                                |
| ----------------- | ----------------------------------------- |
| Frontend          | `Flutter`                                 |
| Backend           | `Fast API`                                |
| LLM Orchestration | `LangChain`                               |
| Embeddings        | `all-miniLM-L6-v2` or `BAAI/bge-small-en` |
| Vector DB         | `ChromaDB`                                |
| Short Term Memory | `Redis` (Coversational memory)            |
| Long Term Memory  | `PostgreSQL` (User Database)              |
| Autentication     | `Firebase Auth`                           |

## System Architecture

The project follows a modular client-server architecture in which the Flutter frontend communicates with a Python FastAPI backend. The backend manages API requests, application logic, database operations, and the integration of retrieval and memory components.

The system is designed to combine relevant medical knowledge with user-specific context to generate personalized PCOS lifestyle recommendations.

### High-Level Architecture

```text
┌──────────────────────────────┐
│       Flutter Frontend       │
│      (Mobile Application)    │
└──────────────┬───────────────┘
               │ REST API
               ▼
┌──────────────────────────────┐
│       FastAPI Backend        │
│                              │
│  API Layer                   │
│  Business Logic              │
│  RAG Orchestration           │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
┌──────────────┐  ┌────────────────┐
│ Memory Layer │  │ Retrieval Layer│
│              │  │                │
│ Redis        │  │ Embeddings     │
│ PostgreSQL   │  │ Vector Search  │
└──────────────┘  └───────┬────────┘
                          ▼
                 ┌──────────────────┐
                 │ PCOS Knowledge   │
                 │ Base             │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Large Language   │
                 │ Model (LLM)      │
                 └────────┬─────────┘
                          │
                          ▼
                 Personalized Response
```

_Note: This diagram represents the target architecture. Components are integrated progressively as development advances._

## Project Structure

The project is organized into separate frontend and backend components to maintain modularity and simplify development.

### Backend Structure

```text
backend/
├── app/
│   ├── api/             # API routes and endpoints
│   ├── core/            # Configuration and core settings
│   ├── db/              # Database connection and session management
│   ├── models/          # SQLAlchemy database models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── services/        # Business logic and service operations
│   └── main.py          # FastAPI application entry point
├── tests/               # Backend test cases
├── migrations/          # Alembic database migrations
├── alembic.ini          # Alembic configuration
└── requirements.txt     # Python dependencies
```

The Flutter frontend is maintained separately from the backend and communicates with it through REST APIs.

### Responsibilities of Backend Components

- **`api/`** — Defines API endpoints and handles incoming requests.
- **`core/`** — Contains shared configuration and application settings.
- **`db/`** — Manages database connectivity and database sessions.
- **`models/`** — Defines the database entities and their relationships using SQLAlchemy.
- **`schemas/`** — Validates incoming data and defines the structure of API requests and responses using Pydantic.
- **`services/`** — Contains reusable business logic, database operations, and future RAG and memory-related operations.
- **`main.py`** — Initializes the FastAPI application and registers the required routes.

The separation between models and schemas keeps database persistence concerns independent from API validation and serialization.

## Core System Components

### 1. Flutter Frontend

The Flutter application provides the user interface through which users will interact with the system, submit queries, and view personalized lifestyle recommendations.

The frontend communicates with the backend through REST API requests. Processing involving database operations, retrieval, memory management, and LLM orchestration is handled on the backend.

### 2. FastAPI Backend

FastAPI acts as the central application layer. It receives client requests, validates incoming data, coordinates business logic, and communicates with the database and other services.

The modular backend structure is intended to support the gradual integration of the RAG pipeline, memory management, and LLM response generation.

### 3. Memory Management

The proposed system uses two memory layers to support conversational continuity and persistent personalization.

- **Short-term memory — Redis:** Intended to maintain active session context and recent conversational interactions.
- **Long-term memory — PostgreSQL:** Intended to store persistent user information, preferences, goals, and other relevant context across sessions.

Relevant memory will be retrieved according to the current query rather than sending the entire conversation history to the LLM.

### 4. Retrieval-Augmented Generation (RAG)

The RAG component is designed to retrieve relevant information from a curated PCOS knowledge base before generating a response.

The intended workflow includes document processing, text chunking, embedding generation, vector search, and retrieval of relevant evidence. The retrieved information will be combined with the current query and relevant user context to construct the LLM prompt.

### 5. PCOS Knowledge Base

The knowledge base will contain relevant information from research papers, clinical guidelines, and other trusted medical sources concerning PCOS lifestyle management.

Its purpose is to provide an evidence base for recommendations related to nutrition, physical activity, sleep, stress management, and general lifestyle guidance.

### 6. Large Language Model Integration

The LLM will generate natural-language responses using the current user query, relevant retrieved medical evidence, and applicable user memory.

The intended approach separates medical evidence from personalization context: user memory helps tailor the response but does not modify or replace the retrieved medical evidence.

## Request Processing Workflow

The intended request-processing workflow is as follows:

1. The user submits a query through the Flutter application.
2. The FastAPI backend receives and validates the request.
3. Relevant short-term conversational context is retrieved from Redis.
4. Relevant persistent user context is retrieved from PostgreSQL.
5. The query is processed to retrieve relevant information from the PCOS knowledge base.
6. The retrieved evidence and relevant user context are combined into an augmented prompt.
7. The LLM generates a personalized response grounded in the available evidence.
8. The backend returns the response to the Flutter application.
9. Relevant information from the interaction may be stored in long-term memory when appropriate.

This workflow describes the planned end-to-end integration. Individual stages will become operational as the corresponding components are implemented.

## Quick Start

Project Athena consists of a Flutter frontend and a Python FastAPI backend. Follow the steps below to prepare the development environment.

### Prerequisites

- Git
- Python and pip
- Flutter SDK and Dart
- PostgreSQL

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace the placeholders with your repository URL and directory name.

### 2. Set Up the Backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL environment variables and apply the existing database migrations as described in the [Backend README](backend/README.md).

Start the development server:

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the available API endpoints.

<!-- ### 3. Set Up the Frontend

Open a separate terminal and navigate to the Flutter application directory.

```bash
cd <flutter-frontend-directory>
flutter pub get
flutter run
```

Replace the directory placeholder with the actual frontend path in the repository. Configure the frontend's API base URL to point to the running backend, using an address accessible from your emulator or device. -->

### 4. Development Documentation

- [Setup and Development](backend/README.md)
- [Backend and Database Setup](backend/README.md)

**Note:** The backend API and database functionality are being developed incrementally. Redis-based conversational memory, long-term memory workflows, vector retrieval, LLM integration, and full frontend-backend integration should be treated as work in progress until implemented and tested.

## Current Development Status

Development is being carried out incrementally, with the backend foundation established before integrating the complete RAG and memory-aware recommendation pipeline.

| Component                                | Status                            |
| ---------------------------------------- | --------------------------------- |
| Project planning and architecture        | Defined                           |
| Backend project structure                | Established                       |
| FastAPI application                      | Under development                 |
| PostgreSQL integration                   | Under development                 |
| SQLAlchemy ORM models                    | Under development                 |
| Alembic migrations                       | Configured for schema management  |
| API request/response schemas             | Under development                 |
| Redis short-term memory                  | Planned                           |
| Long-term user memory workflow           | Planned for integration           |
| PCOS knowledge base and vector retrieval | Planned for integration           |
| LLM-based response generation            | Planned for integration           |
| Flutter-backend integration              | Pending end-to-end implementation |
| Quantitative evaluation                  | Planned                           |

_Update this table as features are completed and tested._

## Safety and Scope

This project focuses on personalized, evidence-informed PCOS lifestyle guidance. It is not intended to diagnose PCOS, calculate diagnostic risk scores, prescribe medication, or replace professional medical care.

The system is intended to use retrieved medical evidence to support its responses, acknowledge limitations when sufficient evidence is unavailable, and direct users to qualified healthcare professionals when medical evaluation is necessary.

---

## Contact

Developed by **Raj Vardhan Singh**  
📧 Email: srajvardhan11@gmail.com
👥 LinkedIn: [rajvsingh11](https://linkedin.com/in/rajvsingh11)

---

> _"Empowering preventive healthcare through technology."_
