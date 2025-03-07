import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "Generador de Publicaciones de Blog"
)

st.title("Generador de Publicaciones de Blog")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)

def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    Como escritor experimentado en startups y capital de riesgo,
    genera una publicación de blog de 400 palabras sobre {topic}
    
    Tu respuesta debe seguir este formato:
    Primero, imprime la publicación del blog.
    Luego, suma el número total de palabras y muestra el resultado de esta manera: Esta publicación tiene X palabras.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input("Enter topic: ")
if not openai_api_key.startswith("sk-"):
    st.warning("Enter OpenAI API Key")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)
        
