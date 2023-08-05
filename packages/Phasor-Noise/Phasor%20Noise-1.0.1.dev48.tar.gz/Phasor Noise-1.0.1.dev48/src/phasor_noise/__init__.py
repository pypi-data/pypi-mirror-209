def default_window():
    import tkinter as tk
    import os
    import src.phasor_noise.GUI as app

    root = tk.Tk()
    gui = app.Window(root)
    root.mainloop()
    PATH = ["src/tmp/noise_reshape.png", "src/tmp/noise.png", "src/tmp/noise_psd.png", "src/tmp/noise_psd_reshape.png",
            "src/tmp/noise_hist.png", "src/tmp/noise_hist_reshape.png"]
    for p in PATH:
        try:
            os.remove(p)
        except:
            pass
