import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import datetime
import webbrowser

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='ko-KR')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again please...")
            return "None"

def process_command(command):
    if "시간" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"현재 시간은 {current_time} 입니다.")
    elif "날짜" in command:
        current_date = datetime.datetime.now().strftime("%Y년 %m월 %d일")
        speak(f"오늘 날짜는 {current_date} 입니다.")
    elif "검색" in command:
        search_query = command.split("검색")[-1].strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"{search_query}에 대한 검색 결과를 브라우저에서 열었습니다.")
    else:
        speak("죄송합니다. 그 명령을 이해하지 못했습니다.")

def main():
    speak("안녕하세요. 무엇을 도와드릴까요?")
    while True:
        query = listen().lower()
        if "종료" in query:
            speak("프로그램을 종료합니다.")
            break
        process_command(query)

if __name__ == "__main__":
    main()