# Bedrock-testing

# Testing AWS Bedrock service
## Basic test

## Cloudwatch query test

```bash
% python3 cloudwatch-titan-test.py "Show me traffic going to 8.8.8.8"
{
    "inputTextTokenCount": 2499,
    "results": [
        {
            "tokenCount": 42,
            "outputText": "fields @timestamp, @logStream, srcAddr, srcPort, dstAddr, dstPort,action,packets,@message  | filter dstAddr like \"8.8.8.8\"",
            "completionReason": "FINISH"
        }
    ]
}
```