from bucket_emitter import emit_bucket_artifact

def route_action(output: dict) -> dict:
    """
    Maps NICAI output → execution action
    """

    risk = output.get("risk_level", "LOW")

    if risk == "HIGH":
        action = "RECOMMEND_ESCALATION_REVIEW"

    elif risk == "MEDIUM":
        action = "RECOMMEND_ENVIRONMENTAL_REVIEW"

    else:
        action = "CONTINUE_MONITORING"

    result = {
        "trace_id": output.get("trace_id", "unknown"),
        "action": action,
        "status": "EMITTED"
    }

    emit_bucket_artifact({
        "trace_id": result["trace_id"],
        "output": result,
        "layer": "ACTION_ROUTER"
    })

    return result