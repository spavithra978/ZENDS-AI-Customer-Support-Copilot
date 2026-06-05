from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

from rag import retrieve_policy

# -----------------------------------
# Sentiment Analysis Model
# -----------------------------------

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# -----------------------------------
# Intent Classification Model
# -----------------------------------

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# -----------------------------------
# Intent Categories
# -----------------------------------

candidate_labels = [
    "Billing",
    "Technical",
    "Complaint",
    "Product Inquiry",
    "Refund",
    "Feedback"
]

# -----------------------------------
# FLAN-T5 Model
# -----------------------------------

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)

llm_model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name
)

# -----------------------------------
# Main Copilot Function
# -----------------------------------

def zends_ai_copilot(user_query):

    # -----------------------------------
    # Intent Prediction
    # -----------------------------------

    prediction = classifier(
        user_query,
        candidate_labels
    )

    intent = prediction["labels"][0]

    # -----------------------------------
    # Sentiment Prediction
    # -----------------------------------

    sentiment_result = sentiment_pipeline(
        user_query
    )[0]

    sentiment = sentiment_result["label"]

    confidence = round(
        sentiment_result["score"] * 100,
        2
    )

    # -----------------------------------
    # RAG Retrieval
    # -----------------------------------

    policy = retrieve_policy(user_query)

    # -----------------------------------
    # FLAN-T5 Prompt
    # -----------------------------------

    prompt = f"""
Customer Query:
{user_query}

Relevant Policy:
{policy}

Generate a professional telecom customer support response.
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = llm_model.generate(
        **inputs,
        max_new_tokens=100
    )

    generated_response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # -----------------------------------
    # Final Response
    # -----------------------------------

    response = f"""
🤖 ZENDS AI Copilot Response

Intent Detected: {intent}

Customer Sentiment: {sentiment}

Confidence Score: {confidence}%

AI Generated Response:

{generated_response}

Relevant Policy Information:

{policy}

Recommended Action:

Please provide the required transaction or account details for verification.

Our support team will review the issue according to company policy and assist you further.

Thank you for contacting ZENDS Customer Support.
"""

    return (
        intent,
        sentiment,
        policy,
        response
    )