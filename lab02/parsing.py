"""Parsing the model's text protocol: Thought / Action / Action Input."""
import re

ACTION_RE = re.compile(
    r"Action:\s*([A-Za-z_]\w*)\s*\n\s*Action Input:\s*(.*)", re.DOTALL
)


def _clean(text: str) -> str:
    """Trim whitespace and one layer of matching quotes or backticks."""
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "`\"'":
        text = text[1:-1].strip()
    return text


def parse(text: str):
    """Return (action, action_input), or (None, None) if the reply is unparseable."""
    match = ACTION_RE.search(text or "")
    if not match:
        return None, None
    action = match.group(1).strip().lower()
    action_input = _clean(match.group(2))
    return action, action_input


if __name__ == "__main__":
    # Step 3 checkpoint: one reply parsed into an action and an input.
    sample = "Thought: I need the total cost.\nAction: calculator\nAction Input: 4*185 + 3*95"
    print(parse(sample))          # ('calculator', '4*185 + 3*95')
    print(parse("Hello there"))   # (None, None)
