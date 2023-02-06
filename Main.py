from pedalboard.pedalboard.io import AudioFile

def change_volume(directory_path, scale_by):
    with AudioFile("Windows XP Startup.wav") as f:
        audio = f.read(f.frames)
        # by multiplying each value in the array representing the audio by some value
        #  you scale its volume by that value
        scaled_audio = audio * scale_by