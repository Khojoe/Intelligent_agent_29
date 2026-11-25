
import os
from pathlib import Path

from dotenv import load_dotenv
from litellm import completion


# Load the project's environment variables
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

MODEL = os.getenv("LLM_MODEL")


# Load campus information from a separate file
FACTS_FILE = Path(__file__).resolve().parent / "facts.md"

with open(FACTS_FILE, "r", encoding="utf-8") as file:
    CAMPUS_FACTS = file.read()


# System prompt derived from our PEAS analysis
SYSTEM_PROMPT = f"""
You are a helpful Campus Information Assistant.

YOUR GOAL:
Help students and visitors obtain accurate campus information.

PERFORMANCE RULES:
1. Answer questions clearly and politely.
2. Use ONLY information explicitly stated in the campus facts.
3. Do not expand, assume or invent additional details.
4. Do not turn broad descriptions into specific services.
5. If information is missing, clearly say you do not know.
6. Direct users to the Department Office when necessary.
7. Use conversation history to understand follow-up questions.
8. Never treat your general training knowledge as official campus information.

ENVIRONMENT:
You operate in a university campus information environment.
You interact with students and visitors through text.

ACTUATOR LIMITATIONS:
You can only provide text responses.
You cannot register students, book appointments,
change academic records or perform administrative actions.

CAMPUS KNOWLEDGE BASE:
{CAMPUS_FACTS}
"""


def run_bot():

    if not MODEL:
        print("Error: LLM_MODEL is missing from the .env file.")
        return

    # Conversation history stores previous messages
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("\n========================================")
    print("       CAMPUS INFORMATION BOT")
    print("========================================")
    print("Hello! How can I help you today?")
    print("Type 'quit' to exit.\n")

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Bot: Thank you for using the Campus Info Bot. Goodbye!")
            break

        # Add the user's message to conversation history
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = completion(
                model=MODEL,
                messages=messages,
                temperature=0
            )

            bot_reply = response.choices[0].message.content

            # Display the response
            print(f"\nBot: {bot_reply}\n")

            # Save the assistant's response for future turns
            messages.append({
                "role": "assistant",
                "content": bot_reply
            })

        except Exception as error:
            print(f"\nError communicating with the model: {error}\n")

            # Remove the unanswered user message
            messages.pop()


if __name__ == "__main__":
    run_bot()
