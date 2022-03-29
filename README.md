## Initial setup

1. Set up virtualenv
2. `pip install -r requirements.txt`

## Run CLIP-as-service client/frontend

1. `python run_once.py` to download initial datasets and store in SQLite for faster loading in frontend
2. In a new terminal, `streamlit run frontend.py`
3. Set server in the sidebar

## Use your own datasets

Currently we pull two datasets **with pre-existing embeddings** from Jina Cloud using `DocumentArray.pull()`:

- `ttl-embedding`: Images and embeddings from [Totally Looks Like Dataset](https://sites.google.com/view/totally-looks-like-dataset)
- `ttl-textual`: Sentences and embeddings from Pride Prejudice

Why do we use pre-computed embeddings? Because our server doesn't have a GPU and can't handle all that heavy lifting (though a more powerful server could!). Our server only handles creating embeddings for the **user inputs** (either a line of text or an image)

To use your own dataset:

### On your local machine

1. Create a file to load your content into a `DocumentArray`
2. Create CLIP embeddings for it via a simple Jina Flow (all it needs is `jinahub://CLIPEncoder` Executor)
3. Push your `DocumentArray` to Jina Cloud with [`DocumentArray.push('your_dataset_name', show_progress=True)`](https://docarray.jina.ai/fundamentals/documentarray/serialization/?highlight=push%20pull#from-to-cloud)
### In `frontend.py`

1. Go to line 13 or 16 (look for `ttl_textual` or `ttl_embedding`)
2. Change `ttl_whatever` to the name of the token you used with `DocumentArray.push()` above
3. `rm -rf clip-as-service.db`
4. `python run_once.py`
