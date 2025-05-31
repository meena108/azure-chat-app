import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Load values from .env
        load_dotenv()
        project_connection = os.getenv("PROJECT_ENDPOINT")
        api_key = os.getenv("API_KEY")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Connect to Azure AI Foundry project using API key
        projectClient = AIProjectClient(
            credential=AzureKeyCredential(api_key),
            endpoint=project_connection,
        )

        # Create chat client
        chat = projectClient.inference.get_chat_completions_client()

        # System prompt
        prompt = [SystemMessage("You are a helpful AI assistant that answers questions.")]

        # Chat loop
        while True:
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if not input_text:
                print("Please enter a prompt.")
                continue

            prompt.append(UserMessage(input_text))

            # Get response
            response = chat.complete(
                model=model_deployment,
                messages=prompt
            )
            completion = response.choices[0].message.content
            print(completion)

            prompt.append(AssistantMessage(completion))

    except Exception as ex:
        print("Error:", ex)

if __name__ == '__main__':
    main()
