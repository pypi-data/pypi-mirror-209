import numpy as np
from scipy.linalg import toeplitz
from scipy.interpolate import interp1d
import ResponsePrediction._tools as rt

class Autocorrelation():
    """Response prediction using the measured autocorrelation function.
    
    Procedures
    ----------

     1. Calculate the autocorrelation matrix
        - Should be calculated from the PSD using FFT
     2. Calculate the predictive vector
     3. Calculate x_hat(t+k*dT) for t+k*dT < t_max, where t_max
        is the prediction furthest ahead.
        - x_hat(t) = y(t)^T@x
        - y(t)^T = r(t)^T@R^-1
    """

    def __init__(self, x, dt, time_array, dt_pred=None, t_future=5, window="hann", nperseg=2**11):
        """
        Parameters
        ----------
        x : array_like
            The measured timeseries.
        dt : float
            The sampling time of the measured timeseries.
        time_array : array_like
            The time array of the measured timeseries.
        dt_pred : float, optional
            The sampling time of the predicted timeseries. If None, then dt_pred = dt.
        t_future : float, optional
            The time into the future to predict. Default is 5 seconds.
        window : str or tuple or array_like, optional
            Desired window to use. See scipy.signal.get_window for a list of windows and required parameters.
            If window is array_like it will be used directly as the window and its length must be nperseg.
            Defaults to a Hann window.
        nperseg : int, optional
            Length of each segment. Defaults to 2048.
        """
        self.x = x      # Timeseries (measurement)
        self.dt = dt    # Sampling time
        self.dt_pred = self._check_dt_pred(dt_pred) # Sampling time for pred.
        self.fs = 1/dt  # Sampling frequency
        self.time = time_array  # Time array
        self.t_future=t_future
        self.m = int(self.t_future/self.dt_pred)
        if x.size != time_array.size:
            raise ValueError(f"x and time_array must have same dimensions.")

        self.f, self._Sx = rt.psd(x, fs=self.fs, window=window, nperseg=nperseg)
        self.m0 = rt.moment(self.f, self.Sx, moment=0)
        self.x_m = 0
        self.x_hat = 0
        self.x_pred = np.zeros(int(self.t_future/self.dt_pred))
        self.t_pred = np.linspace(0, t_future, self.m)
        # Rxx = rt.acf(self.f, self.Sx, self.dt, 1000, self.m0)
        # self._R = rt.acf_to_acorr_matrix(Rxx)
        # self.omega = self.f*2*np.pi
        # self.x_hat = np.zeros(1)

    @property
    def Sx(self):
        """Power Spectral Denisity of the measured timeseries."""
        return self._Sx
    
    @property
    def R(self):
        """Autocorrelation matrix."""
        return self._R
    
    @property
    def Y(self):
        """Prediction matrix."""
        return self._Y
    
    @property
    def x_m(self):
        """Measurement timeseries."""
        return self._x_m
    
    @x_m.setter
    def x_m(self, x):
        self._x_m = x

    def init(self, n, dt_m):
        """Initialize the prediction algorithm with n sampling points and dt_m sampling time.
        Calls the set_R method which computes the autocorralation matrix as an nxn matrix. In 
        addition to this, the prediction vector is computed as an nxm matrix, were m is the number
        of prediction points.
        
        Parameters
        ----------
        n : int
            Number of sampling points.
        dt_m : float
            Sampling time.
        """
        self.n = n
        self.dt_m = dt_m
        self.set_R()
        self.set_prediction_vector()


    def measurement(self, t, x):
        """Set the measurement timeseries and time array. The time array is used to calculate the sampling time.
        
        Parameters
        ----------
        t : array_like
            Time array.
        x : array_like
            Timeseries.
        """
        if t[1] > t[0]:
            t = t[::-1]
            x = x[::-1]
        if x.size != self.n:
            raise ValueError(f"x has size {x.size}, which is different to n {self.n}")
        self.n = x.size
        self.x_m = x
        self.t_m = t
        self.dt_m = t[0] - t[1]
        if self.dt_m < 0:
            raise ValueError(f"Timestep is negative: {self.dt_m}")
    
    def set_R(self):
        """Calculate the autocorrelation matrix and its inverse."""
        self.Rxx = rt.acf(
            self.f,
            self.Sx,
            self.dt_m,
            self.n,
            self.m0
        )
        self._R = rt.acf_to_acorr_matrix(self.Rxx)
        self._Rinv = np.linalg.pinv(self._R)


    def y_m(self, m):
        """Compute the prediction vector for a given m."""
        N = np.arange(self.n)
        r = 1/self.m0 * np.trapz(
            self.Sx*np.cos(2*np.pi*self.f*(m*self.dt_pred + N[:, None]*self.dt_m)),
            x=self.f,
            axis=1
        )
        return r.T@self._Rinv

    def set_prediction_vector(self):
        """Copmute the prediction vector/matrix for all m."""
        Y = np.zeros((self.m, self.n))
        for m in range(self.m):
            Y[m] = self.y_m(m)
        self._Y = Y

    def predict(self):
        """Compute the predicted timeseries."""
        self.x_hat = self.Y @ self.x_m


    def _check_dt_pred(self, dt_pred):
        """Check if the prediction timestep is less than the measurement timestep."""
        if dt_pred is not None and (dt_pred < self.dt):
            print(f"Prediction timestep is less than measurement.")
            print(f"Measurement timestep = {self.dt}, pred. timestep = {dt_pred}")
            raise ValueError(f"dt: {self.dt} !< dt_pred: {dt_pred}")
        elif dt_pred is None:
            dt_pred = self.dt
        return dt_pred

    def __repr__(self) -> str:
        return f"NOT IMPLEMENTED."    


