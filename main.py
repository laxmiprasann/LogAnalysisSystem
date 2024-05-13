import json
from query_interface import QueryInterface

def main():
    # Initialize the Query Interface
    query_interface = QueryInterface()

    # Sample Queries
    print("Reading logs from the following files:")
    query_interface.print_log_files()

    # 1. Find all logs with the level set to "error".
    error_logs = query_interface.search_logs(level='error')
    print("\nError Logs:")
    for log in error_logs:
        print(log)

    # 2. Search for logs with the message containing the term "Failed to connect".
    connect_failure_logs = query_interface.search_logs(log_string='Failed to connect')
    print("\nLogs containing 'Failed to connect':")
    for log in connect_failure_logs:
        print(log)

    # 3. Filter logs between the timestamp "2023-09-10T00:00:00Z" and "2023-09-15T23:59:59Z".
    time_range_logs = query_interface.search_logs(timestamp=['2023-09-10T00:00:00Z', '2023-09-15T23:59:59Z'])
    print("\nLogs between specified timestamp range:")
    for log in time_range_logs:
        print(log)

if __name__ == "__main__":
    main()
