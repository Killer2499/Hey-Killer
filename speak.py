from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile


def say(text, lang='es'):
    try:
        tts = gTTS(text=text, lang=lang)
        mixer.init()
        sf = TemporaryFile()
        tts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()
    except Exception:
        raise

