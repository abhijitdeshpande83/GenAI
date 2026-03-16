from graph import agent
from langchain_core.messages import HumanMessage

config = {"configurable":{"thread_id":"user-1"}}
# First turn: tell the system who you are
agent.invoke(
    {"messages": [HumanMessage(content="My name is Abhijit and I am a data scientist")]},
    config=config
)

# Second turn: ask again
response = agent.invoke(
    {"messages": [HumanMessage(content="What is my name?")]},
    config=config
)

print(response["messages"][-1].content)