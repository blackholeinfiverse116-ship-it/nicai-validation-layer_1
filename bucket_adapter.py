"""
bucket_adapter.py

Phase IV Ecosystem Attachment

Purpose:
Prepare NICAI outputs for the Bucket ecosystem interface.

Ownership:
This adapter ONLY prepares the payload.
It does NOT perform persistence, networking, or Bucket implementation.
"""


CONTRACT_VERSION = "1.0"


def validate_bucket_payload(output: dict):
    """
    Validate minimum payload required for Bucket attachment.
    """

    if not isinstance(output, dict):
        return False, "Invalid payload"

    if not output.get("trace_id"):
        return False, "Missing trace_id"

    return True, "VALID"


def prepare_bucket_payload(output: dict):
    """
    Prepare a standardized payload for the Bucket interface.
    """

    valid, reason = validate_bucket_payload(output)

    if not valid:
        return {
            "status": "ERROR",
            "reason": reason
        }

    return {
        "status": "READY",
        "contract_version": CONTRACT_VERSION,
        "trace_id": output["trace_id"],

        "input": {},

        "output": output,

        "replay_expected": True,

        "ownership_boundary": (
            "Bucket owns persistence. "
            "NICAI owns payload preparation only."
        )
    }