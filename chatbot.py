from langchain.llms import OpenAI

# Initialize OpenAI model
llm = OpenAI(openai_api_key="your-api-key")

def get_ai_response(user_input):
    response = llm(user_input)
    return response
