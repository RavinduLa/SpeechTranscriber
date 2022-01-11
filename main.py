import speech_recognition as sr

listener = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

    except Exception as e:
        print('Exception : ' + str(e))


take_command()
