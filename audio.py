import speech_recognition as sr
import soundfile as sf 


def audio_text():
    r = sr.Recognizer()
    data, samplerate = sf.read('telega.ogg')
    sf.write('convert.wav', data, samplerate)
    with sr.AudioFile('male.wav') as source:
        audio = r.listen(source)
        print('Текст распознается...')
        try:
            text = r.recognize_google(audio, language='ru-RU')
            print( text)

        except:
            print( "Пожалуйста повторите попытку")