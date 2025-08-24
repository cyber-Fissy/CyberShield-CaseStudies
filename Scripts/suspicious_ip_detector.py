#!/usr/bin/env python3
"""
Suspicious IP Detector
Author: Akinola Fisayo
Experience: 3 Years Cybersecurity

Description:
    This script scans a log file for suspicious IP addresses. 
    An IP is considered suspicious if it appears more than a set threshold 
    (e.g., repeated failed logins from the same IP).

Usage:
    - Run the script
    - Enter the log file path (e.g., server_logs.txt)
    - Enter the threshold (e.g., 5)
    - The script will print all IPs that exceed the threshold.
"""

import re
from collections import defaultdict

def detect_suspicious_ips(file_path, threshold=5):
    """
    Detects suspicious IPs that appear more times than the threshold.

    Args:
        file_path (str): Path to the log file
        threshold (int): Minimum number of appearances to be flagged

    Returns:
        dict: Suspicious IPs with their counts
    """
    ip_pattern = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")  # IPv4 regex
    ip_counts = defaultdict(int)

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = ip_pattern.search(line)
                if match:
                    ip_counts[match.group()] += 1

        suspicious_ips = {ip: count for ip, count in ip_counts.items() if count >= threshold}
        return suspicious_ips

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}

if __name__ == "__main__":
    log_file = input("Enter the log file path: ")
    threshold = int(input("Enter threshold for suspicious activity (e.g., 5): "))
    results = detect_suspicious_ips(log_file, threshold)

    print("\n--- Suspicious IPs Detected ---")
    if results:
        for ip, count in results.items():
            print(f"{ip} → {count} hits")
    else:
        print("No suspicious IPs found.")
