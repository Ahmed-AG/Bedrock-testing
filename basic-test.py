import boto3 
import json
import sys

PROFILE = sys.argv[1]
PROMPT = sys.argv[2]

session = boto3.Session(profile_name=PROFILE)
bedrock = session.client('bedrock-runtime')

body = {
        "prompt": PROMPT,
        # "temperature": 0.5,
        # "maxTokens": 200,
    }

response = bedrock.invoke_model(
    modelId="cohere.command-light-text-v14",
    body=json.dumps(body)
)
response_body = json.loads(response.get('body').read())
print(json.dumps(response_body, indent=4))

