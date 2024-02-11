import boto3 
import json

session = boto3.Session(profile_name='botdev')
bedrock = session.client('bedrock-runtime')

# models=bedrock.list_foundation_models()
# print(json.dumps(models, indent=2))

# {"prompt": "\n\nHuman: "'"$QUERY"'"\n\nAssistant:"}

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

