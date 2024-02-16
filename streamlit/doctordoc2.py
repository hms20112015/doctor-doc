# doctordoc.py

import json
import requests
import streamlit as st
from doctordoc.prompt_engineering import generate_prompt
model = 'llama2' 

def doctordoc(prompt, context):
    response = ''
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        response += response_part
        
        if 'error' in body:
            raise Exception(body['error']) 
        
        if body.get('done', False):
            st.code(response, language='c')
            return body['context']

def main():
    st.image("img/img.png")

    context = [] 

    st.title('Doctor Doc')

    txt = st.text_area(label="Please enter an undocumented function:", height=400, placeholder="Type here...", key="name")
    st.write(f'You wrote {len(txt)} characters.')

    try:
        if st.button("Click here to reveal your documented function:"):
            prompt = generate_prompt(st.session_state.name)  # Generate prompt using user input
            context = doctordoc(prompt, context)  # Call doctordoc with the generated prompt
    except:
        st.error("Please enter a valid input.")

if __name__ == "__main__":
    main()
