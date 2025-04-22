def transform_data(data: list[dict]) -> list[dict]:
    return [clean_record(d) for d in data]

def clean_record(record: dict) -> dict:
    return {
        "id": record.get("id"),
        "value": record.get("value"),
        "timestamp": record.get("timestamp"),
    }
