import json
import requests
import streamlit as st

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`

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
        # the response streams one token at a time, print that as we receive it
        response += response_part
        
        if 'error' in body:
            raise Exception(body['error']) 
        
        if body.get('done', False):
            st.code(response, language='c')
            return body['context']

def main():
    st.image("img/img.png")

    context = [] # the context stores a conversation history, you can use this to make the model more context aware

    st.title('Doctor Doc')

    txt = st.text_area(label="Please enter an undocumented function:", height=400, placeholder="Type here...",key="name")
    st.write(f'You wrote {len(txt)} characters.')

    try:
        if st.button("Click here to reveal your documented function:"):
            context = doctordoc(st.session_state.name, context)
    except:
        st.error("Please enter a valid input.")

    #Todo: File upload feature
    #data = st.file_uploader("Upload a C file")

    #Todo: Download C file feature
    #st.download_button("Download file",file)

if __name__ == "__main__":
    main()
