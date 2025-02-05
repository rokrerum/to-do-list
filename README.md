## Features

The application includes the following features:
- You can create new groups to organize your tasks.
- You can add new tasks to specific groups.
- You can remove entire groups along with their tasks.
- You can remove individual tasks from groups.
- You can change the status of tasks (e.g., mark them as done or not done).
- All groups and tasks are stored in a JSON file (dane.json) to retain data between sessions.
- The graphical user interface dynamically updates to reflect changes in tasks and groups.


## Getting Started

To get started with the application, you will need to have Python 3.x installed on your machine, along with the `customtkinter` library.

### Installing

1. First, clone the repository using the following command:
    ```bash
    git clone https://github.com/your-username/to-do-list.git
    cd to-do-list
    ```

2. Next, install the required libraries by running:
    ```bash
    pip install customtkinter
    ```

3. Finally, run the application with:
    ```bash
    python main.py
    ```

### Usage

<ol>
  <li> To add a group, click on the "Add group" button and enter the group name.</li>
  <li> To add tasks within each group, enter the task name and click the "Add" button.</li>
  <li> To toggle the status of a task, click the checkbox next to the task.</li>
  <li> To delete a task, click the "X" button next to the task.</li>
  <li> To delete a group along with all its tasks, click the "X" button next to the group.</li>
</ol>

## File Structure

The main files in the project include:
- `main.py`: This is the main script that runs the application.
- `dane.json`: This JSON file stores all tasks and groups.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Special Thanks

Special thanks to `customtkinter` for the GUI framework.
