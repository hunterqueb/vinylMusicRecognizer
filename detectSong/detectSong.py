from ShazamAPI import Shazam
from recognizer import Recognizer
import pyaudio
import wave

def detectSongFun():

    # audio recording section

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 7
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('\n * Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('\n Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    # 

    file_content_to_recognize = open('output.wav', 'rb').read()

    shazam = Shazam(file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()

    try:
        song = Recognizer.recognize(file_content_to_recognize)
        if song is not None:
            is_success = True
        else:
            is_success = False
    except Exception as e:
        print(e)

    try:
        print(song.full_title)
    except Exception:
        print("song not detected")
    return song.full_title

def detectSongFunDebug():
    print("song detected")
    return "Redbone - Childish Gambino"
