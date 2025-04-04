## to read the ui_configfile.ini
from configparser import ConfigParser

class Config:
    def __init__(self,config_file=r".\src\langgraph\ui\ui_configfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    def get_usercase_option(self):
        print(self.config["DEFAULT"].get("USECASE_OPTIONS").split(","))
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")
    def get_api_key(self):
        return self.config["DEFAULT"].get("GROQ_API_KEY1")
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
