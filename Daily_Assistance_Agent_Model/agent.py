from google.cloud import texttospeech
import os

# Set your Google Cloud credentials path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-key.json"

def synthesize_speech(text, output_filename="output.mp3"):
    """Synthesizes speech from the input string of text."""

    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language, voice, and gender
    # You'll need to find the available voices for Gemini TTS
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        name="en-US-Wavenet-D" # Example voice, check for Gemini specific voices
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output_filename, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_filename}"')

# --- How to use it in your agent ---
def agent_response_with_tts(user_query):
    # ... (your agent logic to generate a text response) ...
    agent_text_response = f"The answer to your question is: {user_query}" # Placeholder

    # Synthesize the agent's response to speech
    synthesize_speech(agent_text_response, "agent_response.mp3")

    # Now you would play "agent_response.mp3" to the user
    # For example, in a web app:
    # return f'<audio controls><source src="agent_response.mp3" type="audio/mpeg"></audio>'

# Example usage:
# agent_response_with_tts("What is the capital of France?")
