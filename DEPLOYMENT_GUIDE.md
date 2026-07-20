# DEPLOYMENT_GUIDE.md

# NICAI Production Deployment Guide

## Purpose

This guide explains how to deploy, validate, maintain, and troubleshoot the NICAI production backend.

---

# 1. Production Deployment

## Backend

https://nicai-intelligence-engine-3.onrender.com

## Frontend

https://nicai-frontend-8wut.vercel.app

## Dashboard

https://nicai-intelligence-engine-3.onrender.com/dashboard

## Swagger API

https://nicai-intelligence-engine-3.onrender.com/docs

Deployment Status:

PASS

---

# 2. Local Deployment

## Install Dependencies

```bash
pip install -r requirements-prod.txt
```

## Start Application

```bash
uvicorn main:app --reload
```

Application starts on:

```
http://127.0.0.1:8000
```

---

# 3. Production Validation

Verify the following:

- Backend responds successfully.
- Dashboard loads.
- Swagger UI is available.
- Runtime execution succeeds.
- Replay validation succeeds.
- Trace continuity preserved.
- API compatibility preserved.

---

# 4. Runtime Validation

Validate endpoints:

| Method | Endpoint |
|---------|----------|
| GET | / |
| GET | /docs |
| GET | /dashboard |
| GET | /run |
| POST | /nicai/evaluate |
| POST | /action |

Expected Result:

HTTP 200 responses for implemented endpoints.

---

# 5. Replay Validation

Replay validation includes:

- JSONL log ingestion
- Replay reconstruction
- Deterministic replay
- Trace continuity

Replay evidence:

review_packets/review_assets/validation_evidence/replay/

---

# 6. Deployment Evidence

Deployment evidence includes:

- Backend screenshots
- Frontend screenshots
- Dashboard screenshots
- API screenshots
- Runtime logs
- Replay validation
- Render deployment logs

Evidence location:

review_packets/review_assets/validation_evidence/

---

# 7. Health Observation

The deployed backend currently does not expose a dedicated `/health` endpoint.

Observed Response:

HTTP 404 Not Found

This behaviour matches the deployed implementation and is documented as an operational observation.

---

# 8. Rollback Procedure

If deployment issues occur:

1. Restore the previous stable deployment.
2. Validate runtime.
3. Validate replay.
4. Validate APIs.
5. Confirm dashboard availability.

---

# 9. Troubleshooting

## API unavailable

Verify:

- Render deployment
- Uvicorn startup
- Dependencies

## Dashboard unavailable

Verify:

- Backend running
- Dashboard route available

## Replay issue

Verify:

- JSONL logs
- Replay engine

## Validation failure

Inspect:

- validator.py
- replay_engine.py
- contract_validator.py

---

# 10. Final Deployment Status

Backend Deployment:

PASS

Runtime Validation:

PASS

Replay Validation:

PASS

API Validation:

PASS

Production Status:

READY FOR FINAL ACCEPTANCE