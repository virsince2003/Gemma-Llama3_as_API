from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os


prompt1 = ChatPromptTemplate.from_messages([
    "You are an A.I Asistent, and you are here to assist {topic} ",
])
prompt2 = ChatPromptTemplate.from_messages([
    "You are an A.I Asistent to help  {topic}"
])

llm1 = Ollama(
    model = "gemma:2b"
)
llm2 = Ollama(
    model = "llama3"
)

app = FastAPI(
    title="langchain Server",
    version="0.1",
    description="API Server"
)



add_routes(
    app,
    prompt1|llm1,
    path="/gemma"


)

add_routes(
    app,
    prompt2|llm2,
    path="/llama3"


)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
