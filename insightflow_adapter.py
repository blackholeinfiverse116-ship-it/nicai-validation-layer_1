"""
insightflow_adapter.py

Phase IV Ecosystem Attachment

Purpose:
Prepare NICAI intelligence outputs for the InsightFlow ecosystem.

Ownership:
NICAI prepares payloads only.
InsightFlow owns downstream analytics and visualization.
"""

CONTRACT_VERSION = "1.0"


def validate_insight_payload(output: dict):
    """
    Validate the minimum payload required for InsightFlow.
    """

    if not isinstance(output, dict):
        return False, "Invalid payload"

    if not output.get("trace_id"):
        return False, "Missing trace_id"

    if not output.get("risk_level"):
        return False, "Missing risk_level"

    return True, "VALID"


def prepare_insight_payload(output: dict):
    """
    Prepare a standardized payload for InsightFlow.
    """

    valid, reason = validate_insight_payload(output)

    if not valid:
        return {
            "status": "ERROR",
            "reason": reason
        }

    return {
        "status": "READY",
        "contract_version": CONTRACT_VERSION,
        "trace_id": output["trace_id"],

        "risk_level": output.get("risk_level"),
        "anomaly_type": output.get("anomaly_type"),
        "confidence": output.get("confidence"),

        "replay_expected": True,

        "ownership_boundary": (
            "InsightFlow owns downstream analytics. "
            "NICAI owns intelligence payload preparation only."
        )
    }