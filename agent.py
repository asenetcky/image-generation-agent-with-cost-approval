from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from mcp import mcp_image_server
from config import retry_config

image_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="image_agent",
    instruction="Use the MCP Tool to generate images for user queries",
    tools=[mcp_image_server],
)
