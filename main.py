from ShazamAPI import Shazam
from recognizer import Recognizer

mp3_file_content_to_recognize = open('lostCauseRecorded.mp3', 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()

try:
	song = Recognizer.recognize(mp3_file_content_to_recognize)
	if song is not None:
		is_success = True
	else:
		is_success = False
except Exception as e:
	print(e)

print(song.full_title)