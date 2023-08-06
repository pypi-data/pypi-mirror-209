import os
import sys
import numpy as np
import matplotlib.pyplot as plt

home_dir = os.path.expanduser('~')
sys.path.append(os.path.join(home_dir, "git", "soundmaker", "src"))

import soundmaker

spl, _ = soundmaker.loudness(40)
print(spl)

freqs = [100, 1000, 2000]

sounds = list()
for idx, freq in enumerate(freqs):
    sounds.append(soundmaker.sound(44100))
    sounds[idx].gen_sine(freq, 1)

soundmaker.equalize_loudness(sounds, 50)

for sound in sounds:
    print(sound.compute_rms())
    
print("===")
    
for sound in sounds:
    print(sound.get_peak())

soundmaker.normalize(sounds)
print("===")
for sound in sounds:
    print(sound.get_peak())