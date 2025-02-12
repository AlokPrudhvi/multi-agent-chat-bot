from agents.chat_history_agent import ChatHistoryAgent
from agents.yfinance_agent import YFinanceAgent
from agents.duckduckgo_agent import DuckDuckGoAgent
from agents.calculator_agent import CalculatorAgent

def main():
    chat_history_agent = ChatHistoryAgent()
    yfinance_agent = YFinanceAgent(chat_history_agent)
    duckduckgo_agent = DuckDuckGoAgent(chat_history_agent)
    calculator_agent = CalculatorAgent(chat_history_agent)

    # Example usage
    yfinance_agent.get_stock_data("AAPL")
    duckduckgo_agent.search("latest car models 2025")
    calculator_agent.calculate("5 + 3 * 2")

    # Print chat history
    for entry in chat_history_agent.get_history():
        print(f"{entry['agent']}: {entry['message']}")

if __name__ == "__main__":
    main()

############################
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
#############################
from agents.chat_history_agent import ChatHistoryAgent

class CalculatorAgent:
    def __init__(self, chat_history_agent: ChatHistoryAgent):
        self.chat_history_agent = chat_history_agent

    def calculate(self, expression: str):
        self.chat_history_agent.add_message("CalculatorAgent", f"Calculating: {expression}")
        try:
            result = eval(expression)
            self.chat_history_agent.add_message("CalculatorAgent", f"Result: {result}")
            return result
        except Exception as e:
            self.chat_history_agent.add_message("CalculatorAgent", f"Error: {e}")
            return str(e)
#######################
from phidata.tools import DuckDuckGoTools
from agents.chat_history_agent import ChatHistoryAgent

class DuckDuckGoAgent:
    def __init__(self, chat_history_agent: ChatHistoryAgent):
        self.chat_history_agent = chat_history_agent
        self.duckduckgo_tools = DuckDuckGoTools()

    def search(self, query: str):
        self.chat_history_agent.add_message("DuckDuckGoAgent", f"Searching for: {query}")
        results = self.duckduckgo_tools.search(query)
        self.chat_history_agent.add_message("DuckDuckGoAgent", f"Search results: {results}")
        return results
########################
from phidata.tools import YFinanceTools
from agents.chat_history_agent import ChatHistoryAgent

class YFinanceAgent:
    def __init__(self, chat_history_agent: ChatHistoryAgent):
        self.chat_history_agent = chat_history_agent
        self.yfinance_tools = YFinanceTools()

    def get_stock_data(self, ticker: str):
        self.chat_history_agent.add_message("YFinanceAgent", f"Fetching stock data for {ticker}")
        stock_data = self.yfinance_tools.get_stock_data(ticker)
        self.chat_history_agent.add_message("YFinanceAgent", f"Stock data for {ticker}: {stock_data}")
        return stock_data

    def get_market_summary(self):
        self.chat_history_agent.add_message("YFinanceAgent", "Fetching market summary")
        market_summary = self.yfinance_tools.get_market_summary()
        self.chat_history_agent.add_message("YFinanceAgent", f"Market summary: {market_summary}")
        return market_summary
##############################
chat_history_agent.py
class ChatHistoryAgent:
    def __init__(self):
        self.history = []

    def add_message(self, agent_name, message):
        self.history.append({"agent": agent_name, "message": message})

    def get_history(self):
        return self.history
#############################
