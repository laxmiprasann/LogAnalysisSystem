import os
import json

class QueryInterface:
    def __init__(self):
        self.log_files = [
            "log1.log",
            "log2.log",
            "log3.log",
            "log4.log",
            "log5.log",
            "log6.log",
            "log7.log",
            "log8.log",
            "log9.log"
        ]

    def print_log_files(self):
        for log_file in self.log_files:
            print(f"- {log_file}")

    def search_logs(self, level=None, log_string=None, timestamp=None):
        logs = []
        for log_file in self.log_files:
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    for line in f:
                        log = json.loads(line)
                        if self._matches_query(log, level, log_string, timestamp):
                            logs.append(log)
        return logs

    def _matches_query(self, log, level=None, log_string=None, timestamp=None):
        if level and log.get('level') != level:
            return False
        if log_string and log_string.lower() not in log.get('log_string', '').lower():
            return False
        if timestamp and not self._is_within_timestamp(log['timestamp'], timestamp):
            return False
        return True

    def _is_within_timestamp(self, log_timestamp, query_timestamp):
        if not query_timestamp:  # If timestamp is not provided, consider it as within range
            return True
        log_timestamp = log_timestamp.replace('Z', '+00:00')  # Convert Zulu time to UTC offset
        return query_timestamp[0] <= log_timestamp
