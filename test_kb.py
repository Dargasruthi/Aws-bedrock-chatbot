import boto3

# Create Bedrock client
client = boto3.client(
    "bedrock-agent-runtime",
    region_name="us-east-1"
)

# Your Knowledge Base ID
KNOWLEDGE_BASE_ID = "7RIOJANXRR"

# Test question
query = "What is company policy?"

try:
    response = client.retrieve_and_generate(
        input={
            "text": query
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                "modelArn": "anthropic.claude-3-haiku-20240307-v1:0"
            }
        }
    )

    print("\n✅ Answer:\n")
    print(response["output"]["text"])

except Exception as e:
    print("\n❌ Error occurred:\n")
    print(e))
