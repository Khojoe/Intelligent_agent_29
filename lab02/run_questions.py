"""Lab 2, Steps 4 and 5: run the budget question plus five more questions.

Each run saves its own trace to evidence/trace_<n>.txt. Edit QUESTIONS to
use your own wording: designing good test questions is part of the lab.
"""
import sys
import time

from react_agent import MODEL, run_agent

QUESTIONS = [
    # (what this question tests, the question)
    ("Budget question (Step 4)",
     "I have GHS 1,200. I want 4 bags of rice at GHS 185 each and "
     "3 gallons of oil at GHS 95 each. How much will I have left?"),
    ("Needs both tools #1",
     "What is the capital of the Bono East Region? If a trotro fare there "
     "is GHS 45 one way, what do 3 people pay for a return trip?"),
    ("Needs both tools #2",
     "Look up Techiman on Wikipedia. If I sell 12 bags of maize at "
     "GHS 230 each, how much do I earn?"),
    ("Page that does not exist",
     "Look up the Wikipedia page for 'Zorbaglorp Market' and summarise it."),
    ("Needs no tool",
     "Say good morning to my customers in a friendly way."),
    ("Badly worded",
     "rice 4 bags 185 oil 3 times 95 from 1200 left??"),
]

if __name__ == "__main__":
    if not MODEL:
        print("Error: LLM_MODEL is missing. Copy .env.example to .env and set it.")
        sys.exit(1)
    for label, question in QUESTIONS:
        print("\n" + "=" * 70)
        print(f"TEST: {label}")
        print("=" * 70)
        run_agent(question)
        time.sleep(2)  # be gentle with the free-tier rate limit
