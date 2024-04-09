import re
from collections import Counter

# Regular expression pattern for parsing Nginx log entries
pattern = r"(?P<ip>\S+) (?P<identity>\S+) (?P<user>\S+) \[(?P<time>[^\]]+)\] \"(?P<request>[^\"]+)\" (?P<status>\d+) (?P<size>\d+) \"(?P<referer>[^\"]+)\" \"(?P<user_agent>[^\"]+)\""

# Open the Nginx log file and read its contents
with open("nginx_access.log") as f:
    logs = f.readlines()

# Parse each log entry and extract the relevant information
parsed_logs = [re.match(pattern, log).groupdict() for log in logs]

# Count the number of 404 errors
four_oh_four_count = Counter(log["ip"] for log in parsed_logs if log["status"] == "404")

# Count the number of requests for each page
page_count = Counter(log["request"] for log in parsed_logs)

# Count the number of requests for each IP address
ip_count = Counter(log["ip"] for log in parsed_logs)

# Print the summarized report
print("Number of 404 errors:")
for ip, count in four_oh_four_count.items():
    print(f"- {ip}: {count}")

print("\nMost requested pages:")
for page, count in page_count.most_common(10):
    print(f"- {page}: {count}")

print("\nIP addresses with the most requests:")
for ip, count in ip_count.most_common(10):
    print(f"- {ip}: {count}")