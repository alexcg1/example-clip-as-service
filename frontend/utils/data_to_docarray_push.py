from docarray import DocumentArray
from jina import Executor

input_file = "./data/quotes.csv"
content_field = "quote"
max_docs = 10000000 # set to high number for all
encoder = "CLIPEncoder"
docarray_pushed_name = "text-quotes-500k-embeddings"

max_docs = 10 # for testing

# Create from csv
docs = DocumentArray.from_csv(input_file, field_resolver={"quote": "text"}, size=max_docs)
print(docs[0])

# Encode
executor = Executor.from_hub(f"jinahub://{encoder}", install_requirements=True)
executor.encode(docs, parameters={})
print(docs[0].embedding)

# Push
docs.push(docarray_pushed_name, show_progress=True)
