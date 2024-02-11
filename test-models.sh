# Testing different models
#!/bin/bash

PROFILE=botdev

INSTRUCTIONS=$(cat instructions_bash.txt)
HUMAN_QUERY="SHow me network straffic going to 8.8.8.8"
QUERY="$INSTRUCTIONS $HUMAN_QUERY"
# BODY='{"prompt": "\n\nHuman: "'"$QUERY"'"\n\nAssistant:"}'
BODY='{\"prompt\": \"Human: tell me a story\n\nAssistant:\"}'

aws --profile $PROFILE bedrock-runtime invoke-model \
    --model-id "amazon.titan-text-lite-v1:0:4k" \
    --body "{\"prompt\": \"Human: $HUMAN_QUERY\n\nAssistant:\"}"\
    --cli-binary-format raw-in-base64-out \
    invoke-model-output.txt

cat invoke-model-output.txt | jq
rm invoke-model-output.txt
