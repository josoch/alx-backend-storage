#!/usr/bin/env python3
"""
// Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats():
    """
    // Function to display stats about Nginx logs
    """
    client = MongoClient('mongodb://localhost:27017/')
    logs = client.logs.nginx

    total_logs = logs.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
