import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize recognizer and microphone objects
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Adjust for ambient noise
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjusting for 0.5 seconds

        # Listen for speech with timeout and phrase time limit
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Timeout of 10 seconds, phrase limit of 5 seconds
            print("Recognizing...")
            # Use Google Speech Recognition to recognize the audio
            recognized_text = recognizer.recognize_google(audio)
            return recognized_text

        except sr.WaitTimeoutError:
            return "Timeout error: No speech detected within timeout period"
        except sr.UnknownValueError:
            return "Unable to recognize speech"
        except sr.RequestError:
            return "API unavailable"

# Test the speech recognition functionality
if __name__ == "__main__":
    print("Please say something...")
    recognized_text = recognize_speech_from_mic()
    print("You said: " + recognized_text)
