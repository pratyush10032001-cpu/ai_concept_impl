from langserve import add_routes
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()


class TranslationRequest(BaseModel):
    lang:str
    text:str

@app.get("/hello")
def hello():
    return {"message":"Hello, How are you?"}

@app.post("/llm")
def translationLang(request:TranslationRequest):
    llm = ChatGroq(model="llama-3.1-8b-instant")

    prompt = PromptTemplate(template='Translate the text: {text} from english to {lang}',input_variables=['text','lang'])

    parser = StrOutputParser()

    chain = prompt | llm | parser

    res = chain.invoke({'text':request.text,'lang':request.lang})

    return {'translation':res}
