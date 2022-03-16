# Import the required module for text 
# to speech conversion
from gtts import gTTS

tts = gTTS('olá mundo!', lang='pt')
tts.save('ola.mp3')