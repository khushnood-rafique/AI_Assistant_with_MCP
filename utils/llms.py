from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama

load_dotenv()

class LLMModel():
    def __init__(self, llm_model):
        if not llm_model:
            raise ValueError('Model not defined')
        
        self.llm_model = llm_model

    def get_model(self):
        return self.llm_model
    
if __name__ == "__main__":
    llm = LLMModel(llm_model=ChatOllama(
            model="gemma3:12b",                    
            base_url="http://127.0.0.1:11434"
        ))
    llm_model = llm.get_model()
    print(llm_model.invoke('Hi'))


