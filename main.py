from gtts import gTTS
import os

text="Welcome to text reading project"
language="tr"
tts=gTTS(text=text,lang=language,slow=True)
tts.save("save.mp3")

file_name="save.mp3"
os.system(file_name)

