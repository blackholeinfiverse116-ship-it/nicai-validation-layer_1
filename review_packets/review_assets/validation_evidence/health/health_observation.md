# Health Endpoint Observation

The deployed production backend currently does not expose a dedicated `/health` endpoint.

Accessing:

https://nicai-intelligence-engine-3.onrender.com/health

returns:

404 Not Found

This behavior matches the current implementation and has been documented in the API Compatibility Report. It is not considered a deployment defect.