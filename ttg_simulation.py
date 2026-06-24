from bucket_emitter import emit_bucket_artifact


def emit_ttg_consume(participation: dict):

    ttg_event = {
        "trace_id": participation.get("trace_id"),
        "consumer": "TTG",
        "simulation_pack": "RUDRA_ATHARVA",
        "consume_status": "CONSUMED"
    }

    emit_bucket_artifact({
        "trace_id": ttg_event["trace_id"],
        "output": ttg_event,
        "layer": "TTG_CONSUME"
    })

    return ttg_event