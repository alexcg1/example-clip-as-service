FROM jinaai/jina:3.2.9-py39-standard

COPY . /workspace
WORKDIR /workspace

RUN pip install -r requirements.txt

EXPOSE 8502

ENTRYPOINT ["streamlit", "run"]
CMD ["frontend.py"]
