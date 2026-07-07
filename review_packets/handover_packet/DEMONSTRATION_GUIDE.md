# NICAI Live Integration Demonstration Guide

## Objective

Demonstrate the integrated NICAI backend operating as a deterministic production-ready system.

---

## Demonstration Scope

The demonstration includes:

- Backend startup
- Frontend integration
- API execution
- Runtime execution
- Dashboard
- Replay validation
- Trace continuity
- Contract validation
- Deployment overview

---

## Prerequisites

- Python environment configured
- Dependencies installed
- Runtime logs available
- Local backend operational
- Production deployment available

---

## Local Execution

Start the backend:

```bash
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/dashboard

Production:

- Backend
- Frontend

---

## Demonstration Goal

Demonstrate deterministic execution from signal ingestion to intelligence output while preserving trace continuity.