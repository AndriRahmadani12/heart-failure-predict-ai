from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()
@dataclass
class OpenAIConfig:
    api_key: str
    api_version: str
    azure_endpoint: str
    deployment_name: str

openai_config = OpenAIConfig(
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    deployment_name=os.getenv("DEPLOYMENT_NAME"),
)
