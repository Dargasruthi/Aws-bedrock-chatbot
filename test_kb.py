import boto3

client = boto3.client(
    "bedrock-agent-runtime",
    region_name="us-east-1"
)

response = client.retrieve_and_generate(
    input={
        "text": "What is company policy?"
    },
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",   # ✅ THIS IS REQUIRED
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "GHL8UMPSQK",  # replace this
            "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0"
        }
    }
)

print(response["output"]["text"])