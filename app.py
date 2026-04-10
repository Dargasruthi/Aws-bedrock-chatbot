import streamlit as st
import boto3

st.title("📚 AI Knowledge Base Chatbot")

client = boto3.client(
    "bedrock-agent-runtime",
    region_name="us-east-1"
)

# IMPORTANT: replace this with your real Knowledge Base ID
KNOWLEDGE_BASE_ID = "GHL8UMPSQK"

# Safe working model (NO PAYMENT ISSUE)
MODEL_ARN = "amazon.titan-text-express-v1"

user_input = st.text_input("Ask your question:")

if st.button("Get Answer"):

    if user_input:

        response = client.retrieve_and_generate(
    input={
        "text": user_input
    },
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KNOWLEDGE_BASE_ID,
            "modelArn": "anthropic.claude-3-haiku-20240307-v1:0"
        }
    }
)

        answer = response["output"]["text"]

        st.subheader("Answer:")
        st.write(answer)

    else:
        st.warning("Please enter a question")