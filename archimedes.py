from actions import add_action, get_action
from memory import MemoryStore
from completion import generate_completion
import time
import re

class Archimedes:
    def __init__(self, initial_identity, initial_goal, wait_time=1):
        self.identity = initial_identity
        self.goal = initial_goal

        self.memory = MemoryStore()
        self.subconscious_thoughts = []

        self.wait_time = wait_time

    def do_thought(self, thought):
      formulate_question = generate_completion(f"Without explaining yourself, I want you to turn this idea: '{thought}' into a incredibly well-thought out query and goal, that I will then ask GPT to answer. You should not mention GPT, but simply try and write the best question possible that will achieve this idea.")

      messages = [
        {"role": "system", "content": f"You are a genius level assistant, that has assumed this identity: {self.identity}. Your goal is to: {self.goal}. You should aim to be as creative and clever as possible, and answer any questions to the best of your ability."},
        {"role": "user", "content": 'Write a one sentence story about a haunted house?'},
        {"role": "assistant", "content": 'The last man on earth sat alone in his house, when he heard a knock at the door.'},
        {"role": "user", "content": formulate_question}
      ]

      action = generate_completion(prompt="", messages=messages)  
      self.memory.store_thought(action)  # add the thought to memory

    def attempt_goal(self):
      memory = self.memory.retrieve_thought(self.goal)

      messages = [
        {"role": "system", "content": f"You are a genius level assistant, that has assumed this identity: {self.identity}. Your goal is to: {self.goal}. You should aim to be as creative and clever as possible, and answer any questions to the best of your ability."},
        {"role": "user", "content": 'Write a one sentence story about a haunted house?'},
        {"role": "assistant", "content": 'The last man on earth sat alone in his house, when he heard a knock at the door.'},
        {"role": "user", "content": f"I want you to assume this identity '{self.identity}' and do this goal {self.goal}. To hellp you achive this goal, here is some resources I've made: {memory}"}
      ]

      g = generate_completion(prompt="", messages=messages)   
      add_action(g)

    def stage(self, current_thought):
      self.do_thought(current_thought)

    def backstage(self):
      thoughts = generate_completion(f"You are {self.identity} and your goal is to: {self.goal}. Without explaining yourself, think step by step, and write three tasks to achieve this goal. Return it as a numbered list, in order of priority. Make sure to not repeat previous goals that have been set, like: {self.subconscious_thoughts}")
      self.subconscious_thoughts.extend(self.split_numbered_string(thoughts))

      return self.subconscious_thoughts.pop(0) if self.subconscious_thoughts else None

    def split_numbered_string(self, s):
      return [task.strip() for task in re.split(r'\d+\.\s*', s)[1:]]
    
    def reflection(self):
      new_self = generate_completion(f"Without explaining yourself, what is a better identity that you could assume to help you achieve this goal: {self.goal}? Here is your current identity: {self.identity}")
      self.identity = new_self

      new_goal = generate_completion(f"Without explaining yourself, write a better version of the following goal, that this person '{self.goal}' could achieve. It should be clearer, and more specific: {self.goal}")

    def run(self):
        count = 0
        while count < 5:
          current_thought = self.backstage()
          self.stage(current_thought)
          self.attempt_goal()
          self.reflection()

          print(f"Current Identity: {self.identity}")
          print(f"Current Goal: {self.goal}")

          count = count + 1
          
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