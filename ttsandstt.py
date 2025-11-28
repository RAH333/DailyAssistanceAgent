#pip install SpeechRecognition PyAudio
#    pip install gTTS


    import speech_recognition as sr

    def speech_to_text():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio) # Using Google Web Speech API
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    # Example usage:
    # transcribed_text = speech_to_text()



    from gtts import gTTS
    import os

    def text_to_speech(text, lang='en'):
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "output.mp3"
        tts.save(filename)
        os.system(f"start {filename}") # For Windows, use 'afplay' for macOS, 'xdg-open' for Linux

    # Example usage:
    # text_to_speech("Hello, I am a Python agent.")







def run_agent():
    print("Agent listening...")
    user_input = speech_to_text()

    if user_input:
        # Process user_input (e.g., use an LLM for more complex interactions)
        response = f"You said: {user_input}. I am processing your request."
        text_to_speech(response)
