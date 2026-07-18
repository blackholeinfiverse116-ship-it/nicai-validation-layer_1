# DEFECT_REGISTER

## Repository
NICAI Validation Layer Repository

## Auditor
Ankita Prajapati

## Audit Date
18 July 2026

---

# Purpose

This document records all defects identified during the independent engineering audit of the NICAI repository.

Only reproducible issues observed during validation are included.

No implementation changes were made during the audit.

---

# Defect Summary

| ID | Severity | Status | Area |
|----|----------|--------|------|
| DEF-001 | Medium | Open | Deployment |
| DEF-002 | Low | Open | Backend Routing |

---

# DEF-001

## Title

Render deployment fails due to platform-specific dependency.

### Severity

Medium

### Status

Open

### Area

Deployment

### Description

The application could not be deployed successfully on Render because the project dependencies include the Windows-only package `pywinpty`.

This package is incompatible with Linux deployment environments.

### Expected Behaviour

The application should install all dependencies successfully and complete deployment on the target platform.

### Actual Behaviour

Deployment terminated during dependency installation while processing the `pywinpty` package.

The application failed to build.

### Steps to Reproduce

1. Push the repository to GitHub.
2. Create a new Render Web Service.
3. Configure:
   - Build Command:
     `pip install -r requirements.txt`
   - Start Command:
     `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Start deployment.
5. Observe the build logs.

### Evidence

Render build logs reported an installation failure while generating metadata for the `pywinpty` package.

### Impact

Cloud deployment cannot be completed until the dependency is made compatible with the deployment environment.

### Recommendation

Review project dependencies and ensure only platform-compatible packages are included for production deployment.

---

# DEF-002

## Title

Backend root endpoint returns HTTP 404.

### Severity

Low

### Status

Open

### Area

Backend Routing

### Description

Accessing the backend root URL directly returns an HTTP 404 Not Found response.

### Expected Behaviour

The root endpoint should either provide a health/status response or be documented as intentionally unavailable.

### Actual Behaviour

The backend returned:

```json
{
  "detail": "Not Found"
}
```

### Steps to Reproduce

1. Start the backend server.
2. Open the backend base URL in a browser.
3. Observe the response.

### Evidence

HTTP response:

```json
{
  "detail": "Not Found"
}
```

Swagger documentation and other API endpoints remained accessible during testing.

### Impact

No impact on documented APIs.

May cause confusion during manual verification.

### Recommendation

If intended, document the behaviour.

Otherwise, consider exposing a simple health or status endpoint.

---

# Defect Statistics

Total Defects Identified: 2

Critical: 0

High: 0

Medium: 1

Low: 1

---

# Audit Conclusion

The identified defects do not prevent successful local execution of the repository.

Core functionality, API execution, dashboard operation, validation pipeline, and runtime behaviour were successfully verified.

The primary issue affecting production deployment is the platform-specific dependency identified during deployment validation.

No additional reproducible defects were identified during this audit.

---

**Prepared By**

Ankita Prajapati

Independent Engineering Auditor

18 July 2026
