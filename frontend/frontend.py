from config import clip_server, sqlite_filename
from clip_client import Client
from docarray import DocumentArray
import streamlit as st



@st.cache  # only run this once
def get_docs():
    # img_da = DocumentArray.pull("ttl-embedding", show_progress=True, local_cache=True)
    img_da = DocumentArray(
        storage="sqlite",
        config={"connection": sqlite_filename, "table_name": "ttl_embedding"},
    )

    txt_da = DocumentArray(
        storage="sqlite",
        config={"connection": sqlite_filename, "table_name": "ttl_textual"},
    )

    return [img_da, txt_da]


img_da, txt_da = get_docs()

st.header("CLIP-as-service")

st.sidebar.header("What is CLIP-as-service?")
st.sidebar.markdown("[**CLIP-as-service**](https://clip-as-service.jina.ai/) is a low-latency high-scalability service from [Jina AI](https://github.com/jina-ai/) for embedding images and text. It can be easily integrated as a microservice into [neural search](https://docs.jina.ai/get-started/neural-search/) solutions.")

st.sidebar.header("Options")
mode = st.sidebar.radio(label="Input type", options=["Text-to-image", "Image-to-text"])
server = st.sidebar.text_input(
    label="CLIP-as-service server", value=clip_server
)
c = Client(server)

if mode == "Text-to-image":
    st.markdown(
        "### Text to image\n Match text input strings to images from the [Totally-looks-like dataset](https://sites.google.com/view/totally-looks-like-dataset)"
    )
    input_text = st.text_input(label="Text input")
    txt_search_button = st.button(label="Search")
    random_button = st.button(
        label="I feel lucky (random sentence from Pride and Prejudice)"
    )

    if txt_search_button:
        vec = c.encode([input_text])
        r = img_da.find(query=vec, limit=9)

        cell1, cell2, cell3 = st.columns(3)
        cell4, cell5, cell6 = st.columns(3)
        cell7, cell8, cell9 = st.columns(3)
        all_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        for cell, doc in zip(all_cells, r):
            cell.image(doc.uri)

    if random_button:
        txt_query = txt_da.sample(1)
        st.markdown(f"### Input text\n\n{txt_query[0].text}")
        st.markdown("### Results")
        vec = c.encode([txt_query[0].text])
        r = img_da.find(query=vec, limit=9)

        cell1, cell2, cell3 = st.columns(3)
        cell4, cell5, cell6 = st.columns(3)
        cell7, cell8, cell9 = st.columns(3)
        all_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        for cell, doc in zip(all_cells, r):
            cell.image(doc.uri)


elif mode == "Image-to-text":
    st.markdown("### Image to text")
    st.markdown(
        "In this demo we'll take an input image and search for the closest matching lines from *Pride and Prejudice*"
    )
    random_button = st.button(label="I feel lucky (random image from Totally Looks Like dataset)")
    if random_button:
        query_image = img_da.sample(1)
        st.markdown("### Input image")
        st.image(query_image[0].uri)
        st.markdown("### Results")

        # vec = c.encode([query_image.uri])
        r = txt_da.find(query=query_image[0].embedding, limit=9)

        for doc in r:
            st.markdown(doc.text)
