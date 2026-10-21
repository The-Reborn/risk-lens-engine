# 🛡️ RiskLens: Automated Insurance Risk & Portfolio Analytics Engine

> A production-grade backend platform designed for processing, analyzing, and storing large-scale insurance portfolio datasets asynchronously. Built to showcase robust software engineering practices, asynchronous processing pipelines, and data analytics.

---

## 🏗️ Architecture & Data Flow

RiskLens uses an asynchronous message-driven architecture to ensure high availability and non-blocking API performance during heavy data processing.

```text
[ Client / API Request ] 
          │
          ▼
   ( Flask REST API ) ──> Publishes Task ──> [ RabbitMQ (Message Broker) ]
          │                                            │
Returns 202 Accepted                                   ▼
          │                                [ Celery Background Worker ]
          │                                            │
          │                                Runs Pandas & NumPy Analytics
          │                                            │
          ▼                                            ▼
   [ MongoDB Database ] <────────────────── Saves Structured JSON Report
          │
          ▼
[ Client GET /reports ] ──> Fetches Historical Portfolio Analytics
```


## 🛠️ Tech Stack

- Core Language: Python 3.12
- Web Framework: Flask (Application Factory Pattern)
- Asynchronous Processing: Celery with RabbitMQ (Message Broker)
- Database & Persistence: MongoDB (via PyMongo)
- Data Processing & Analytics: Pandas & NumPy
- Testing & Quality Assurance: PyTest
- CI/CD & DevOps: GitHub Actions & Docker Compose


## 📁 Project Structure


risk-lens-engine/
├── .github/
│   └── workflows/
│       └── ci.yml          # Automated CI/CD pipeline running pytest
├── app/
│   ├── api/                # Flask Blueprints & REST endpoints
│   ├── models/             # Database schemas and interactions
│   ├── services/           # Pandas/NumPy data cleaning & analytics logic
│   ├── tasks/              # Celery background job definitions
│   └── __init__.py         # Flask Application Factory & DB connection
├── data/
│   └── insurance_data.xlsx # Kaggle-sourced portfolio dataset
├── tests/                  # PyTest unit test suite
├── docker-compose.yml      # Local container setup for MongoDB and RabbitMQ
├── requirements.txt        # Project dependencies
├── run.py                  # Application entry point
└── README.md



## 🚀 Getting Started Locally

Prerequisites

- Python 3.12+ installed on your machine.
- Docker & Docker Compose installed (for MongoDB and RabbitMQ).


1. Clone the Repository & Setup Environment

    ```bash
    git clone [https://github.com/your-username/risk-lens-engine.git](https://github.com/The-Reborn/risk-lens-engine.git)
    cd risk-lens-engine


    # Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt
    ```

2. Start Infrastructure (Docker Compose)

    Spin up MongoDB and RabbitMQ in the background:

        ```bash
        docker compose up -d
        ```

3. Run the Application

    You will need two terminal windows (both with your virtual environment activated):

        Terminal 1: Start the Flask Web Server

            ```bash
            python run.py
            ```

        Terminal 2: Start the Celery Worker

            ```bash
            celery -A app.tasks.celery_app.celery_app worker --loglevel=info
            ```

## 🧪 Usage & API Endpoints

You can interact with the API using curl or Postman:

1. Check System Health:

    ```bash
    curl http://localhost:5000/api/v1/health
    ```

2. Trigger Asynchronous Risk Analysis:
    (Offloads the Pandas processing job to RabbitMQ and Celery)

    ```bash
    curl -X POST http://localhost:5000/api/v1/analyze
    ```

3. Fetch Processed Reports from MongoDB:

    ```bash
    curl http://localhost:5000/api/v1/reports
    ```

## 🧪 Running Automated Tests

Run the test suit locally using pytest:

    ```bash
    pytest -v
    ```

## 📄 License

Distributed under the MIT License. See LICENSE for more information.