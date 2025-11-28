#pip install google-genai

from google import genai
from google.genai import types
import wave
import io

# Function to save the PCM audio data to a WAV file
def save_as_wave(filename, pcm_data, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm_data)

# Initialize the client (API key will be picked up from environment variable)
client = genai.Client()

# Text prompt to convert to speech, including natural language instructions for style
prompt_text = "Say cheerfully: Have a wonderful day!"

try:
    # Generate audio content using the specific TTS model
    response = client.generate_content(
        model="gemini-2.5-flash-lite-preview-tts",
        contents=prompt_text,
        config=types.GenerateContentConfig(
            # Set the response modality to AUDIO
            response_modalities=[types.Modality.AUDIO],
            # Optional: configure the voice
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore" # Example voice name
                    )
                )
            )
        )
    )

    # The audio data is in the 'audio' field of the response
    if response.audio:
        # Get raw PCM data as bytes
        audio_bytes = response.audio.audio_bytes
        
        # Save the audio data to a file
        output_filename = "output_cheerfully.wav"
        # Default settings for the model output are 24kHz rate, 1 channel, 2 bytes width (16-bit PCM)
        save_as_wave(output_filename, audio_bytes, rate=24000) 
        print(f"Audio successfully saved to {output_filename}")
    else:
        print("No audio content generated.")

except Exception as e:
    print(f"An error occurred: {e}")
  
