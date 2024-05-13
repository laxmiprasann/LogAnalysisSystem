import json
from datetime import datetime, timezone

class LogIngestor:
    def __init__(self):
        self.logs = []

    def create_log_entry(self, level, log_string, source):
        timestamp = datetime.now(timezone.utc).isoformat()
        log_data = {
            "level": level,
            "log_string": log_string,
            "timestamp": timestamp,
            "metadata": {
                "source": source
            }
        }
        self.logs.append(log_data)
        return json.dumps(log_data) + '\n'

    def search_logs(self, level=None, log_string=None, timestamp=None):
        results = []
        for log in self.logs:
            if level and log['level'] != level:
                continue
            if log_string and log_string not in log['log_string']:
                continue
            if timestamp and log['timestamp'] not in timestamp:
                continue
            results.append(log)
        return results

    def read_logs_from_files(self, log_files):
        print("Reading logs from the following files:")
        for log_file in log_files:
            print(f"- {log_file}")
            try:
                with open(log_file, 'r') as f:
                    for line in f:
                        log_data = json.loads(line)
                        self.logs.append(log_data)
            except Exception as e:
                print(f"Error reading log file {log_file}: {e}")