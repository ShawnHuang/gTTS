import time
from gtts import gTTS
from pygame import mixer
import tempfile
#pip3 install gTTS --upgrade
#pip3 install gTTS-token --upgrade

def speak(sentence, lang, loop=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        print(fp.name)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(loop)

speak('哈囉世界', 'zh-tw')
speak('Hello World!', 'en')
time.sleep(3)
