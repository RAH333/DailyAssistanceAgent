# @title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import asyncio
import logging
import os
import uuid

from kaggle_secrets import UserSecretsClient

#from google.adk.agents import Agent
#from google.adk.agents import LlmAgent
#from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent,LlmAgent

from google.adk.agents.base_agent import BaseAgent
from google.adk.agents.callback_context import CallbackContext

#from google.adk.apps.app import App, EventsCompactionConfig
#from google.adk.apps.app import App, ResumabilityConfig
from google.adk.apps.app import App, EventsCompactionConfig, ResumabilityConfig

from google.adk.code_executors import BuiltInCodeExecutor


from google.adk.models.google_llm import Gemini
from google.adk.models.llm_request import LlmRequest

from google.adk.memory import InMemoryMemoryService

from google.adk.plugins.base_plugin import BasePlugin
from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)  # <---- 1. Import the Plugin


#from google.adk.runners import InMemoryRunner
#from google.adk.runners import Runner
from google.adk.runners import InMemoryRunner, Runner


#from google.adk.sessions import InMemorySessionService
#from google.adk.sessions import DatabaseSessionService
from google.adk.sessions import DatabaseSessionService, InMemorySessionService

#from google.adk.tools import google_search
#from google.adk.tools import AgentTool, FunctionTool, google_search
#from google.adk.tools import google_search, AgentTool, ToolContext
#from google.adk.tools import load_memory, preload_memory

from google.adk.tools import AgentTool, FunctionTool, google_search, load_memory, preload_memory, ToolContext 
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.google_search_tool import google_search

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.tool_context import ToolContext

from google.genai import types

from mcp import StdioServerParameters
#from typing import Any, Dict
#from typing import List
from typing import Any, Dict, List


print("✅ ADK components imported successfully.")
