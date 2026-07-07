# Troubleshooting Guide

# Purpose

Provide guidance for diagnosing and resolving common operational issues.

---

# Build Issues

## Symptom

Application does not start.

## Resolution

- Verify Python version.
- Install dependencies.
- Execute build verification.
- Review import errors.

---

# Runtime Issues

## Symptom

Application starts but APIs fail.

## Resolution

- Verify Uvicorn startup.
- Review runtime logs.
- Check traceback output.
- Validate datasets.

---

# Dashboard Issues

## Symptom

Dashboard unavailable.

## Resolution

- Verify backend running.
- Check /dashboard endpoint.
- Refresh browser.
- Review browser console.

---

# Replay Issues

## Symptom

Replay reports incomplete stages.

## Resolution

- Verify runtime logs exist.
- Confirm selected trace ID.
- Review replay summary.

Replay completeness depends on available runtime logs.

---

# API Issues

## Symptom

Unexpected API response.

## Resolution

- Validate request payload.
- Review Swagger.
- Check validator output.
- Review runtime logs.

---

# Deployment Issues

## Symptom

Production unavailable.

## Resolution

- Verify Render deployment.
- Verify Vercel deployment.
- Confirm backend URL.
- Confirm frontend URL.

---

# Logging Issues

## Symptom

Missing runtime logs.

## Resolution

- Verify logs directory.
- Execute runtime again.
- Check write permissions.

---

# Escalation

Only investigate verified issues supported by runtime evidence.