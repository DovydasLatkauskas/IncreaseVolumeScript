import os
from pedalboard.io import AudioFile

def change_volume(directory_path, scale_by):
    audio_files = os.listdir(directory_path)
    for i in range (2):
        for audio_file in audio_files:
            with AudioFile(directory_path + "/" + audio_file) as f:
                audio = f.read(f.frames)
                mono = audio[i]
                # by multiplying each value in the array representing the audio by some value
                #  you scale its volume by that value
                scaled_audio = mono * scale_by
                with AudioFile("out_" + audio_file, "w", f.samplerate) as o:
                    o.write(scaled_audio)

change_volume("testFolder1", 2)
print("Done!")