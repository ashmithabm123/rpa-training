try:
    error_count = 0

    with open("app_log.txt", "r") as file:
        with open("error_logs.txt", "w") as output:
            for line in file:
                if "ERROR" in line:
                    output.write(line)
                    error_count += 1

    print(f"Found {error_count} ERROR lines.")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Log filtering process completed.")