def generate_documentation_prompt(function_name, function_code, examples=None):
    """
    Generates a detailed prompt for the LLaMA2 model to document an undocumented function.

    :param function_name: The name of the function to document.
    :param function_code: The code of the function.
    :param examples: Optional examples of similar functions with documentation.
    :return: A string containing the prompt for the LLaMA2 model.
    """
    prompt = f"## Function to Document\nName: {function_name}\n```\n{function_code}\n```\n"

    if examples:
        prompt += "\n## Example Documentation\n"
        for example in examples:
            prompt += f"### {example['name']}\n```\n{example['code']}\n```\n---\n{example['documentation']}\n\n"

    prompt += "## Required Documentation\nPlease write detailed documentation for the above function, including parameters, return values, and a brief description.\n"

    return prompt
