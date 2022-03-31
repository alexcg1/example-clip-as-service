from docarray import DocumentArray
from jina import Executor

input_file = "./data/quotes.csv"
content_field = "quote"
max_docs = 10000000 # set to high number for all
encoder = "CLIPEncoder"

# Create from csv
docs = DocumentArray.from_csv(input_file, field_resolver={"quote": "text"}, size=max_docs)

# Encode
executor = Executor.from_hub(f"jinahub://{encoder}")
executor.encode(docs)

# Push
docs.push("text-quotes-500k-embeddings", show_progress=True)
