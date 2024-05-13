import json
from datetime import datetime, timezone

def create_log_entry(level, log_string, source, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()
    log_data = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": {
            "source": source
        }
    }
    return json.dumps(log_data) + '\n'

def create_sample_log_files():
    # Log entries with various levels, log messages, and timestamps
    log_entries = [
        ("info", "Sample info log entry 1", None),
        ("info", "Sample info log entry 2", None),
        ("error", "Failed to connect", None),
        ("error", "Internal server error", None),
        ("success", "Operation successful", None),
        ("info", "Sample log entry with custom timestamp", "2023-09-14T12:30:00Z"),
        ("error", "Another failed attempt", "2023-09-15T10:45:00Z"),
        ("info", "Sample log entry 3", None),
        ("warning", "Warning: Resource usage high", None)
    ]

    for i in range(1, 10):
        file_name = f"log{i}.log"
        with open(file_name, 'w') as f:
            for level, log_string, timestamp in log_entries:
                log_entry = create_log_entry(level, log_string, file_name, timestamp)
                f.write(log_entry)

create_sample_log_files()
