import os

# A function that takes an action and adds it to our actions folder, for easy use in the future
def add_action(action_string, action_folder="actions"):
  # Assign a unique ID to the action based on the number of existing actions
  action_id = len(os.listdir(action_folder)) + 1 
  action_filename = f"{action_folder}/action_{action_id}.txt"

  with open(action_filename, 'w') as file:
    file.write(action_string)
  
  print(f"Action added: {action_id}")
