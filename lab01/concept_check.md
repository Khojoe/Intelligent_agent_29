# Lab 1: Agents Then and Now: PEAS and Your First LLM Call: Concept Check

## Q1. Give the PEAS description of a self-checkout machine at a supermarket.

Performance Measure:
Accurately scans products, calculates the correct total, processes payments securely and provides a smooth checkout experience.

Environment:
The supermarket, customers, products, barcode labels, payment systems and checkout area.

Actuators:
Display screen, payment terminal, receipt printer, speakers and conveyor belt controls.

Sensors:
Barcode scanner, weighing scale, touchscreen, payment reader and cameras.

## Q2. Is the Campus Info Bot's environment episodic or sequential? Justify your answer using what the bot needs to remember.

The Campus Info Bot operates in a sequential environment because its current responses can depend on previous interactions. It needs to remember conversation history to understand follow-up questions and maintain context. For example, when a student asks about the ICT Support Office and later asks for its room number, the bot uses the earlier conversation to understand what the student means.

## Q3. Which part of an LLM agent plays the role of the percept sequence?

The conversation history, which is stored as a list of previous user messages and assistant responses, plays the role of the percept sequence. It allows the agent to use information from previous interactions when responding to new questions.

## Q4. An agent gives a wrong office location because its facts block was out of date. Was it irrational? Explain.

Not necessarily. The agent may have made a decision based on the information available to it at the time. However, an agent should be designed to use reliable and updated information. If the facts block is outdated, the system's performance and accuracy will be affected even if it follows its instructions correctly.


