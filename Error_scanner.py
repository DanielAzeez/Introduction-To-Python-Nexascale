def scan_log(file_path, severity="ERROR"):
    count = 0
    filtered_logs = []

    with open(file_path, "r") as log_file:
        for line in log_file:
            if severity in line:
                count += 1
                filtered_logs.append(line.strip())

    print(f"Found {count} occurrences of '{severity}' in logs.")

    if filtered_logs:
        print("\nFiltered logs:")
        for log in filtered_logs:
            print(log)

# Run the function
log_file_path = "sample.log"
scan_log(log_file_path, "ERROR")