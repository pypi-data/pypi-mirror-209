import os
import sys
import numpy as np
import matplotlib.pyplot as plt

home_dir = os.path.expanduser('~')
sys.path.append(os.path.join(home_dir, "git", "soundmaker", "src"))

import soundmaker

spl, freq = soundmaker.loudness(50)

sm = soundmaker.sound(44100)

data, t = sm.gen_sine(100, 1)
data, w = sm.apply_window(0.1)
rms = sm.compute_rms()
print(rms)

#sm.scaling_db()
##rms = sm.compute_rms()
#print(rms)

sm.change_db(30)
rms = sm.compute_rms()
print(rms)

#plt.plot(t, data)
#plt.show()



#sm.export_wav(os.path.join(home_dir, "test.wav"))
