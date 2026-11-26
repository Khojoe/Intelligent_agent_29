"""Lab 2 tools: the actions the ReAct agent can take.

The model never runs these. It only writes text that names a tool; our code
(react_agent.py) parses that text, calls the function and feeds the result
back as an Observation.
"""
import ast
import operator as op

import requests

# ---------------------------------------------------------------- calculator
# Only these operators are allowed. Anything else raises an error, so the
# model (or a user) cannot run arbitrary code through the calculator.
OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
}


def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.operand))
    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Safely evaluate an arithmetic expression (never uses eval)."""
    try:
        expr = expression.replace(",", "")
        return str(_eval(ast.parse(expr, mode="eval").body))
    except Exception as e:
        return f"Error: {e}"


# ------------------------------------------------------------- wikipedia
def wiki_lookup(title: str) -> str:
    """Return the first part of a Wikipedia page summary."""
    url = ("https://en.wikipedia.org/api/rest_v1/page/summary/"
           + title.strip().replace(" ", "_"))
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "DCIT403-lab"})
    except requests.RequestException as e:
        return f"Error: could not reach Wikipedia ({type(e).__name__})."
    if r.status_code != 200:
        return f"No Wikipedia page found for '{title}'."
    return r.json().get("extract", "")[:800]


# --------------------------------------------------------------- registry
# The agent looks tools up here. To add a tool (for example the stretch task
# convert_currency), add it to both dictionaries and the prompt updates itself.
TOOLS = {
    "calculator": calculator,
    "wiki_lookup": wiki_lookup,
}

TOOL_DESCRIPTIONS = {
    "calculator": (
        "Evaluates an arithmetic expression. Input: an expression such as "
        "4*185 + 3*95. Supports + - * / and parentheses."
    ),
    "wiki_lookup": (
        "Returns the opening summary of a Wikipedia page. Input: the page "
        "title, such as Bono East Region."
    ),
}


if __name__ == "__main__":
    # Step 2 checkpoint: test the tools directly before using the model.
    print(calculator("4*185 + 3*95"))                # expect 1025
    print(calculator("1,200 - 1025"))                # expect 175
    print(calculator("__import__('os')"))            # expect an Error
    print(wiki_lookup("Bono East Region")[:200])
    print(wiki_lookup("Zorbaglorp Market"))          # expect "No Wikipedia page..."
