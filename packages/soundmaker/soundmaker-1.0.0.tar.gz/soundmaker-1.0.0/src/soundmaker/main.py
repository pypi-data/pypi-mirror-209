import numpy as np

class sound:
    
    def __init__(self, fs):
        self.fs = fs
        self.data = None
        self.freq = None
        self.t = None
        self.length = None
        self.N = None
        self.rms = None
        self.peak = None
    
    def gen_sine(self, f, length):
        """
        generate sine tone.
        
        Parameters
        ----------
        f : float
            frequency (Hz).
        length : float
            length of tone in seconds.
        """
        
        self.length = length
        self.freq = f

        t = np.arange(0, length, 1/self.fs)
        data = np.sin(2*np.pi*f*t)
        
        self.N = np.squeeze(data.shape)
        
        self.data = data
        self.t = t
        
        return data, t
    
    def apply_window(self, len_transition, type = 'tukey'):
        """
        apply window function to audio data.
        
        Parameters
        ----------
        len_transision : float
            length of rise/fall in seconds. This value will be used for both rise and fall.
        type : str
            Currently, only tukey window is supported
        """
        if type == 'tukey':
            from scipy.signal.windows import tukey
            M = self.N
            alpha = len_transition / self.length * 2

            w = tukey(M = M,  alpha = alpha) 
            
        self.data = self.data * w
            
        return self.data, w

    def compute_rms(self):
        #from librosa.feature import rms
        #val = rms(y = self.data,
        #          frame_length = self.N,
        #          center = False)
        from .utils import rms
        val = rms(self.data)
        dBref = 20e-6
        self.rms = 20 * np.log10(val/dBref) # convert unit to dB

        return self.rms
    
    def scaling(self, factor):
        self.data = self.data * factor
        self.compute_rms()
        self.get_peak()
        
        return self.data
    
    def scaling_db(self, factor):
        """
        scale volume by dB.

        e.g., 
        scaling_db(30) -> +30dB
        scalind_db(-30) -> -30dB
        """
        factor_db = (10**(factor/20))
        data = self.scaling(factor_db)
        
        return data
    
    def change_db(self, val):
        rms = self.compute_rms()

        factor = val - rms
        data = self.scaling_db(factor)
        
        return data

    def get_peak(self):
        peak = np.max(np.abs(self.data))
        self.peak = peak

        return peak

    def export_wav(self, file, subtype = 'FLOAT'):
        """
        export data as wav format.

        Parameters
        ----------
        file : path-like
        subtype : subtype for soundfile.
            See soundfile.available_subtypes() for all possible values.
            Currently, only 'FLOAT' is supported by soundmaker.
        """
        import soundfile
        soundfile.write(file = file,
                        data = self.data,
                        samplerate  = self.fs,
                        subtype = subtype)


