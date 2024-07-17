This is a Python-based To-Do List application with a graphical user interface built using the customtkinter library. The application allows users to manage groups of tasks, add and delete tasks within those groups, and change the status of individual tasks. All data is stored in a JSON file for persistence.

Features
Create Groups: Add new groups to organize your tasks.
Add Tasks: Add new tasks to specific groups.
Delete Groups: Remove entire groups along with their tasks.
Delete Tasks: Remove individual tasks from groups.
Toggle Task Status: Change the status of tasks (e.g., mark as done or not done).
Data Persistence: All groups and tasks are stored in a JSON file (data.json) to retain data between sessions.
Dynamic Interface: The GUI dynamically updates to reflect changes in tasks and groups.
Getting Started
Prerequisites
Python 3.x
customtkinter library
Installing
Clone the repository:

sh
Skopiuj kod
git clone https://github.com/your-username/to-do-list.git
cd to-do-list
Install the required libraries:

sh
Skopiuj kod
pip install customtkinter
Run the application:

sh
Skopiuj kod
python main.py
Usage
Add a Group: Click on the "Add group" button and enter the group name.
Add Tasks: Within each group, you can add new tasks by entering the task name and clicking "Add".
Toggle Task Status: Click the checkbox next to a task to toggle its status.
Delete Tasks: Click the "X" button next to a task to delete it.
Delete Groups: Click the "X" button next to a group to delete the group along with all its tasks.
File Structure
main.py: The main script that runs the application.
data.json: The JSON file where all tasks and groups are stored.
