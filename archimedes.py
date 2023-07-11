from actions import add_action

import time

class Archimedes:
    def __init__(self, wait_time=1):
        # self.identity = initial_identity
        # self.goal = initial_goal
        # self.memory = MemoryStore(memory_index)
        # self.current_thought = None
        # self.current_action = None
        self.wait_time = wait_time  # Wait time in seconds

    # ...other methods...

    def run(self):
        flag = True
        while flag:
            add_action("Do one")
            time.sleep(self.wait_time)
            add_action("Do two")
            flag = False
