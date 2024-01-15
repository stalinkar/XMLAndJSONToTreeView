import tkinter as tk
from tkinter import ttk, filedialog
import json


class JSONTreeViewApp:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Tree View App")

        # Create TreeView widget
        self.tree = ttk.Treeview(self.master)
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Add columns
        self.tree["columns"] = ("Value",)
        self.tree.column("#0", anchor=tk.W, width=300)
        self.tree.column("Value", anchor=tk.W, width=300)

        # Create heading
        self.tree.heading("#0", text="Element", anchor=tk.W)
        self.tree.heading("Value", text="Value", anchor=tk.W)

        # Open file button
        open_button = tk.Button(self.master, text="Open JSON File", command=self.open_file)
        open_button.pack(pady=10)

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if file_path:
            self.load_json(file_path)

    def load_json(self, file_path):
        # Clear existing tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Populate TreeView
        self.populate_tree("", data)

    def populate_tree(self, parent_id, data):
        if isinstance(data, dict):
            for key, value in data.items():
                item_id = self.tree.insert(parent_id, "end", text=str(key))
                self.populate_tree(item_id, value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                item_id = self.tree.insert(parent_id, "end", text=str(i))
                self.populate_tree(item_id, item)
        else:
            self.tree.insert(parent_id, "end", values=(str(data),))


if __name__ == "__main__":
    root = tk.Tk()
    app = JSONTreeViewApp(root)
    root.mainloop()
