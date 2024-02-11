# Sample JSON input for amazon.titan-text-express-v1 
# {
#  "modelId": "amazon.titan-text-express-v1",
#  "contentType": "application/json",
#  "accept": "application/json",
#  "body": "{\"inputText\":\"this is where you place your input text\",\"textGenerationConfig\":{\"maxTokenCount\":8192,\"stopSequences\":[],\"temperature\":0,\"topP\":1}}"
# }

import boto3 
import json
import sys

def read_file(file_path):
    file = open(file_path, "r")
    return file.readlines()

def generate_prompt(request):
    training_set = read_file("cloudwatch_instructions.txt")
    prompt = "Consider this:" + str(training_set) + "\n" + request + "->"
    return prompt

def invoke_model(request):
    session = boto3.Session(profile_name=PROFILE)
    bedrock = session.client('bedrock-runtime')

    prompt = generate_prompt(request)

    body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "temperature": 0,
            }
        }
    response = bedrock.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps(body)
    )
    response_body = json.loads(response.get('body').read())
    return response_body

PROFILE = sys.argv[1]
request = sys.argv[2] 

output  = invoke_model(request)
print(json.dumps(output,indent=4))
