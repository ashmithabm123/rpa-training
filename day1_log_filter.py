from logger_utils import Logger


logger = Logger()

try:
    error_count = 0

    logger.info("Log filtering process started.")

    with open("app_log.txt", "r") as file:
        with open("error_logs.txt", "w") as output:
            for line in file:
                if "ERROR" in line:
                    output.write(line)
                    error_count += 1

    logger.info(f"Found {error_count} ERROR lines.")
    logger.info("Error logs saved to error_logs.txt.")

except Exception as e:
    logger.error(f"Error: {e}")

finally:
    logger.info("Log filtering process completed.")