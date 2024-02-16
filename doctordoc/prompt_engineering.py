from config import documentation_examples

def generate_prompt(user_input):
    examples_str = '\n\n'.join(f"Example {i + 1}:\nDocumentation:\n{example['documentation']}\nCode:\n{example['code']}\n" for i, example in enumerate(documentation_examples))
    
    prompt = f"Here are some examples of well-documented functions:\n\n{examples_str}\n\nGiven the following function, generate detailed documentation including parameters, return values, and purpose:\n\n{user_input.strip()}"
    
    return prompt
