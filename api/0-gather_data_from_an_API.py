"""
- Get the user id from the command line argument
- Access the API endpoint that gives you the details about a user and their todos
- Count the total number of items in the returned data
- Count the total number of items that have the completed status to be true
- Display the content the way it is displayed in the example on the intranet
"""

import requests
import sys


employee_id = sys.argv[1]
employee_details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
employee_todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

employee_details = requests.get(employee_details_url)
employee_details = employee_details.json()
employee_name = employee_details['name']


todos = requests.get(employee_todos_url)
total_task = len(todos.json())

total_completed = 0
titles_completed = []

# get the total number of items completed and the respective titles
for todo in todos.json():
    if todo['completed']:
        total_completed += 1
        titles_completed.append(todo['title'])

text_to_print = f"Employee {employee_name} is done with tasks({total_completed}/{total_task}):"


print(text_to_print)

for item in titles_completed:
    print(f"\t{item}")
