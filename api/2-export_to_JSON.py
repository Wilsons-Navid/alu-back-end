#!/usr/bin/python3
""""Module"""

import json
import requests
import sys

if __name__ == '__main__':
    # Get employee ID from arguments
    employee_id = sys.argv[1]
    # Construct user URL with ID
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    # Construct todos URL with ID
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    # Request user information as JSON
    user_info = requests.request('GET', user_url).json()
    # Request todos information as JSON
    todos_info = requests.request('GET', todos_url).json()

    # Extract username from user info
    employee_username = user_info["username"]

    # Create sorted todos information
    todos_info_sorted = [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], employee_username]))
        for task in todos_info]

    # Create user dictionary with todos
    user_dict = {str(employee_id): todos_info_sorted}
    # Write user dictionary to JSON file
    with open(str(employee_id) + '.json', "w") as file:
        file.write(json.dumps(user_dict))
