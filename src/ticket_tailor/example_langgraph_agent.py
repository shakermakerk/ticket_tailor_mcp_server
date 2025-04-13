# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from ticket_tailor_funcs import tt_mcp

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import asyncio

# Define a strong system message to prevent hallucination
SYSTEM_MESSAGE = """You are an assistant that helps with Ticket Tailor data.
IMPORTANT: Only provide information that you can verify using the available tools. 
Do NOT make up or hallucinate any information.
If you don't know something or can't find it with the tools, admit that you don't know.
Always verify data using the ticket_tailor tools before providing an answer.
When asked about orders or events, you MUST use the appropriate tool to fetch the actual data.
Make sure.
always use the get_current_datetime tool to get the current date and time before you use any other tools.
"""

model = ChatOpenAI(model="gpt-4o-mini")

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your ticket_tailor_funcs.py file
    args=["/Users/chriswood/git/ai_projects_folder/ticket_tailor_mcp_server/src/ticket_tailor/ticket_tailor_funcs.py"],
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent with the system message
            agent = create_react_agent(model, tools)
            question = "what orders have we recevied today on ticket tailor?"
            
            # Format the messages properly as a list of message objects
            messages = [HumanMessage(content=question), SystemMessage(content=SYSTEM_MESSAGE)]
            
            # Invoke the agent with properly formatted messages
            agent_response = await agent.ainvoke({"messages": messages})
            
            # Print only the content of the final AI message
            print("AI Response:")
            print(agent_response['messages'][-1].content)
            print("--------------------------------")
            # print("Full response object:")
            # print(agent_response)

if __name__ == "__main__":
    asyncio.run(main())