# Archimedes AGI

Archimedes is a personal project aimed at developing a powerful and versatile AI system inspired by the concept of AGI. The project focuses on building an intelligent agent capable of performing a wide range of tasks, learning from its environment, and exhibiting general problem-solving abilities.

## Features

- **Versatile AI**: Archimedes AGI is designed to be a flexible and adaptable AI system, capable of handling various tasks across different domains.
- **Learning Capabilities**: The AGI employs state-of-the-art machine learning algorithms to acquire knowledge and improve its performance over time.
- **Problem-solving Abilities**: Archimedes AGI is equipped with advanced reasoning and decision-making capabilities to solve complex problems and make informed choices.
- **Extensibility**: The project is structured in a modular way, allowing for easy integration of new functionalities and expansion of its capabilities.
- **Memory**: Archimedes has the ability to remember, and use thoughts in the future.
- **Actions**: Archimedes tries to act, and create actions on the world. Currently limited by what is capable of a computer, but the concept is anything on a computer it can also do.

## Getting Started

These instructions will help you set up and run the Archimedes AGI project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- [Add any additional prerequisites or dependencies here]

### Installation

1. Clone the repository:

git clone https://github.com/alexjackhughes/archimedes.git

2. Navigate to the project directory:

cd archimedes

3. Install the required dependencies:

pip install -r requirements.txt

### Usage

[Provide instructions on how to use and interact with the Archimedes AGI system. Include any specific commands or steps needed to run the AI or any related scripts.]

### Contributing

Contributions are welcome! If you would like to contribute to Archimedes AGI, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your changes
5. Submit a pull request

### License

[MIT]

### Acknowledgments

[Alex Hughes](twitter.com/alexjackhughes)

## TODO

[Link](https://chat.openai.com/c/fd5079b3-c798-46c9-aab5-32318a119168)

Create the AGI System Class:

Initialization of the system with a given identity and goal.
A method to generate new thoughts based on the current goal.
A method to present the most relevant thought to the "stage".
A method to allow the ego to generate new actions based on the thought currently on the stage.
A method to evaluate the success of these actions in achieving the goal.
A method to update the ego's sense of self based on the outcomes of the actions and new experiences.
A method to continually evaluate the success of the current process in achieving the goal and, if needed, generate a new thought to re-evaluate the current process and consider a different direction.
Create a Main Execution Flow:

Initialize the AGI system.
Enter a loop where the system continuously generates new thoughts, presents them to the stage, generates actions, performs them, and evaluates their outcomes.
Update the ego's sense of self and the system's goal as needed based on the outcomes of the actions.
Continually monitor and adjust the system's process based on its success in achieving the goal.
Create a Backstage Process:

Continually generate new thoughts in the background.
Rank these thoughts based on their relevance to the goal and the ego's current sense of self.
Present the most relevant thought to the stage for the ego to consider.
Integrate the MemoryStore with the AGI System:

Store each thought and the corresponding action in the MemoryStore after it's processed on the stage.
Retrieve relevant thoughts from the MemoryStore when generating new thoughts.
Use the MemoryStore to help update the ego's sense of self based on past experiences.
These steps give a high-level plan for building the AGI system as per our discussions. Each step involves a significant amount of work and could potentially be broken down further into sub-steps. The actual implementation would also need to take into account various practical considerations, such as the specific AI models and APIs to use, the ways to interact with the system's environment, and the criteria for evaluating the success of actions and processes.
