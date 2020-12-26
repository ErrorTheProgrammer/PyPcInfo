#Please note this is designed for windows machines, Linux may be coming soon...
#It may work, but I don't guarantee it
import platform,sys,os
import tkinter as tk
VER = '0.0.1'
print("="*40, "PyPcInfo", "="*40)
uname = platform.uname()
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title(f"PYPCINFO V {VER}")
        self.master['bg'] = 'gray'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.txt = tk.Text(self.master)
        self.txt.insert(tk.INSERT, "PYPCINFO V")
        self.txt.insert(tk.END, VER)
        self.txt.insert(tk.INSERT, f"\nHello ")
        self.txt.insert(tk.END, f"{os.getlogin()}!")
        self.txt.insert(tk.INSERT, f"\nSystem : ")
        self.txt.insert(tk.END, uname.system)
        self.txt.insert(tk.INSERT, f"\nName : ")
        self.txt.insert(tk.END, uname.node)
        self.txt.insert(tk.INSERT, f"\nRelease : ")
        self.txt.insert(tk.END, uname.release)
        self.txt.insert(tk.INSERT, f"\nVersion : ")
        self.txt.insert(tk.END, uname.version)
        self.txt.insert(tk.INSERT, f"\nMachine : ")
        self.txt.insert(tk.END, uname.machine)
        self.txt.insert(tk.INSERT, f"\nProcessor(s) : ")
        self.txt.insert(tk.END, uname.processor)
        self.txt.insert(tk.INSERT, f"\nCPU count : ")
        self.txt.insert(tk.END, os.cpu_count())
        self.txt.insert(tk.INSERT, f"\nComputer type : ")
        if sys.getwindowsversion().product_type == 1:
            PCTYPE="Workstation"
        elif sys.getwindowsversion().product_type == 2:
            PCTYPE="Domain controller"
        elif sys.getwindowsversion().product_type == 3:
            PCTYPE="Server"
        else:
            PCTYPE="Not Available"
        self.txt.insert(tk.END, PCTYPE)
        self.txt.insert(tk.INSERT, f"\nEdition : ")
        self.txt.insert(tk.END, platform.win32_edition())
        self.txt['bg'] = "gray"
        self.txt['state'] = tk.DISABLED
        self.txt.pack()
root = tk.Tk()
app = Application(master=root)
app.mainloop()
