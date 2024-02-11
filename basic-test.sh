#!/bin/bash

PROFILE=$1
PROMPT=$2

aws --profile $PROFILE bedrock-runtime invoke-model \
    --model-id cohere.command-light-text-v14 \
    --body "{\"prompt\": \"$PROMPT\"}"\
    --cli-binary-format raw-in-base64-out \
    invoke-model-output.txt

cat invoke-model-output.txt | jq
rm invoke-model-output.txt
