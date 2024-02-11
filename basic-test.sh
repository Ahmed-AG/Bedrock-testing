# Testing different models
#!/bin/bash

PROFILE=botdev

INSTRUCTIONS=$(cat instructions_bash.txt)
HUMAN_QUERY="SHow me network straffic going to 8.8.8.8"
QUERY="$INSTRUCTIONS $HUMAN_QUERY"
# BODY='{"prompt": "\n\nHuman: "'"$QUERY"'"\n\nAssistant:"}'
PROMPT="tell me a story"

aws --profile $PROFILE bedrock-runtime invoke-model \
    --model-id cohere.command-light-text-v14 \
    --body "{\"prompt\": \"$PROMPT\"}"\
    --cli-binary-format raw-in-base64-out \
    invoke-model-output.txt

cat invoke-model-output.txt | jq
rm invoke-model-output.txt
