import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Can you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def voice_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there!")

        elif "how are you" in command:
            speak("I'm doing well, thank you for asking.")

        elif "what is your name" in command:
            speak("I'm your voice assistant. You can call me Assistant.")

        elif "quit" in command or "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    voice_assistant()
