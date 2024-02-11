import boto3 
import json

PROFILE="botdev"

session = boto3.Session(profile_name=PROFILE)
bedrock = session.client('bedrock-runtime')

prompt = "tell me a story"

body = {
        "prompt": prompt,
        # "temperature": 0.5,
        # "maxTokens": 200,
    }

response = bedrock.invoke_model(
    modelId="cohere.command-light-text-v14",
    body=json.dumps(body)
)
response_body = json.loads(response.get('body').read())
print(json.dumps(response_body, indent=4))

