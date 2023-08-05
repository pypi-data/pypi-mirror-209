import tkinter as tk

class Menu():
    def __init__(self, gui) -> None:
        #Main top menu
        mainmenu  = tk.Menu (relief=tk.RAISED, borderwidth=3)

        #Version chooser section
        version= tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label= "Version", menu = version)
        version.add_radiobutton(label="Python")
        version.add_radiobutton(label="Numpy")
        version.add_radiobutton(label="JAX")
        version.entryconfigure("Python", command=gui.change_mode_python)
        version.entryconfigure("Numpy", command=gui.change_mode_numpy)
        version.entryconfigure("JAX", command=gui.change_mode_jax)

        #Parameters chooser section
        param = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label= "Paramètres", menu=param)

        #Save configuration 
        save = tk.Menu(mainmenu, tearoff=0)
        param.add_cascade(label="Sauvegarde des données", menu=save)
        save.add_command(label="Sauvegarder la configuration", command=gui.save)

        #Visualize options
        visu= tk.Menu(mainmenu, tearoff=0)
        param.add_cascade(label="Visualisation", menu=visu)
        visu.add_separator()
        visu.add_checkbutton(label="Afficher les noyaux", onvalue=1, offvalue=0, variable=gui.visualize)
        visu.add_separator()

        #Load the menu
        gui.master.config(menu = mainmenu)
