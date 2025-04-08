## to read the ui_configfile.ini
from configparser import ConfigParser

class Config:
    def __init__(self,config_file=r".\src\langgraph\ui\ui_configfile.ini"):
        print(f"Looking for config at: {os.path.abspath(config_file)}")
        self.config = ConfigParser()
        self.config.read(config_file)
        print("Config sections:", self.config.sections())

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")
    def get_api_key(self):
        return self.config["DEFAULT"].get("GROQ_API_KEY1")
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
