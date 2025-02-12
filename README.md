# Multi-Agent Chatbot

This project implements a multi-agent chatbot using the PhiData framework. The chatbot includes agents for fetching stock data, performing web searches, and calculating expressions. It also maintains a chat history of all interactions.

## Setup

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```sh
    python src/main.py
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run src/streamlit_app.py
    ```

## Agents

- **YFinanceAgent**: Fetches stock data using PhiData's YFinanceTools.
- **DuckDuckGoAgent**: Performs web searches using PhiData's DuckDuckGoTools.
- **CalculatorAgent**: Evaluates mathematical expressions.
- **ChatHistoryAgent**: Maintains a history of all interactions between agents.
