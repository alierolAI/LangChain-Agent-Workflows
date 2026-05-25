from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



load_dotenv()



model = ChatOpenAI(model="gpt-4o-mini")


 
if __name__ == '__main__':
    message=HumanMessage(content="hello my name is ali")
    response=model.invoke([message])
    print(response.content)