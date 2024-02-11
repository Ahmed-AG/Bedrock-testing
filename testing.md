## Bedrock testing:
aws bedrock list-foundation-models  --profile botdev |jq -r '.modelSummaries | .[].modelId'

aws --profile botdev bedrock-runtime invoke-model \
    --model-id amazon.titan-tg1-large \
    --body '{"prompt": "\n\nHuman: story of two dogs\n\nAssistant:", "max_tokens_to_sample" : 300}' \
    --cli-binary-format raw-in-base64-out \
    invoke-model-output.txt

    aws --profile botdev bedrock-runtime invoke-model \
    --model-id cohere.command-text-v14 \
    --body '{"prompt": "\n\nHuman: story of two dogs\n\nAssistant:"}' \
    --cli-binary-format raw-in-base64-out \
    invoke-model-output.txt 
    