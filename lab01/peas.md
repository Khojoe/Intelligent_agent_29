
# Lab 1: PEAS Analysis — Campus Information Bot

## 1. Introduction

PEAS stands for Performance Measure, Environment, Actuators and Sensors. It is used to describe an intelligent agent by identifying how its success is measured, where it operates, how it acts and what information it receives.

## 2. PEAS Description

| Component | Description |
|---|---|
| Performance Measure | Provides accurate and relevant campus information, responds clearly, avoids inventing information and admits when it does not know an answer. |
| Environment | University campus, students, visitors, campus facilities, offices and the available campus information database. |
| Actuators | Displays text responses, provides directions or information and asks clarification questions when necessary. |
| Sensors | Receives students' typed questions, conversation history and the supplied campus facts. |

## 3. Environment Properties

- **Partially observable:** The bot cannot know everything happening on campus or the user's exact circumstances.
- **Stochastic:** Users can ask unexpected questions or phrase similar questions differently.
- **Sequential:** Previous messages may influence the meaning of later questions, so conversation history matters.
- **Static:** The information environment is treated as unchanged during an individual response, although campus information can become outdated over time.
- **Discrete:** Communication happens through individual text messages and responses.
- **Multi-agent:** The interaction involves the bot and the student or visitor.

## 4. Connection to the Agent Design

The PEAS analysis influences the bot's system instructions and behaviour.

The performance measures establish the rules for good responses. The environment defines the information domain. The actuators determine what responses the bot can produce, while the sensors identify the information it receives.

The campus facts supplied to the model provide its reference knowledge. Conversation history allows it to maintain context across multiple interactions.

## 5. Conclusion

PEAS provides a structured way to understand the Campus Information Bot as an intelligent agent. It ensures that the system has clear objectives, understands its operating environment, receives relevant information and performs appropriate actions.
