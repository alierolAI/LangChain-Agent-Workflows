from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

system_promt="Translate the following from {language}"
promt_template = ChatPromptTemplate.from_messages([

    ("system", system_promt),("user","{text}")
  ]
)

parser = StrOutputParser()
chain=promt_template | model | parser

app = FastAPI(
    title="Translator App",
    version="1.0",
    description="Translation Chat Bot",
)

add_routes(
    app,
    chain,
    path="/chain"

)

if __name__ == "__main__":
   import uvicorn
   uvicorn.run(app, host="localhost", port=8000)


