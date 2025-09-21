from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from utils.send_email import send_email

from dotenv import load_dotenv

load_dotenv()

@tool
def send_email_tool(to: str, subject: str, body: str):
    """Send an email to the specified recipient."""
    return send_email(to, subject, body)


agent = create_react_agent(
    model="openai:gpt-4.1-mini",
    tools=[send_email_tool],  # Pass all tool functions
    prompt="You are a helpful assistant"
)

def get_response(messages):
    agent_response = agent.invoke({"messages": messages})
    
    # Return the last AI message content
    for message in reversed(agent_response["messages"]):
        if hasattr(message, 'content') and message.type == "ai":
            return message.content

if __name__ == "__main__":
    # result = agent.invoke({"messages": [("user", "Send email to manager@example.com that I am runnig late for the meeting")]})
    # print("Agent response:")
    # for message in result["messages"]:
    #     print(f"{message.type}: {message.content}")


    response = get_response([("user", "Send email to manager@example.com that I am running late for the meeting")])
    print(response)