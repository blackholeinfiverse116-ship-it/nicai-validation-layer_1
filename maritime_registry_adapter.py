"""
maritime_registry_adapter.py

Phase IV Ecosystem Attachment

Purpose:
Prepare NICAI outputs for the Maritime Knowledge Registry.

Ownership:
NICAI prepares registry payloads only.
The Maritime Knowledge Registry owns storage, indexing,
search, and knowledge management.
"""

CONTRACT_VERSION = "1.0"


def validate_registry_payload(output: dict):
    """
    Validate minimum payload required for registry attachment.
    """

    if not isinstance(output, dict):
        return False, "Invalid payload"

    if not output.get("trace_id"):
        return False, "Missing trace_id"

    return True, "VALID"


def prepare_registry_payload(output: dict):
    """
    Prepare a standardized payload for the Maritime Knowledge Registry.
    """

    valid, reason = validate_registry_payload(output)

    if not valid:
        return {
            "status": "ERROR",
            "reason": reason
        }

    return {
        "status": "READY",
        "contract_version": CONTRACT_VERSION,

        "trace_id": output["trace_id"],

        "knowledge_record": output,

        "replay_expected": True,

        "ownership_boundary": (
            "Maritime Knowledge Registry owns persistence "
            "and knowledge management. "
            "NICAI owns payload preparation only."
        )
    }