import streamlit as st
from langflow.load import run_flow_from_json
import pandas as pd
import nest_asyncio
nest_asyncio.apply()

st.title("Social Media Engagement Analyzer")
st.write("Enter your query to analyze social media engagement data.")
st.markdown(
    """
    **Post Types:**
    - reel
    - podcast
    - carousel
    - static_image
    """
    )
ASTRA_DB_APPLICATION_TOKEN = st.secrets["ASTRA_DB_APPLICATION_TOKEN"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

TWEAKS = {
  "ChatInput-MTlI0": {
    "background_color": "",
    "chat_icon": "",
    "files": "",
    "input_value": "Carousels",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ParseData-adsKR": {
    "sep": "\n",
    "template": "{data}"
  },
  "Prompt-IzAU0": {
    "template": "{data}\n\nYou are given a list of social media data. Each post has a unique post_id. Your task is to:\n1. Analyze the list and ensure that only unique posts are considered.\n2. If there are multiple entries with the same post_id, ignore the duplicates and keep only one instance of each post.\n3. Focus on the unique post_id values and give direct answers to the questions based on the unique posts only.\n\nDo not include any introductory or explanatory text in your response—answer directly.\n\n{questions}\n\nAnswers:\n",
    "data": "",
    "questions": ""
  },
  "SplitText-Eu6wk": {
    "chunk_overlap": 200,
    "chunk_size": 1000,
    "separator": "\n"
  },
  "ChatOutput-NdkZi": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "AstraDB-KBXWx": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://fedad9a4-17db-4f2d-bd14-0c74e3c05195-us-east1.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "social_media_json",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": ASTRA_DB_APPLICATION_TOKEN
  },
  "File-Lt37j": {
    "concurrency_multithreading": 4,
    "path": "social_media_engagement.json",
    "silent_errors": False,
    "use_multithreading": False
  },
  "Google Generative AI Embeddings-VVdqn": {
    "api_key": GEMINI_API_KEY,
    "model_name": "models/text-embedding-004"
  },
  "AstraDBGraph-EuGDQ": {
    "api_endpoint": "https://fedad9a4-17db-4f2d-bd14-0c74e3c05195-us-east1.apps.astra.datastax.com",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "social_media_json",
    "keyspace": "",
    "metadata_incoming_links_key": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 140,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": ASTRA_DB_APPLICATION_TOKEN
  },
  "GoogleGenerativeAIModel-noVvW": {
    "google_api_key": GEMINI_API_KEY,
    "input_value": "",
    "max_output_tokens": None,
    "model": "gemini-1.5-pro",
    "n": None,
    "stream": False,
    "system_message": "You are a social media analyst. Your task is to provide insights on social media engagement data and analyze the provided data and generate meaningful insights based on the user's query. Use the data to calculate engagement metrics, compare post types, and provide actionable recommendations. Ensure your responses are clear, concise, and data-driven. Show numbers in the response but avoid showing calculations",
    "temperature": 0.1,
    "top_k": None,
    "top_p": None
  },
  "Google Generative AI Embeddings-6U7Fh": {
    "api_key": GEMINI_API_KEY,
    "model_name": "models/text-embedding-004"
  }
}

query = st.text_input("Enter your query")

if st.button("Analyze"):
    result = run_flow_from_json(flow="VectorStoreRAG.json",
                                session_id="", # provide a session id if you want to use session state
                                fallback_to_env_vars=True, # False by default
                                input_value=query,
                                tweaks=TWEAKS)
    st.markdown(result[0].outputs[0].results['message'].data['text'])