class PRWR():
    """
    Phase-Resolved wave reconstruction (PRWR).

    Use the FFT to obtain the individual wave components of a measured wave elevation. The 
    wave elevation at a location x can be estimated from these wave components by using
    the dispersion relation. The wave elevation should be estimated at a location downwave.
    Whether the prediction is possible or not can be determined from the predictable zone.

    The prediction algorithm uses the linear dispersion relation.

    Attributes
    ----------
    t_pred : array_like
        The time instances where we want to estimate the wave elevation.
    t0 : float
        The start point of measurement
    beta : float
        The wave direction. It is defined in the North-East-Down frame as waves going to.
        beta = 0.0 corresponds to waves coming from south moving north, and beta=pi the opposit.
    g : float
        Gravitational acceleration.
    rao_amp : array_like
        Array of vessel motion RAOs (m/m or rad/m) for each DOF.
    rao_phase : array_like
        Array of vessel motion RAO phase for each DOF. The prediction method use phase lag convention.
        Make sure that the input RAO phase follows the same convention.
    rao_freq : array_like
        Array of frequencies used in motion RAO computation. 
    """
    def __init__(self, t0, t_pred, wavedir: float, rao_amp, rao_phase, rao_freq, rao_headings):
        self.t0 = t0
        self.t_pred = t_pred
        self.beta = wavedir
        self.g = 9.81
        self.rao_amp = rao_amp
        self.rao_phase = rao_phase
        self.rao_freqs_rad = rao_freq
        self.rao_headings = rao_headings

    def __call__(self, wave_measurement, fs=100, x=0):
        """Calculate an estimate of the wave elevation at a point x based on a measurement
        of the wave elevation."""
        self._wave_reconstruction(wave_measurement, fs)
        return np.sum(np.real(self.amp*np.exp(1j*(self.w*self.t_pred[:, None] - self.k*np.cos(self.beta)*x))), axis=1)
    
    def motion_prediction(self, wave_measurement, dof=3, fs=100, x=0, psi=0):
        self._wave_reconstruction(wave_measurement, fs)
        _, rao_amp, rao_phase = self._set_raos(self.w, dof, psi)
        return np.sum(
            np.real(
                self.amp*rao_amp*np.exp(1j*(self.w*self.t_pred[:, None] - self.k*np.cos(self.beta)*x - rao_phase))
            ),
            axis=1
        )

    def _wave_reconstruction(self, wave_measurement, fs=100):
        # Use the FFT to obtain the phase-resolved wave
        zeta_hat = np.fft.rfft(wave_measurement)
        f_hat = np.fft.rfftfreq(n=wave_measurement.size, d=1/fs)
        self.w = f_hat*2*np.pi
        self.k = self.w**2/self.g
        self.amp = zeta_hat/zeta_hat.size

    def _set_raos(self, freqs, dof, psi):
        rao_amp_interp_freq = interp1d(
            self.rao_freqs_rad,
            self.rao_amp,
            axis=1,
            bounds_error=False,
            fill_value=(self.rao_amp[:, 0, :], 0)
        )
        rao_phase_interp_freq = interp1d(
            self.rao_freqs_rad,
            self.rao_phase,
            axis=1,
            bounds_error=False,
            fill_value=(0, self.rao_phase[:, -1, :])
        )
        new_rao_amp = rao_amp_interp_freq(freqs)
        new_rao_phase = rao_phase_interp_freq(freqs)

        rao_amp_interp_angle = interp1d(
            self.rao_headings,
            new_rao_amp,
            axis=2
        )
        rao_phase_interp_angle = interp1d(
            self.rao_headings,
            new_rao_phase,
            axis=2
        )
        rel_angle_pipi = np.mod(self.beta - psi + np.pi, 2*np.pi) - np.pi
        rel_angle_pos = np.where(rel_angle_pipi < 0, rel_angle_pipi + 2*np.pi, rel_angle_pipi)
        rao = rao_amp_interp_angle(rel_angle_pos)
        phase = rao_phase_interp_angle(rel_angle_pos)
        return freqs, rao[dof-1], phase[dof-1]