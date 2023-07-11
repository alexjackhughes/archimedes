from actions import add_action, get_action

import time

class Archimedes:
    def __init__(self, initial_identity, initial_goal, wait_time=1):
        self.identity = initial_identity
        self.goal = initial_goal

        self.current_thought = None
        self.current_action = None

        self.wait_time = wait_time

    # ...other methods...

    def run(self):
        flag = True
        while flag:
            add_action("Do one")
            time.sleep(self.wait_time)
            add_action("Do two")
            flag = False
            print(get_action('1'))
