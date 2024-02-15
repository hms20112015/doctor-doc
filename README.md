# doctor-doc
This repo uses llama2 to generate documented functions based on user input.

# Quickstart

1. Ensure you have the `llama2` model installed:

   ```bash
   ollama pull llama2
   ```

2. Install the Python dependencies.

   ```bash
   pip install poetry
   ```
   ```bash
   poetry shell
   ```
   ```bash
   poetry install
   ```

3. Run the example:

   ```bash
   streamlit run doctordoc.py
   ```