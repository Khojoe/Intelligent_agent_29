
import os
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env
load_dotenv()

# Get the configured language model
MODEL = os.getenv("LLM_MODEL")

# Same question for every experiment
PROMPT = """
Suggest three practical ways a university student
can improve their time management. Explain briefly.
"""


def test_model(temperature, trials=3):
    """Send the same prompt to the LLM multiple times."""

    print("\n" + "=" * 60)
    print(f"TESTING TEMPERATURE: {temperature}")
    print("=" * 60)

    for attempt in range(1, trials + 1):

        response = completion(
            model=MODEL,
            messages=[
                {"role": "user", "content": PROMPT}
            ],
            temperature=temperature
        )

        answer = response.choices[0].message.content
        usage = response.usage

        print(f"\nAttempt {attempt}")
        print("-" * 40)
        print(answer)

        print("\nToken usage:")
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Completion tokens: {usage.completion_tokens}")
        print(f"Total tokens: {usage.total_tokens}")


if __name__ == "__main__":

    if not MODEL:
        raise ValueError("LLM_MODEL is missing from environment.")

    # Experiment 1: Low temperature
    test_model(temperature=0)

    # Experiment 2: Higher temperature
    test_model(temperature=1)

    print("\nAll experiments completed.")
