## Initial setup

1. Set up virtualenv
2. `pip install -r requirements.txt`

## Run CLIP-as-service client

1. `python run_once.py` to download initial datasets and store in SQLite for faster loading in frontend
2. In a new terminal, `streamlit run frontend.py`
3. Set server in the sidebar
