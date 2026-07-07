# NICAI Architecture Walkthrough

# Purpose

This document provides a complete technical overview of the NICAI backend architecture. It is intended for the final technical handover so that incoming developers can understand, operate, maintain, validate, and extend the system independently.

---

# System Overview

NICAI (Networked Intelligence & Context Analysis Interface) is a deterministic intelligence platform built using FastAPI. The system processes structured environmental datasets, validates incoming signals, generates explainable intelligence, performs runtime orchestration, and provides traceable outputs for downstream consumers.

The platform is designed as a decision-support system. It does not execute autonomous decisions but instead produces structured intelligence outputs that can be consumed by other systems.

---

# High-Level Architecture

```
Environmental Datasets
        │
        ▼
Samachar Input Adapter
        │
        ▼
Signal Conversion
        │
        ▼
Validation Layer
        │
        ▼
Sanskar Intelligence Engine
        │
        ▼
Pattern Analysis
        │
        ▼
Contract Validation
        │
        ▼
Action Routing
        │
        ▼
Dashboard & API Responses
        │
        ▼
Runtime Logging
        │
        ▼
Replay Engine
```

---

# Architecture Components

## 1. Data Sources

Purpose:

Provide the raw environmental information used by NICAI.

Current datasets:

- clean_weather.csv
- clean_aqi.csv

Typical information includes:

- Temperature
- AQI
- Timestamp
- Latitude
- Longitude
- Location

These datasets simulate real-world environmental observations and are used as the initial input for the intelligence pipeline.

---

## 2. Samachar Input Adapter

Primary File:

samachar_input_adapter.py

Purpose:

Convert raw dataset records into standardized NICAI signals.

Responsibilities:

- Read dataset records
- Normalize input structure
- Generate signal objects
- Attach metadata
- Prepare data for validation

Output:

A standardized signal ready for processing by the validation layer.

---

## 3. Signal Conversion

Purpose:

Transform incoming data into the internal signal format used across the system.

Typical signal fields:

- signal_id
- timestamp
- location
- value
- dataset_id
- trace_id (generated during validation)

This standardization ensures that every downstream module works with a consistent schema.

---

## 4. Validation Layer

Primary File:

validator.py

Purpose:

Validate incoming signals before intelligence processing.

Responsibilities:

- Required field validation
- Data type validation
- Dataset validation
- Confidence calculation
- Validation status assignment
- Trace generation

Possible outputs:

- VALID
- FLAG
- REJECT
- ERROR

Only valid signals continue through the runtime pipeline.

---

## 5. Sanskar Intelligence Engine

Primary File:

sanskar_engine.py

Purpose:

Generate deterministic intelligence from validated signals.

Responsibilities:

- Risk assessment
- Anomaly detection
- Risk classification
- Confidence scoring
- Recommendation generation
- Explainable output generation

Possible risk levels:

- LOW
- MEDIUM
- HIGH

The engine is rule-based and deterministic, ensuring identical outputs for identical inputs.

---

## 6. Pattern Analysis

Primary File:

cluster_intelligence.py

Purpose:

Identify relationships across multiple validated signals.

Responsibilities:

- Detect repeated anomalies
- Identify clusters
- Trend analysis
- Aggregate anomaly information
- Produce higher-level intelligence summaries

Pattern analysis supplements single-signal intelligence without altering individual signal outcomes.

---

## 7. Contract Validation

Primary File:

contract_validator.py

Purpose:

Ensure all generated outputs conform to the expected API and consumer schemas.

Responsibilities:

- Schema validation
- Required field verification
- Response consistency
- Consumer compatibility checks

This layer protects downstream systems from malformed outputs.

---

## 8. Action Routing

Primary File:

action_router.py

Purpose:

Generate structured action recommendations.

Responsibilities:

- Route intelligence outcomes
- Create recommendation payloads
- Preserve trace information
- Record action events

Important:

NICAI only generates action recommendations.

It never executes external actions.

---

## 9. Dashboard

Primary Endpoint:

GET /dashboard

Purpose:

Provide a visual representation of runtime intelligence.

Displays:

- Signal counts
- Risk distribution
- Pattern summaries
- Runtime statistics
- Trace information
- Action summaries

The dashboard is intended for monitoring and demonstration purposes.

---

## 10. Runtime Logging

Purpose:

Maintain a complete audit trail of system execution.

Log files include:

- validation_logs.json
- anomaly_logs.json
- pattern_logs.json
- contract_logs.json
- action_logs.json
- tantra_logs.json
- ttg_logs.json

Logs support:

- Debugging
- Traceability
- Replay
- Operational auditing

---

## 11. Replay Engine

Primary File:

replay_engine.py

Purpose:

Reconstruct historical execution using recorded runtime logs.

Capabilities:

- JSONL support
- Legacy JSON support
- Trace reconstruction
- Stage verification
- Ordered replay validation

Replay helps verify deterministic behaviour and investigate historical executions.

---

# Runtime Flow

The runtime pipeline follows the sequence below:

```
Dataset
    │
    ▼
Samachar Input Adapter
    │
    ▼
Signal Conversion
    │
    ▼
Validation
    │
    ▼
Intelligence Engine
    │
    ▼
Pattern Analysis
    │
    ▼
Contract Validation
    │
    ▼
Action Routing
    │
    ▼
Dashboard
    │
    ▼
Runtime Logging
    │
    ▼
Replay
```

Each module performs a dedicated responsibility and passes structured outputs to the next stage.

---

# Architecture Principles

The NICAI backend is designed around the following engineering principles:

### Deterministic Execution

Identical inputs always produce identical outputs.

---

### Explainable Intelligence

Every intelligence output includes an explanation describing why the result was generated.

---

### Trace Continuity

A unique `trace_id` is propagated across the complete execution pipeline, enabling end-to-end traceability.

---

### Replay Capability

Historical executions can be reconstructed using runtime logs for validation and debugging.

---

### Modular Design

Each module has a clearly defined responsibility, reducing coupling and simplifying maintenance.

---

### Bounded Ownership

NICAI owns:

- Validation
- Intelligence generation
- Runtime orchestration
- Replay
- Dashboard
- Documentation

NICAI does not own:

- External governance systems
- Production acceptance
- Independent testing
- External ecosystem services

---

# Final Architecture Assessment

The current architecture satisfies the objectives of:

- Deterministic intelligence generation
- Explainable decision support
- Production-ready runtime execution
- Replay validation
- Traceable execution
- Modular maintainability
- Technical handover readiness