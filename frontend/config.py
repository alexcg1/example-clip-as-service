import os
sources = ["ttl-textual", "ttl-embedding"]  # text  # images

clip_server = os.getenv("SERVER", "grpc://examples.jina.ai:51000")
sqlite_filename = "clip-as-service.db"
table_name = "clip_as_service"
data_sources = ["ttl-embedding", "ttl-textual"]
