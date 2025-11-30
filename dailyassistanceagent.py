#!export GOOGLE_GENAI_USE_VERTEXAI=FALSE && adk create daily-assistant-agent-model --model gemini-2.5-flash-lite --api_key GOOGLE_API_KEY
!export GOOGLE_GENAI_USE_VERTEXAI=FALSE && adk create daily-assistant-agent-model --model gemini-2.5-flash-lite --api_key 
#!export GOOGLE_GENAI_USE_VERTEXAI=FALSE && adk create daily-assistant-agent-model --model gemini-2.5-flash-lite --api_key=$GOOGLE_API_KEY
#!export GOOGLE_GENAI_USE_VERTEXAI=FALSE && adk create daily-assistant-agent-model --model gemini-2.5-flash-lite --api_key=$
#!adk create daily-assistant-agent --model gemini-2.5-flash-lite --api_key=$GOOGLE_API_KEY
#!cd daily-assistant-agent-model
%%writefile daily-assistant-agent-model/agent.py
