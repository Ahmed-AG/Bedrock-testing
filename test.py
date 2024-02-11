import boto3 
import json

session = boto3.Session(profile_name='botdev')
bedrock = session.client('bedrock-runtime')

# models=bedrock.list_foundation_models()
# print(json.dumps(models, indent=2))

# {"prompt": "\n\nHuman: "'"$QUERY"'"\n\nAssistant:"}

prompt = "\n\nHuman: tell me a story \n\nAssistant:"

body = {
        "prompt": prompt,
        # "temperature": 0.5,
        # "maxTokens": 200,
    }

response = bedrock.invoke_model(
    modelId="cohere.command-text-v14", body=json.dumps(body)
)
print(response)
