import streamlit as st
from agents.chat_history_agent import ChatHistoryAgent
from agents.yfinance_agent import YFinanceAgent
from agents.duckduckgo_agent import DuckDuckGoAgent
from agents.calculator_agent import CalculatorAgent

# Initialize agents
chat_history_agent = ChatHistoryAgent()
yfinance_agent = YFinanceAgent(chat_history_agent)
duckduckgo_agent = DuckDuckGoAgent(chat_history_agent)
calculator_agent = CalculatorAgent(chat_history_agent)

# Streamlit UI
st.title("Multi-Agent Chatbot")

# User input
user_input = st.text_input("You: ", "")

if user_input:
    if user_input.startswith("stock "):
        ticker = user_input.split("stock ")[1]
        response = yfinance_agent.get_stock_data(ticker)
    elif user_input.startswith("search "):
        query = user_input.split("search ")[1]
        response = duckduckgo_agent.search(query)
    elif user_input.startswith("calc "):
        expression = user_input.split("calc ")[1]
        response = calculator_agent.calculate(expression)
    else:
        response = "Sorry, I didn't understand that. Please use 'stock', 'search', or 'calc' commands."

    st.write(f"Bot: {response}")

# Display chat history
st.subheader("Chat History")
for entry in chat_history_agent.get_history():
    st.write(f"{entry['agent']}: {entry['message']}")
