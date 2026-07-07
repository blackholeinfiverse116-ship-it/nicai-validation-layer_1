# Configuration Guide

# Purpose

This document explains the configuration required to build, run, and maintain the NICAI backend.

---

# Development Environment

Recommended:

- Windows / Linux
- Python 3.11+
- Git
- VS Code (recommended)

---

# Dependencies

Primary packages include:

- FastAPI
- Uvicorn
- Pandas
- NumPy

Additional dependencies are listed in:

requirements-prod.txt

---

# Repository Configuration

Key runtime files:

- main.py
- validator.py
- sanskar_engine.py
- action_router.py
- replay_engine.py

---

# Runtime Configuration

The application starts using:

```bash
uvicorn main:app --reload
```

---

# Data Configuration

Primary datasets:

- clean_weather.csv
- clean_aqi.csv

These datasets are processed through:

samachar_input_adapter.py

---

# Logging Configuration

Runtime generates:

- validation_logs.json
- anomaly_logs.json
- action_logs.json
- contract_logs.json
- pattern_logs.json

These logs are required for replay and debugging.

---

# Deployment Configuration

Backend:

Render

Frontend:

Vercel

---

# Configuration Verification

Verify:

- Python version
- Installed dependencies
- Dataset availability
- Runtime logs directory
- Production URLs

---

# Final Assessment

The current configuration is sufficient for local development, production deployment, replay validation, and future maintenance.