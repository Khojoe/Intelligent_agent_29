"""Lab 2: a ReAct agent from scratch (no framework).

Loop: the model writes a Thought and an Action; our code runs the tool and
sends back an Observation; repeat until the action is `finish` or max_steps.
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from litellm import completion

from parsing import parse
from prompts import build_system_prompt
from tools import TOOLS

load_dotenv()
MODEL = os.getenv("LLM_MODEL")
EVIDENCE_DIR = Path(__file__).resolve().parent / "evidence"

DEFAULT_QUESTION = (
    "I have GHS 1,200. I want 4 bags of rice at GHS 185 each and "
    "3 gallons of oil at GHS 95 each. How much will I have left?"
)

FORMAT_REMINDER = (
    "Your reply could not be parsed. Reply in exactly this format:\n"
    "Thought: <your reasoning>\n"
    "Action: <calculator | wiki_lookup | finish>\n"
    "Action Input: <input>"
)


def save_trace(lines):
    """Save a trace to evidence/trace_<n>.txt using the next free number."""
    EVIDENCE_DIR.mkdir(exist_ok=True)
    n = 1
    while (EVIDENCE_DIR / f"trace_{n}.txt").exists():
        n += 1
    path = EVIDENCE_DIR / f"trace_{n}.txt"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run_agent(question, max_steps=6, llm=completion, save=True):
    """Run the loop. Never raises: always returns a result dictionary.

    `llm` can be replaced by a fake function so the loop can be tested
    without calling a real model.
    """
    lines = []

    def emit(text):
        print(text)
        lines.append(text)

    messages = [
        {"role": "system", "content": build_system_prompt()},
        {"role": "user", "content": question},
    ]
    emit(f"Question: {question}\n")

    status, answer, total_tokens = "max_steps", None, 0

    for step in range(1, max_steps + 1):
        emit(f"--- Step {step} ---")
        try:
            # stop=["Observation:"] stops the model from inventing its own
            # observations: only our code may supply those.
            resp = llm(model=MODEL, messages=messages,
                       temperature=0, stop=["Observation:"])
        except Exception as err:  # rate limit, network, bad key, ...
            emit(f"API error: {type(err).__name__}: {err}")
            status = "api_error"
            break

        reply = (resp.choices[0].message.content or "").strip()
        usage = getattr(resp, "usage", None)
        total_tokens += getattr(usage, "total_tokens", 0) or 0

        emit(reply if reply else "(empty reply)")
        messages.append({"role": "assistant", "content": reply or "(empty reply)"})

        action, action_input = parse(reply)

        if action is None:                      # unparseable reply
            observation = FORMAT_REMINDER
        elif action == "finish":                # termination
            answer, status = action_input, "finished"
            emit(f"\nFinal answer: {answer}")
            break
        elif action not in TOOLS:               # unknown tool name
            observation = (f"Error: unknown action '{action}'. "
                           f"Choose one of: {', '.join(list(TOOLS) + ['finish'])}.")
        else:                                   # run the tool (our code, not the model)
            observation = TOOLS[action](action_input)

        emit(f"Observation: {observation}")
        messages.append({"role": "user", "content": f"Observation: {observation}"})
    else:
        emit(f"\nStopped: reached max_steps ({max_steps}) without a final answer.")

    emit(f"\n[status: {status} | total tokens: {total_tokens}]")
    path = save_trace(lines) if save else None
    return {"answer": answer, "status": status,
            "tokens": total_tokens, "trace_file": path}


if __name__ == "__main__":
    if not MODEL:
        print("Error: LLM_MODEL is missing. Copy .env.example to .env and set it.")
        sys.exit(1)
    question = " ".join(sys.argv[1:]) or DEFAULT_QUESTION
    run_agent(question)
