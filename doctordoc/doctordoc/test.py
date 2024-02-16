try:
    from prompt_engineering import generate_prompt
    print("Successfully imported generate_prompt.")
    
    # Test generate_prompt with hardcoded parameters
    test_output = generate_prompt("void test_function() {}")
    print("Generated prompt:", test_output)
except Exception as e:
    print(f"Error: {e}")

