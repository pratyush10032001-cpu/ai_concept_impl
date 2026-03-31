from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

domain =input("Domain: ")
query=input("Query: ")

# messages = [SystemMessage(content="""You are a helpful assistant and helping people grow there youtube channel."""),HumanMessage(content=f"as a youtube help me grow my content of selling AI arts in less than 50 words? {query}"),]
messages = ChatPromptTemplate.from_messages([("system", "You are expert in {domain} and have been helping people since last 3 years."),("human", "Help me with explaining {query} in less than 50 words?"),])

prompt = messages.invoke({"domain": domain, "query": query})


model=ChatGroq(model="llama-3.1-8b-instant")

response = model.invoke(prompt)

## Convert the response to an AIMessage
aimessage = AIMessage(content=response.content)

print(aimessage)
