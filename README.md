# Social Media Performance Analysis

## Project Overview
This project is a basic analytics module designed to analyze engagement data from mock social media accounts using **Langflow** and **DataStax Astra DB**. The module allows users to input queries related to social media post types (e.g., carousel, reels, static images) and provides insights into engagement metrics such as likes, shares, and comments. The project leverages **GPT integration** to generate meaningful insights based on the data stored in **DataStax Astra DB**.

The project consists of two main files, `main.py` and `main2.py`, which achieve the same functionality but use different approaches to interact with Langflow and DataStax Astra DB. Both files are deployed on **Streamlit**, providing a user-friendly interface for analyzing social media engagement data.

---

## Key Features
- **API Integration**: `main.py` interacts with Langflow and DataStax Astra DB through API endpoints.
- **JSON-Based Flow Execution**: `main2.py` uses a JSON-based flow with predefined tweaks to customize the workflow.
- **Streamlit Interface**: Both files provide a user-friendly interface for query input and result display.

---

## File Descriptions

### 1. **`main.py`**
- **Approach**: This file interacts with Langflow and DataStax Astra DB through **API endpoints**. It uses a predefined flow ID and Langflow ID to run the workflow and fetch results.
- **Key Features**:
  - **API Integration**: The `run_flow` function sends a POST request to the Langflow API endpoint with the user's query. The API returns the analysis results, which are then displayed on the Streamlit interface.
  - **Streamlit Interface**: The interface allows users to input their query and displays the analysis results.


### 2. **`main2.py`**
- **Approach**: This file uses **Langflow's JSON-based flow execution** with predefined tweaks to customize the workflow. It directly runs the flow from a JSON file and applies specific configurations for data processing and GPT integration.
- **Key Features**:
  - **Tweaks Configuration**: The file defines a `TWEAKS` dictionary that customizes various components of the Langflow workflow, such as the input prompt, data parsing, and output formatting.
  - **Google Generative AI Integration**: The file integrates with **Google's Gemini API** for generating insights using the `gemini-1.5-pro` model.
  - **Streamlit Interface**: Similar to `main.py`, this file provides interface for query input and result display.

---

## Usage
1. **Input Query**: Enter your query related to social media post types (e.g., "Analyze carousel posts").
2. **Analyze**: Click the "Analyze" button to process the query and fetch insights.
3. **View Results**: The analysis results will be displayed on the Streamlit interface.