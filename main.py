from archimedes import Archimedes

# Incredible short story horror writer
# initial_identity = "Your name is Archimedes, you are a world-class writer of short horror fiction."
# initial_goal = "To write the best short horror story ever written."

# initial_identity = "Your name is Archimedes, you are a world-class writer of haikus based on the war."
# initial_goal = "To write the best haiku ever written."

initial_identity = "Your name is Ben Williams, you are a war veteran and now an exceptional motivatior and leadership coach."
initial_goal = "To create a simple course to take managers and make them leaders."

my_AI = Archimedes(initial_identity, initial_goal, wait_time=1)

# Run the AGI system
my_AI.run()