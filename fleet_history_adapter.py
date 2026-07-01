"""
fleet_history_adapter.py

Phase IV Ecosystem Attachment

Purpose:
Prepare NICAI outputs for the Fleet History Registry.

Ownership:
NICAI prepares payloads only.
Fleet History Registry owns historical persistence,
timeline construction, and historical analytics.
"""

CONTRACT_VERSION = "1.0"


def validate_fleet_history_payload(output: dict):
    """
    Validate minimum payload required for Fleet History attachment.
    """

    if not isinstance(output, dict):
        return False, "Invalid payload"

    if not output.get("trace_id"):
        return False, "Missing trace_id"

    return True, "VALID"


def prepare_fleet_history_payload(output: dict):
    """
    Prepare a standardized payload for Fleet History Registry.
    """

    valid, reason = validate_fleet_history_payload(output)

    if not valid:
        return {
            "status": "ERROR",
            "reason": reason
        }

    return {
        "status": "READY",
        "contract_version": CONTRACT_VERSION,

        "trace_id": output["trace_id"],

        "history_record": output,

        "replay_expected": True,

        "ownership_boundary": (
            "Fleet History Registry owns historical storage "
            "and timeline management. "
            "NICAI owns payload preparation only."
        )
    }