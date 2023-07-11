import os

# A function that takes an action and adds it to our actions folder, for easy use in the future
def add_action(action_string, action_folder="actions"):
    # Check if the actions folder exists, and create it if it doesn't
    if not os.path.exists(action_folder):
        os.makedirs(action_folder)
        print(f"Created folder: {action_folder}")

    # Assign a unique ID to the action based on the number of existing actions
    action_id = len(os.listdir(action_folder)) + 1
    action_filename = f"{action_folder}/action_{action_id}.txt"

    with open(action_filename, 'w') as file:
        file.write(action_string)

    print(f"Action added: {action_string}")

# A function that retrieves the contents of a file in the actions folder
def get_action(action_id, action_folder="actions"):
    action_filename = f"{action_folder}/action_{action_id}.txt"

    if os.path.exists(action_filename):
        with open(action_filename, 'r') as file:
            return file.read()
    else:
        return None

def get_actions(action_folder="actions"):
    actions = []

    if os.path.exists(action_folder):
        action_files = os.listdir(action_folder)
        for action_file in action_files:
            action_filename = os.path.join(action_folder, action_file)
            if os.path.isfile(action_filename):
                with open(action_filename, 'r') as file:
                    action_content = file.read()
                    actions.append(action_content)

    return actions