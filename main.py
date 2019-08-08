# @Date:   2019-08-06T17:23:06-07:00
# @Last modified time: 2019-08-07T22:42:34-07:00
from __future__ import print_function
import librosa
import time
import pyaudio
import wave
import GUI
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget

class BPMThread(QThread):

    bpmSig = pyqtSignal(int)

    def __init__(self, sampleTime = None, filename = None, parent = None):
        QtCore.QThread.__init__(self, parent)
        if sampleTime is None:
            print('Error\'d out')
        self.sampleTime = sampleTime
        self.filename = filename

    def run(self):
        while(True):
            getSampleSound(self.sampleTime, self.filename)
            # time.sleep(2)
            print("BPMCheck")
            bpm = analyzeSound(self.filename, 4)
            print('passing bpm{}'.format(bpm))
            print('analyzed')
            self.bpmSig.emit(int(bpm))

def analyzeSound(filename, beatsPerMeasure):
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return tempo #returns b



def getSampleSound(x, filename):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = x
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
    frames = []

    #5 second initialization
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.startApp()

    @pyqtSlot(int)
    def setBPMMeter(self, bpm):
        self.ui.progressBar.setProperty("value", bpm)

    def startApp(self):
        beatsPerMeasure = 4
        # self.MainWindow.show()
        print("Running")
        samp = 'sampleFile.wav'
        #default 5 second initialization
        getSampleSound(5,samp)
        print('init sampled')
        sampleTime = (60/ analyzeSound(samp, 4)) * beatsPerMeasure
        self.thread = BPMThread(sampleTime, samp)
        self.thread.bpmSig.connect(self.ui.progressBar.setValue)
        self.thread.bpmSig.connect(self.ui.lcdNumber.display)
        self.thread.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
