import librosa
import librosa.display
import scipy
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

if __name__ == "__main__":
    # Load the audio file
    samples, sample_rate = librosa.load('test.wav')
    print(f'# samples: {str(len(samples))}, sample rate: {str(sample_rate)}')
    # Berechnen der Audiolänge
    duration = len(samples) / sample_rate
    print(f'Audiolänge: {str(duration)}')

    # Darstellung der Amplitude über die Zeit
    plt.figure()
    librosa.display.waveshow(samples, sr=sample_rate)
    plt.xlabel('Zeit (s)')
    plt.ylabel('Amplitude (db)')
    plt.show()

    # FFT mit Hilfe von scipy
    n = len(samples)
    T= 1 / sample_rate
    yf = scipy.fft.fft(samples)
    xf = np.linspace(0.0, 1.0/ (2.0 * T), n//2)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

    # Ableitn des Spektrogramms über scipy
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    plt.specgram(samples, Fs=sample_rate, sides='default', mode='default', scale='dB')
    plt.title('Spektrogramm')
    plt.ylabel('Frequenz (Hz)')
    plt.xlabel('Zeit (s)')
    plt.show() 