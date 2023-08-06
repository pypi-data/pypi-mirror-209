import numpy as np

def normalize(sounds, max_peak = 1.0):
    peaks = list()
    for sound in sounds:
        peaks.append(sound.get_peak())
    peaks = np.array(peaks)
    peak_ref = np.max(peaks)
    
    factor = max_peak / peak_ref
    for sound in sounds:
        sound.scaling(factor)

def equalize_loudness(sounds, phon):
    lc, f = loudness(phon)
    
    for sound in sounds:
        freq = sound.freq
        spl, f_used = get_loudness(phon, freq)
        sound.change_db(spl)

def get_loudness(phon, f):
    lc, freq = loudness(phon)
    
    I = np.argmin(np.abs(freq - f))
    
    spl = lc[I]
    f_used = freq[I]
    
    return spl, f_used 

def loudness(phon):
    """
    derive loudness curve from phon value as described in ISO 226
    """
    
    f = np.array([20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500])
    af = np.array([0.532, 0.506, 0.48, 0.455, 0.432, 0.409, 0.387, 0.367, 0.349, 0.33, 0.315, 0.301, 0.288, 0.276, 0.267, 0.259, 0.253, 0.25, 0.246, 0.244, 0.243, 0.243, 0.243, 0.242, 0.242, 0.245, 0.254, 0.271, 0.301])
    Lu = np.array([-31.6, -27.2, -23, -19.1, -15.9, -13, -10.3, -8.1, -6.2, -4.5, -3.1, -2, -1.1, -0.4, 0, 0.3, 0.5, 0, -2.7, -4.1, -1, 1.7, 2.5, 1.2, -2.1, -7.1, -11.2, -10.7, -3.1])
    Tf = np.array([78.5, 68.7, 59.5, 51.1, 44, 37.5, 31.5, 26.5, 22.1, 17.9, 14.4, 11.4, 8.6, 6.2, 4.4, 3, 2.2, 2.4, 3.5, 1.7, -1.3, -4.2, -6, -5.4, -1.5, 6, 12.6, 13.9, 12.3])

    Ln = phon
    Af = 4.47e-3 * (10**(0.025*Ln) - 1.15) + (0.4*10**(((Tf+Lu)/10)-9))**af
    Lp = ((10/af)*np.log10(Af)) - Lu + 94
    
    spl = Lp
    freq = f

    return spl, freq

def rms(x):
    rms = np.sqrt(np.mean(x**2))
    return rms