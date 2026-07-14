# ENDPOINT_HANDOVER.md

# NICAI Integration Endpoint Handover

## Purpose

This document describes the integration-ready API endpoints exposed by the NICAI backend for frontend integration, testing, deployment validation, and technical handover.

These endpoints provide a stable interface for future integration while preserving the existing backend architecture.

---

# Backend Information

Service Name:
NICAI Intelligence Engine

Framework:
FastAPI

Base URL (Production)

https://nicai-intelligence-engine-3.onrender.com

Local Development

http://127.0.0.1:8000

---

# Endpoint Summary

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | / | Backend landing page |
| GET | /health | Health and deployment verification |
| POST | /nicai/evaluate | Signal evaluation and intelligence generation |
| POST | /contract/validate | Validate NICAI output contract |
| POST | /cluster/analyze | Multi-signal cluster intelligence |
| GET | /trace/{trace_id} | Replay verification |
| POST | /action | Action routing |
| GET | /dashboard | Runtime dashboard |
| GET | /run | End-to-end orchestration pipeline |

---

# 1. GET /

Purpose

Returns the backend landing page and confirms the application is running.

Example Response

HTML page displaying:

NICAI Running

---

# 2. GET /health

Purpose

Returns backend health information.

Used for

- Deployment verification
- Render monitoring
- Integration checks
- Operational readiness

Example Response

```json
{
  "status": "healthy",
  "service": "NICAI Intelligence Engine",
  "version": "1.0.0",
  "timestamp": "2026-07-14T09:30:00Z"
}
```

---

# 3. POST /nicai/evaluate

Purpose

Evaluates incoming signals through the NICAI intelligence pipeline.

Pipeline

Validation

↓

Intelligence Engine

↓

Pattern Analysis

Request

List of signals.

Response

Validated intelligence output together with pattern analysis.

Primary Consumer

Frontend / Runtime Processing

---

# 4. POST /contract/validate

Purpose

Validates whether an intelligence output conforms to the NICAI output contract.

Validation Includes

- Required fields
- Enumerated values
- Confidence range
- Output schema

Example Response

```json
{
  "trace_id": "TRACE_TEST",
  "contract_status": "VALID",
  "errors": []
}
```

Primary Consumer

Frontend

Testing

Integration

---

# 5. POST /cluster/analyze

Purpose

Performs cluster-level intelligence using multiple processed signals.

Capabilities

- Cluster risk assessment
- Composite environmental detection
- Multi-region analysis
- Recommendation generation

Example Response

```json
{
  "trace_id": "TRACE_001",
  "risk_level": "HIGH",
  "recommendation_signal": "requires_review"
}
```

Primary Consumer

Frontend

Testing

Analytics

---

# 6. GET /trace/{trace_id}

Purpose

Performs replay verification for a specific trace.

Capabilities

- Trace lookup
- Replay validation
- Stage verification
- Ordered replay confirmation

Example Response

```json
{
  "trace_id": "TRACE_001",
  "replay_status": "COMPLETE"
}
```

Primary Consumer

Testing

Governance

Audit

---

# 7. POST /action

Purpose

Maps validated intelligence into operational recommendations.

Examples

- CONTINUE_MONITORING
- RECOMMEND_ENVIRONMENTAL_REVIEW
- RECOMMEND_ESCALATION_REVIEW

Primary Consumer

Runtime

Dashboard

---

# 8. GET /dashboard

Purpose

Displays the NICAI operational dashboard.

Displays

- Signals
- Validation status
- Risk level
- Recommendations
- Pattern summary

Primary Consumer

Operators

Demonstrations

---

# 9. GET /run

Purpose

Executes the complete deterministic orchestration pipeline.

Execution Flow

Signal

↓

Validation

↓

Intelligence

↓

Cluster Analysis

↓

Contract Validation

↓

Action Routing

↓

TANTRA Participation

↓

TTG Consume

Primary Consumer

Testing

Integration

End-to-End Validation

---

# Integration Notes

The following endpoints were added to support future integration and technical handover:

- GET /health
- GET /trace/{trace_id}
- POST /contract/validate
- POST /cluster/analyze

These endpoints expose existing backend capabilities without modifying the core runtime architecture.

---

# Handover Notes

These APIs are intended for integration by the frontend and testing teams.

The backend architecture remains deterministic, traceable, and replay-compatible.

Future integrations should consume these endpoints rather than directly invoking backend modules.

---

# Status

Integration Endpoints

Completed

Documentation

Completed

Testing

Completed

Ready for Technical Handover

Yes

Ready for Audit

Yes