import tkinter as tk
import os
from phasor_noise.GUI import Window

def default_window():
    """
    Easy first window to manipulate the phasor noise and observe it
    """

    root = tk.Tk()
    Window(root)
    root.mainloop()
    path = ["src/tmp/noise_reshape.png", "src/tmp/noise.png", "src/tmp/noise_psd.png", "src/tmp/noise_psd_reshape.png",
            "src/tmp/noise_hist.png", "src/tmp/noise_hist_reshape.png"]
    for p in path:
        try:
            os.remove(p)
        except:
            pass
