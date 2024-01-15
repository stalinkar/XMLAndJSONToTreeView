import tkinter as tk
from tkinter import ttk, filedialog
import xml.etree.ElementTree as ET


class XMLTreeViewApp:
    def __init__(self, master):
        self.master = master
        self.master.title("XML Tree View App")

        # Create TreeView widget
        self.tree = tk.ttk.Treeview(self.master)
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Add columns
        self.tree["columns"] = ("Attribute", "Value")
        self.tree.column("#0", width=200, minwidth=200, stretch=tk.NO)
        self.tree.column("Attribute", anchor=tk.W, width=150)
        self.tree.column("Value", anchor=tk.W, width=300)

        # Create headings
        self.tree.heading("#0", text="Element", anchor=tk.W)
        self.tree.heading("Attribute", text="Attribute", anchor=tk.W)
        self.tree.heading("Value", text="Value", anchor=tk.W)

        # Open file button
        open_button = tk.Button(self.master, text="Open XML File", command=self.open_file)
        open_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])

        if file_path:
            self.load_xml(file_path)

    def load_xml(self, file_path):
        # Clear existing tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Parse XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Populate TreeView
        self.populate_tree(root, "")

    def populate_tree(self, parent, parent_id):
        if parent_id == '':
            parent_id = self.tree.insert(parent_id, "end", text=parent.tag)
        for element in parent:
            item_id = self.tree.insert(parent_id, "end", text=element.tag)

            # Add attributes
            for attr, value in element.attrib.items():
                self.tree.insert(item_id, "end", values=("@" + attr, value))

            # Add text content
            if element.text and element.text.strip() != "":
                self.tree.insert(item_id, "end", values=("Text", element.text))

            # Recursively process child elements
            self.populate_tree(element, item_id)


if __name__ == "__main__":
    root = tk.Tk()
    app = XMLTreeViewApp(root)
    root.mainloop()
