#!/usr/bin/env python3
"""
Log Search Tool
Author: Akinola Fisayo
Experience: 3 Years Cybersecurity

Description:
    This script helps security analysts quickly search through log files 
    for suspicious keywords such as 'failed login', 'error', or 'unauthorized'. 
    It saves time during incident investigations by pinpointing relevant lines in logs.

Usage:
    - Run the script
    - Enter the log file path (e.g., system_logs.txt)
    - Enter the keyword you want to search for (e.g., "error")
    - The script will print out all matching lines with line numbers
"""

import re  # Regular expressions library for keyword matching

def search_logs(file_path, keyword):
    """
    Searches through the specified log file for a given keyword.

    Args:
        file_path (str): Path to the log file
        keyword (str): The keyword or phrase to search for

    Returns:
        list: Lines from the log file that match the keyword
    """
    try:
        with open(file_path, 'r') as log_file:
            matches = []
            for line_num, line in enumerate(log_file, start=1):
                # Check if the keyword appears in this line (case-insensitive)
                if re.search(keyword, line, re.IGNORECASE):
                    matches.append(f"Line {line_num}: {line.strip()}")
            return matches

    except FileNotFoundError:
        return [f"Error: File '{file_path}' not found."]
    except Exception as e:
        return [f"An error occurred: {e}"]

if __name__ == "__main__":
    # Prompt user for inputs
    log_file = input("Enter the log file path: ")
    keyword = input("Enter keyword to search for: ")

    # Perform the search
    results = search_logs(log_file, keyword)

    # Display results
    print("\n--- Search Results ---")
    if results:
        for result in results:
            print(result)
    else:
        print("No matches found.")
