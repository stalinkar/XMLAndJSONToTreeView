import tkinter as tk
from json_treeview import JSONTreeViewApp
from xml_treeview import XMLTreeViewApp


class XMLAndJSONToTreeView:
    def __init__(self, master):
        self.master = master
        self.master.title("XML And JSON To TreeView")

        # Create buttons
        self.button1 = tk.Button(self.master, text="XML To Tree View", command=lambda: button_clicked(1))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.master, text="JSON To Tree View", command=lambda: button_clicked(2))
        self.button2.pack(pady=10)


def button_clicked(value):
    master = tk.Tk()
    if value == 1:
        XMLTreeViewApp(master)
    else:
        JSONTreeViewApp(master)


if __name__ == "__main__":
    root = tk.Tk()
    app = XMLAndJSONToTreeView(root)
    new_width = 350
    new_height = 100
    root.geometry(f"{new_width}x{new_height}")
    root.mainloop()
