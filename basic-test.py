import boto3 
import json
import sys

PROFILE = sys.argv[1]
QUERY = sys.argv[2]

def read_instructions(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return str(content)

session = boto3.Session(profile_name=PROFILE, region_name="us-east-1")
bedrock = session.client('bedrock-runtime')

instructions = read_instructions("spl_instructions.txt")
# print(instructions)

prompt = instructions + "\n" + QUERY


body = {
        "prompt": prompt,
        "temperature": 0
        # "maxTokens": 200
    }

response = bedrock.invoke_model(
    # modelId="cohere.command-light-text-v14",
    # modelId="amazon.titan-tg1-large",
    modelId="meta.llama3-8b-instruct-v1:0",
    body=json.dumps(body)
)
response_body = json.loads(response.get('body').read())
print(json.dumps(response_body, indent=4))

