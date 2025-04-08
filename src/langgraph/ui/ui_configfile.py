## to read the ui_configfile.ini
from configparser import ConfigParser
import os

class Config:
    def __init__(self,config_file="ui_configfile.ini"):
        root_dir = os.getcwd()
        print(f"root directory: {root_dir}")
        current_dir=  os.path.join("src", "langgraph", "ui", config_file)
        
        config_path = os.path.join(root_dir,current_dir)
        print(f"Looking for config at: {config_path}")
        self.config = ConfigParser()
        self.config.read(config_path)
        print("Config sections:",  self.config.read(config_path))

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
