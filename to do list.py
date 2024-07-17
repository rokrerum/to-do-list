import customtkinter
import tkinter.simpledialog as simpledialog
import json
import os


def create_file():
    files = os.listdir()
    if "data.json" not in files:
        base = {}
        with open('data.json', 'w') as file:
            json.dump(base, file, indent=4)


def get_group_list():
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Get the list of group names
    group_list = list(data.keys())
    
    return group_list


def get_data_from_group(group):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Check if the group exists
    if group not in data:
        print(f"Group {group} does not exist in the data.")
        return []
    # Get data from the specified group and place them in separate lists
    data_list = [list(item.values()) for item in data[group]]
    
    return data_list


def add_group(group_name):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Check if the group exists, if not, create it as an empty list
    if group_name not in data:
        data[group_name] = []
        # Save updated data to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Created a new group: {group_name}")
    else:
        print(f"Group {group_name} already exists.")


def add_data(group_name, value):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Check if the group exists, if not, create it
    if group_name not in data:
        data[group_name] = []
    # Add a new person to a specific group
    new_person = {
        "name": value,
        "status": 0
    }
    data[group_name].append(new_person)  # the group name to which you are adding data
    # Save updated data to the JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def delete_group(group_name):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Check if the group exists, if so, delete it
    if group_name in data:
        del data[group_name]
        # Save updated data to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Deleted group: {group_name}")
    else:
        print(f"Group {group_name} does not exist.")


def delete_data_from_group(group_name, criteria):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Check if the group exists
    if group_name in data:
        # Filter data in the group, leaving only those that do not meet the criteria
        new_group = [item for item in data[group_name] if not all(item.get(k) == v for k, v in criteria.items())]
        # Update the group in the data
        data[group_name] = new_group
        # Save updated data to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data meeting the criteria {criteria} has been removed from group {group_name}.")
    else:
        print(f"Group {group_name} does not exist.")


def change_value_in_file(group_name, data_name, new_value):
    # Load data from file
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    # Check if the group exists
    if group_name in data:
        # Go through all the data in the group
        for item in data[group_name]:
            # Check if the data name matches
            if item["name"] == data_name:
                # Change the value of the 'status' field
                item["status"] = new_value
        
        # Save updated data to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Changed the 'status' value to {new_value} for data with name {data_name} in group {group_name}.")
    else:
        print(f"Group {group_name} does not exist.")


def add_field_to_interface(group_name, value, status=0):
    # Add a new label to the group frame in the interface
    if group_name in frames_dict:
        group_frame = frames_dict[group_name]
        
        data = customtkinter.CTkFrame(group_frame)
        data.grid(sticky="ew", padx=10, pady=10)
        
        # Use the variable value for the data name
        data_name = value

        # Function to change the status of the data
        def change_status(group_name, data_name):
            # Load data from file
            with open('data.json', 'r') as file:
                data = json.load(file)
            
            # Check if the group exists
            if group_name in data:
                # Go through all the data in the group
                for item in data[group_name]:
                    # Check if the data name matches
                    if item["name"] == data_name:
                        # Change the value of the 'status' field
                        item["status"] = 1 if item["status"] == 0 else 0
                
                # Save updated data to the JSON file
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                
                # Optionally: refresh the interface to reflect the changes
                # You can add code here to refresh the interface

                print(f"Changed the 'status' value for data {data_name} in group {group_name}.")
            else:
                print(f"Group {group_name} does not exist.")

        change_status_button = customtkinter.CTkCheckBox(data, text="", width=30, height=30, command=lambda: change_status(group_name, data_name))
        change_status_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Set the CheckBox status
        if status == 1:
            change_status_button.select()
        
        delete_button = customtkinter.CTkButton(data, text="X", width=30, height=30, command=lambda: delete_field(group_name, data, data_name))
        delete_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        
        label = customtkinter.CTkLabel(data, text=value)
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
    else:
        print(f"Group {group_name} does not exist in the interface.")


def add_group_to_interface(group_name):
    # Create a frame for the group
    group_frame = customtkinter.CTkFrame(frame)
    group_frame.grid(sticky="ew", padx=10, pady=10)
    
    # Group label
    button = customtkinter.CTkButton(group_frame, text=group_name, command=lambda: switch_between_subsections(group_name))
    button.grid(row=0, column=0, padx=10, pady=10)
    
    # Button to delete the group
    delete_button = customtkinter.CTkButton(group_frame, text="X", width=30, height=30, command=lambda: delete_group_and_field(group_name, group_frame))
    delete_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    # Add a frame for the group data
    name = customtkinter.CTkScrollableFrame(app, width=400, height=200)
    name.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    
    # Text field to enter new information
    entry = customtkinter.CTkEntry(name)
    entry.grid(row=1, column=0, padx=10, pady=10)

    # Button to add new information
    add_button = customtkinter.CTkButton(name, text="Add", command=lambda: add_new_information(group_name, entry.get()))
    add_button.grid(row=1, column=1, padx=10, pady=10)

    # Add the frame to the global dictionary
    global frames_dict
    frames_dict[group_name] = name


def add_new_information(group_name, value):
    if value:
        add_data(group_name, value)
        add_field_to_interface(group_name, value)


def switch_between_subsections(group_name):
    # Hide all frames
    for frame in frames_dict.values():
        frame.grid_remove()
    # Show the selected frame
    frames_dict[group_name].grid()


def delete_group_and_field(group_name, frame):
    delete_group(group_name)
    frame.grid_remove()
    # Remove the frame from the global dictionary
    global frames_dict
    del frames_dict[group_name]


def delete_field(group_name, frame, data_name):
    # Delete data from the JSON file
    delete_data_from_group(group_name, {"name": data_name})
    # Remove the frame from the interface
    frame.grid_remove()


def get_name():
    app = customtkinter.CTk()  # We need the main window to use simpledialog
    app.withdraw()  # Hide the main window
    result = simpledialog.askstring("Enter name", "Enter the group name:")
    app.destroy()  # Destroy the main window after getting the result
    return result


# functions that combine the functionality of the program
def create_new_field(value):
    group_name = get_name()
    add_data(group_name, value)
    add_field_to_interface(group_name, value)


def create_new_group():
    group_name = get_name()
    if group_name:
        add_group(group_name)
        add_group_to_interface(group_name)


app = customtkinter.CTk()
app.title("To Do List")

# Dictionary to store frames
frames_dict = {}

# Left window
frame = customtkinter.CTkFrame(app, width=100, height=70)
frame.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="ns")

add_group_button = customtkinter.CTkButton(frame, text="Add group", command=create_new_group)
add_group_button.grid(row=1, column=0, pady=5, sticky="ew")

# functions to create the interface
create_file()

groups = get_group_list()

for i in groups:
    add_group_to_interface(i)  # add groups to the interface
    
    data = get_data_from_group(i)
    for j in range(len(data)):
        add_field_to_interface(i, data[j][0], data[j][1])  # add data to the interface

app.mainloop()
