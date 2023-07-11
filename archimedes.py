from actions import add_action, get_action
from memory import MemoryStore
from completion import generate_completion
import time

class Archimedes:
    def __init__(self, initial_identity, initial_goal, wait_time=1):
        self.identity = initial_identity
        self.goal = initial_goal

        self.memory = MemoryStore()

        self.wait_time = wait_time

    # ...other methods...

    def run(self):
        flag = True
        while flag:
          completion = generate_completion("what does 2+2 equal?")
          print(completion)
          # thought = self.run_backstage()
          # if thought:
          #   conscious_thought = self.run_stage(thought)
          #   if conscious_thought:
          #     action = do_action("conscious_thought")
          #     add_action(action)
          
          # REFERENCE:
          # Running memory
          # self.memory.store_thought('hello world')
          # x = self.memory.retrieve_thought('hello')
          # Adding actions
          # add_action("Do one")
          # time.sleep(self.wait_time)
          # add_action("Do two")
          flag = False