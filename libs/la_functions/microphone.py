import sounddevice as sd
import soundfile as sf

class Microphone():
    def __init__(self, name, duration):
        """ inizializzazione (nome  e durata di registrazione) """
        self.duration = duration
        self.name = name
    def recoding(self): 
        """ registrazione + salvataggio file .wav """
        myrecording = sd.rec(int(self.duration * 10000), samplerate=10000, channels=1) 
        sd.wait()
        sf.write(self.name, myrecording, 10000)
    def play(self):
        """ play """
        data, fs = sf.read(self.name) 
        sd.play(data, fs)
        sd.wait()
    def stop(self):
        """ stop """
        sd.stop()