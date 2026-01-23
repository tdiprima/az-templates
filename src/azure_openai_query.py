import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

# Validate that all required variables are set
if not all([api_key, api_endpoint, api_version, deployment_name]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=api_endpoint
)

# Make a simple query
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you tell me what 2+2 equals?"}
    ],
    max_tokens=150
)

# Print the response
print("Response from Azure OpenAI:")
print(response.choices[0].message.content)
