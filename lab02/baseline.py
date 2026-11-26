"""Lab 2, Step 1: the model on its own (no tools, no loop).

Writes evidence/baseline.md. YOU must mark each answer correct or incorrect:
check the arithmetic yourself, and verify the facts on Wikipedia.
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from litellm import completion

load_dotenv()
MODEL = os.getenv("LLM_MODEL")
OUT = Path(__file__).resolve().parent / "evidence" / "baseline.md"

BUDGET = (
    "I have GHS 1,200. I want 4 bags of rice at GHS 185 each and "
    "3 gallons of oil at GHS 95 each. How much will I have left?"
)
FACTUAL = [
    "What is the capital of the Bono East Region of Ghana?",
    "How many regions does Ghana have?",
]
TEMPERATURE = 0  # same as the agent, so the comparison is fair


def ask(question):
    resp = completion(model=MODEL, temperature=TEMPERATURE,
                      messages=[{"role": "user", "content": question}])
    return (resp.choices[0].message.content or "").strip()


def main():
    if not MODEL:
        print("Error: LLM_MODEL is missing. Copy .env.example to .env and set it.")
        sys.exit(1)

    out = ["# Lab 2 baseline: the model on its own (no tools)\n",
           f"Model: {MODEL} | temperature: {TEMPERATURE}\n",
           "## Budget question (correct answer: GHS 175)\n", f"> {BUDGET}\n"]
    for i in range(1, 4):
        answer = ask(BUDGET)
        hint = "yes" if "175" in answer else "no"
        out += [f"### Attempt {i}\n", answer + "\n",
                f"Auto-check (contains 175): {hint}. **Correct? [ ]** (verify yourself)\n"]

    out.append("## Factual questions\n")
    for q in FACTUAL:
        out += [f"### {q}\n", ask(q) + "\n",
                "**Correct? [ ]** Verified against: [source]. "
                "How confident did it sound? [note]\n"]

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Saved {OUT}. Open it and mark each answer correct or incorrect.")


if __name__ == "__main__":
    main()
