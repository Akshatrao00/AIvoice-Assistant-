import datetime

def speak(text):
    print("AI 🤖:", text)

def listen():
    return input("You 👤: ").lower()

def process(query):
    if "hello" in query:
        speak("Hello Parth! How can I assist you?")
    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif "date" in query:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")
    elif "your name" in query:
        speak("I am your AI Assistant. You can call me ParthBot!")
    elif "bye" in query or "exit" in query or "stop" in query:
        speak("Goodbye Parth! Have a divine day ahead!")
        return False
    else:
        speak("Sorry, I am still learning. Try something else.")
    return True

def main():
    speak("Namaste Parth! I'm your simple AI assistant.")
    running = True
    while running:
        query = listen()
        if query:
            running = process(query)

if __name__ == "__main__":
    main()
