from actions import add_action, get_action
from memory import MemoryStore
from completion import generate_completion
import time

class Archimedes:
    def __init__(self, initial_identity, initial_goal, wait_time=1):
        self.identity = initial_identity
        self.goal = initial_goal

        self.memory = MemoryStore()
        self.subconscious_thoughts = []

        self.wait_time = wait_time

    def do_thought(self, thought):
      formulate_question = generate_completion(f"Without explaining yourself, I want you to turn this idea: '{thought}' into a incredibly well-thought out query and goal, that I will then ask GPT to answer. You should not mention GPT, but simply try and write the best question possible that will achieve this idea.")
      print(f"The question: {formulate_question}")

      messages = [
        {"role": "system", "content": f"You are a genius level assistant, that has assumed this identity: {self.identity}. Your goal is to: {self.goal}. You should aim to be as creative and clever as possible, and answer any questions to the best of your ability."},
        {"role": "user", "content": 'Write a one sentence story about a haunted house?'},
        {"role": "assistant", "content": 'The last man on earth sat alone in his house, when he heard a knock at the door.'},
        {"role": "user", "content": formulate_question}
      ]

      action = generate_completion(prompt="", messages=messages)   
      add_action(action)
      # self.memory.store_thought(action) add the story to memory

    def conscious_thought(self, current_thought):
      # reflect_on_thought = generate_completion(f"Pretend that you are {self.identity} and you had the thought: {current_thought}. You are trying to achieve this goal: {self.goal}. Is this a good idea to act on? How could it be improved to achieve our current goal?")
      self.do_thought(current_thought)

    def run(self):
        flag = True
        while flag:
          self.conscious_thought("Why not write a story about a haunted house?")
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

          # Converting thoughts into actions
          # do_thought('We should work out what 2+2 equals')

          # Running OpenAI chat completion
          # completion = generate_completion("what does 2+2 equal?")
          # print(completion)

          flag = False