# Deployment Procedure

# Purpose

This document describes the complete deployment process for the NICAI backend and frontend. It serves as the operational guide for future maintainers responsible for deploying, validating, and updating the system.

---

# Deployment Architecture

NICAI consists of two primary deployment components:

Frontend (Vercel)

↓

Backend API (Render)

↓

Runtime Processing

↓

Dashboard

↓

Logging

↓

Replay Support

---

# Deployment Components

## Backend

Platform:

Render

Technology:

- FastAPI
- Uvicorn

Responsibilities:

- Signal validation
- Intelligence generation
- Dashboard serving
- Runtime execution
- Replay support
- API services

Current Production URL:

https://nicai-intelligence-engine-3.onrender.com

---

## Frontend

Platform:

Vercel

Responsibilities:

- Dashboard interface
- User interaction
- API consumption

Current Production URL:

https://nicai-frontend-8wut.vercel.app

---

# Local Deployment

## Requirements

- Python 3.11+
- Git
- pip
- Virtual environment (recommended)

---

## Clone Repository

```bash
git clone <repository_url>

cd nicai-validation-layer
```

---

## Install Dependencies

```bash
pip install -r requirements-prod.txt
```

---

## Start Application

```bash
uvicorn main:app --reload
```

Default URL

```
http://127.0.0.1:8000
```

---

# API Verification

After startup verify:

GET /

GET /docs

GET /dashboard

GET /run

POST /nicai/evaluate

POST /action

All endpoints should respond successfully.

---

# Production Validation

After deployment verify:

- Backend accessible
- Dashboard accessible
- Swagger available
- Runtime operational
- Replay functional
- Logs generated

---

# Health Validation

Current Observation

The application does not expose a dedicated `/health` endpoint.

Health verification is performed using:

- API availability
- Runtime execution
- Dashboard functionality

This behavior is documented and should not be interpreted as a deployment failure.

---

# Deployment Checklist

Before deployment:

- Repository up to date
- Dependencies installed
- Build verification completed
- Runtime verification completed

After deployment:

- APIs validated
- Dashboard verified
- Runtime logs generated
- Replay validation completed

---

# Rollback Strategy

If deployment fails:

1. Restore previous working build.
2. Validate application startup.
3. Re-run API verification.
4. Confirm dashboard functionality.
5. Review runtime logs.

---

# Final Assessment

The deployment process supports both local development and production hosting while preserving deterministic runtime behavior and operational stability.