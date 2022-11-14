from email.mime import audio
from tkinter import *
# from PIL import ImageTk, Image
from tkinter import filedialog

from click import command
from debugpy import configure
import speech_recognition as sr
sr.__version__

root = Tk()
root.title('SpeechToText')  # 윈도우 창 제목
root.geometry("540x380") # 가로 * 세로
root.resizable(False,False)  # 창 크기 조절 허용x
 
def open():
    global file # 함수에서 파일 기억하도록 전역변수 선언
    file = filedialog.askopenfilename()
    print(file) 
    label1.config(text="파일 경로 : " +  file)
    # Label(root, text=root.filename).pack() # 파일경로 view

 
def label():
    r = sr.Recognizer()  # 음성인식 recognizer 인스턴스 생성

    harvard = sr.AudioFile(file)
    with harvard as source:
        audio = r.record(source)

    type(audio)  # audio data로 타입 변경시킴

    r.recognize_google(audio)  # 음성 인식하여 text로 return

    with harvard as source:
        audio1 = r.record(source, duration=4)
        audio2 = r.record(source, duration=4)
        audio3 = r.record(source, offset=4, duration=3)  # offset, 오디오 시작위치 지정

    a = r.recognize_google(audio, language='ko')

    label2.config(text="음성 인식 결과 : " + a)
    

my_btn = Button(root, text='파일열기', command=open).pack()
 
label1 = Label(root, text = " ")
label1.pack()


btn = Button(root, text = "speech to text", command=label)
btn.pack()

label2 = Label(root)
label2.pack()

root.mainloop()  # 루트에 메인 루프 선언(윈도우창이 종료 버튼 누르기 전까지 종료되지 않음)







'3.8.1'


