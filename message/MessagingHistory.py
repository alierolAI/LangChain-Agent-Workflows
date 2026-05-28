from distutils.command.config import config
from urllib import response

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from SimpleMessage import model

load_dotenv()


store={}
def get_sesion_history(session_id : str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id]= InMemoryChatMessageHistory()
    return store[session_id]

promt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Answer all questions bast of your ability"),
        MessagesPlaceholder(variable_name="messages")
    ]
)

chain= promt | model
config={"configurable" : {"session_id" : "abcde123"}}
with_message_history = RunnableWithMessageHistory(chain, get_sesion_history)




model = ChatOpenAI(model="gpt-4o-mini")


 
if __name__ == '__main__':
    for sayi in range(10):
        user_input = input(">")
        response= with_message_history.invoke(
            [
                HumanMessage(content=user_input),
            ],
            config=config,
        )
        print(response.content)

