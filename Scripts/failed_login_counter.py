#!/usr/bin/env python3
"""
Failed Login Counter
Author: Akinola Fisayo
Experience: 3 Years Cybersecurity

Description:
    This script scans a log file and counts the number of failed login attempts. 
    Useful for detecting brute-force attacks or unauthorized access attempts.

Usage:
    - Run the script
    - Enter the log file path (e.g., auth_logs.txt)
    - The script will display how many failed login attempts were found.
"""

def count_failed_logins(file_path):
    """
    Counts the number of failed login attempts in a log file.

    Args:
        file_path (str): Path to the log file

    Returns:
        int: Number of failed login attempts
    """
    try:
        with open(file_path, 'r') as log_file:
            failed_count = 0
            for line in log_file:
                if "failed login" in line.lower():
                    failed_count += 1
            return failed_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1

if __name__ == "__main__":
    log_file = input("Enter the log file path: ")
    result = count_failed_logins(log_file)

    if result >= 0:
        print(f"\nTotal Failed Login Attempts: {result}")
