def process_prompt(prompt, ai_model):
    """
    Wrapper that short-circuits "thank you" prompts before they reach the AI model.

    Args:
        prompt: The user's input string.
        ai_model: Any callable that accepts a prompt string and returns a response.

    Returns:
        "you're welcome" if the prompt is a thank you. Otherwise, delegates to ai_model.
    """
    if prompt.strip().lower() == "thank you":
        return "you're welcome"
    return ai_model(prompt)
