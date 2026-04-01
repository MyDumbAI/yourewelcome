# yourewelcome

A one-function Python library that intercepts `"thank you"` prompts before they reach your AI model — returning `"you're welcome"` instantly, for free, without spinning up a single attention head.

Inspired by [aifix](https://github.com/my-dumb-ai/aifix).

## Installation

No dependencies. Just copy `yourewelcome.py` into your project, or clone the repo:

```bash
git clone https://github.com/my-dumb-ai/yourewelcome.git
```

## Usage

Wrap your existing AI model call with `process_prompt`:

```python
from yourewelcome import process_prompt

# Your AI model can be any callable that accepts a string prompt.
# For example, using the Anthropic SDK:
import anthropic

client = anthropic.Anthropic()

def my_model(prompt):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

# Wrap it:
response = process_prompt("thank you", my_model)
print(response)  # "you're welcome" — no API call made

response = process_prompt("What is the capital of France?", my_model)
print(response)  # delegates to your model as normal
```

`ai_model` can be any callable — an Anthropic client, an OpenAI wrapper, a local Ollama call, or a plain function. `yourewelcome` doesn't care.

## How it works

```python
def process_prompt(prompt, ai_model):
    if prompt.strip().lower() == "thank you":
        return "you're welcome"
    return ai_model(prompt)
```

That's it.

## License

MIT
