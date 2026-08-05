
# Gemini AI Chatbot — Step-by-Step Tutorial

A minimal, hands-on Streamlit app that demonstrates how to build a conversational Q&A chatbot using Google Gemini (via the `google-genai` client). This repository contains a compact example to get you from zero to a working local chatbot in minutes — perfect for learning or prototyping.

---

## Highlights
- Tiny, easy-to-read codebase (single-file example: `app.py`)
- Built with Streamlit for immediate UI and local hosting
- Uses Google Gemini model (`gemini-3.6-flash` by default) via `google-genai`
- Keeps conversation in Streamlit session state for simple chat history

---

## Table of contents
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Features](#features)
- [How it works (internals)](#how-it-works-internals)
- [Configuration & secrets](#configuration--secrets)
- [Troubleshooting](#troubleshooting)
- [Next steps & improvements](#next-steps--improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Requirements
- Python 3.8+ (3.10+ recommended)
- An active Google Gemini API key / credentials that can be used with the `google-genai` Python client
- pip

Dependencies are listed in `requirements.txt`:
- streamlit
- google-genai

---

## Quick start

1. Clone:
```bash
git clone https://github.com/mdzaheerjk/Step-by-Step-Tutorial-to-Create-Conversational-Q-A-Chatbot-using-Gemini-Pro.git
cd Step-by-Step-Tutorial-to-Create-Conversational-Q-A-Chatbot-using-Gemini-Pro
```

2. Install:
```bash
python -m pip install -r requirements.txt
```

3. Run:
```bash
streamlit run app.py
```

4. In the web UI:
- Open the sidebar
- Enter your Gemini API key
- Choose the model (default: `gemini-3.6-flash`)
- Ask questions in the chat input

---

## Features
- Simple Streamlit chat UI with history stored in `st.session_state.messages`
- Model selection (currently set to `gemini-3.6-flash`)
- Clear chat button to reset conversation
- Error handling surface: displays errors from the API or network

---

## How it works (internals)
- `app.py` uses Streamlit's chat UI primitives:
  - On user input, the prompt is appended to `st.session_state.messages`
  - `google.genai.Client` (constructed with the provided API key) calls `models.generate_content`
  - The assistant response is added back into `st.session_state.messages` and rendered in the chat UI

Key code references:
- `app.py` — main UI and logic
- `requirements.txt` — required packages

---

## Configuration & secrets
- By default the app asks for your Gemini API key in the sidebar (keeps secrets off disk).
- For automation or CI, you can set an environment variable and modify the code to use it:

```python
import os
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
```

Security tips:
- Never commit your API key.
- Use environment variables or secret stores when deploying.
- Restrict API key permissions where possible.

---

## Troubleshooting
- ModuleNotFoundError: make sure you installed dependencies:
  ```bash
  python -m pip install -r requirements.txt
  ```
- API errors (authentication, rate limits, model access):
  - Confirm your Gemini API key is valid and has access to the selected model.
  - Check network connectivity.
  - If you receive permission errors for a particular `gemini-*` model, try a model you are allowed to use.
- Streamlit UI not showing:
  - Confirm you ran `streamlit run app.py` and check the CLI output for the local URL.

---

## Next steps & improvements (ideas you can implement)
- Persist chat history to a file or database (SQLite, Supabase).
- Add streaming responses if the client supports incremental output.
- Add retrieval-augmented generation (RAG): add embeddings + a vector store (FAISS, Chroma) to answer from your docs.
- Deploy to Streamlit Community Cloud, Render, or Vercel for public access.
- Add unit tests and CI to validate dependencies and linting.
- Add environment-based API key handling (Streamlit secrets, env vars) and optional multi-model support.

Example: simple environment-based key usage:
```python
import os
api_key = os.getenv("GEMINI_API_KEY") or st.text_input("Enter Gemini API Key", type="password")
client = genai.Client(api_key=api_key)
```

---

## Contributing
- Improvements and PRs welcome:
  - Add features (persistence, RAG)
  - Harden error handling and edge cases
  - Improve UX (messages timestamps, user avatars, streaming)
- Please follow a small PR: describe the change, include tests where applicable.

---

## License
This project includes a LICENSE file. Review it for reuse and distribution terms.

