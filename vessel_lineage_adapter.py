"""
vessel_lineage_adapter.py

Phase IV Ecosystem Attachment

Purpose:
Prepare NICAI outputs for the Vessel Lineage Registry.

Ownership:
NICAI prepares lineage payloads only.
The Vessel Lineage Registry owns lineage persistence,
relationship tracking, and historical provenance.
"""

CONTRACT_VERSION = "1.0"


def validate_lineage_payload(output: dict):
    """
    Validate minimum payload required for Vessel Lineage attachment.
    """

    if not isinstance(output, dict):
        return False, "Invalid payload"

    if not output.get("trace_id"):
        return False, "Missing trace_id"

    return True, "VALID"


def prepare_lineage_payload(output: dict):
    """
    Prepare a standardized payload for the Vessel Lineage Registry.
    """

    valid, reason = validate_lineage_payload(output)

    if not valid:
        return {
            "status": "ERROR",
            "reason": reason
        }

    return {
        "status": "READY",
        "contract_version": CONTRACT_VERSION,

        "trace_id": output["trace_id"],

        "lineage_record": output,

        "replay_expected": True,

        "ownership_boundary": (
            "Vessel Lineage Registry owns lineage persistence "
            "and relationship management. "
            "NICAI owns payload preparation only."
        )
    }