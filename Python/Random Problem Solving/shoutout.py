from gtts import gTTS
import os
name_list = ["Rahul", "Nishant", "Harry"]
for name in name_list:
    tts = gTTS(f"Shoutout to {name}")
    tts.save("pronunciation.mp3")
    os.system("mpg321 pronunciation.mp3")
print("Pronunciation done.")
