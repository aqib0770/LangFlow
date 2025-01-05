import streamlit as st
import requests
import json

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "c24c2c71-45ba-422b-a73f-2a1fc3c09c49"
FLOW_ID = "ba831f05-a4b2-4505-a112-d228f14ab683"
APPLICATION_TOKEN = st.secrets['ASTRA_DB_APPLICATION_TOKEN']

# Function to run the flow
def run_flow(message: str, endpoint: str = FLOW_ID, tweaks: dict = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    if tweaks:
        payload["tweaks"] = tweaks
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Streamlit App
def main():
    st.title("Social Media Engagement Analyzer")
    st.write("Enter your query to analyze social media engagement data.")
    st.markdown(
        """
    **Approach**: This app uses **API endpoints** to interact with Langflow and DataStax Astra DB."""
    )
    st.markdown(
    """
    **Post Types:**
    - reel
    - podcast
    - carousel
    - static_image
    """
    )

    # Input from user
    user_input = st.text_input("Enter your query:")

    if st.button("Analyze"):
        if user_input:
            with st.spinner("Analyzing data..."):
                try:
                    # Call the API
                    response = run_flow(message=user_input)
                    st.markdown(response['outputs'][0]['outputs'][0]['results']['message']['text'])
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()