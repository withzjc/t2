# count = 0
# while count <= 5:
#     count += 1
#     if count == 3:
#         break
#     print("Loop", count)
#
# else:
#     print("end")
# print("end a")

#当循环被break打断，就不会执行else的结果
#%占位符 S字符串，d digit %%显示百分号

import win32com.client
from gtts import gTTS
import os
import pyttsx3
text='''模仿、对口型、主题挑战等）
恋爱套路（搭讪、表白、秀恩爱）
专业技能（'''
test='测试'

#tts.sapi
import tts.sapi
voice = tts.sapi.Sapi()
voice.say("Hello")
voice.set_voice("Hongyu")
voice.say(test)
voice.set_voice("Huihui")
voice.say(test)
voice.set_voice("Kangkang")
voice.say(test)
voice.create_recording('output.wav', text)


#pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.say(text)
engine.runAndWait()

#改变声音
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   print(voice.id)
   engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_zhCN_HongyuM')
   engine.say(text)
engine.runAndWait()

#win32com
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.rate=1
speaker.Speak(text)

#gTTS
tts = gTTS(text='模仿、对口型、主题挑战等', lang='en')
tts.save("hello.mp3")

