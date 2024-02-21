import streamlit as st
import ollama
from doctor_doc.prompt_engineering import generate_prompt as gp

# Specify the Ollama model you wish to use
model_name = 'llama2'  # Example model name, replace with your choice

def ollama_generator(prompt):
    """
    Communicates with Ollama to generate a response based on the given prompt.
    """
    messages = [{'role': 'user', 'content': prompt}]
    response = ''
    stream = ollama.chat(model=model_name, messages=messages, stream=True)
    for chunk in stream:
        response += chunk['message']['content']
        if chunk.get('done', False):
            break
    return response

def doctordoc(user_input):
    """
    Processes the user input to generate documentation using the Ollama model.
    """
    refined_prompt = gp(user_input)  # Enhance user input using the generate_prompt function
    documentation = ollama_generator(refined_prompt)  # Generate documentation using Ollama
    st.code(documentation, language='python')  # Display generated documentation

def main():
    st.image("img/imgred.png")  # Display a logo or image at the top of the app

    context = []  # Initialize context for storing conversation history

    st.title('Doctor Doc')

    # Text area for user's undocumented function input
    user_input = st.text_area("Please enter an undocumented function:", height=300, placeholder="Type here...", key="function_input")
    st.write(f'You wrote {len(user_input)} characters.')

    if st.button("Generate Documentation"):
        try:
            context.append(user_input)  # Update context with the user's current input
            doctordoc(user_input)  # Generate and display documentation
        except Exception as e:
            st.error("An error occurred: " + str(e))

    # Placeholder for future feature: File upload
    # data = st.file_uploader("Upload a file")

    # Placeholder for future feature: Download file
    # st.download_button("Download File", data)

if __name__ == "__main__":
    main()