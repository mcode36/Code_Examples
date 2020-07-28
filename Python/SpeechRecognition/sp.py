import speech_recognition
import re
import time
import os
import pyaudio
import wave
def Play_Voice(AUDIO_FILE_NAME):
  CHUNK = 1024
  # Open wav file
  File = wave.open(AUDIO_FILE_NAME,"rb")
  # PyAudio
  p = pyaudio.PyAudio()
  # Open Stream
  stream = p.open(format = p.get_format_from_width(File.getsampwidth()),
           channels = File.getnchannels(),
           rate = File.getframerate(),
           output = True)
  # Read sound file
  data = File.readframes(CHUNK)
  # Play sound file
  while data:
    stream.write(data)
    data = File.readframes(CHUNK)
  # Stop sound file
  stream.stop_stream()
  stream.close()
  # Close PyAudio
  p.terminate()
  
def AudioFile_To_Text(AUDIO_FILE_NAME):
  r = speech_recognition.Recognizer()
  with speech_recognition.AudioFile(AUDIO_FILE_NAME) as source:
    r.adjust_for_ambient_noise(source, duration=0)
    audio = r.record(source)
    #
  Text = r.recognize_google(audio,language='en-US')
  return Text
  
# Chinese speach-to-text
def Voice_To_Text():
  r = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as source:
    print("Please speak Chinese")
  # Adjust noise level from Micphone
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
  try:
    Text = r.recognize_google(audio,language='zh-TW')
  except r.UnknownValueError:
    Text = "Can not translate"
  except sr.RequestError as e:
    Text = "Can not translate{}".format(e)
  return Text
  
# Set text file path
outfile = 'Voice.txt'
f1 = open(outfile, 'w', encoding='utf-8')

print('Play wav file:')
AUDIO_FILE_NAME = 'that-feels-really-powerful.wav'
Play_Voice(AUDIO_FILE_NAME)

print('Convert to text:')
Text = AudioFile_To_Text(AUDIO_FILE_NAME)
print(Text)
f1.write(Text+'\n')

print('Verbal Translate start:')
Text = Voice_To_Text()
print(Text)
f1.write(Text)
print('\n\nFile ' + outfile + ' has been saved')
f1.close()
