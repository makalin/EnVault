import tkinter as tk
from tkinter import messagebox
from core.version_control import EnvVaultVersionControl
from core.encryption import EnvVaultEncryption

class EnvVaultGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EnvVault")
        self.key = None

        self.key_label = tk.Label(root, text="Encryption Key:")
        self.key_label.pack()
        self.key_entry = tk.Entry(root, show="*")
        self.key_entry.pack()

        self.save_button = tk.Button(root, text="Save Environment Variables", command=self.save_env_vars)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Environment Variables", command=self.load_env_vars)
        self.load_button.pack()

    def save_env_vars(self):
        self.key = self.key_entry.get()
        if not self.key:
            messagebox.showerror("Error", "Encryption key is required")
            return

        env_vars = {"API_KEY": "12345", "DB_PASSWORD": "s3cr3t"}
        version_control = EnvVaultVersionControl()
        version_control.save_version(env_vars, self.key)
        messagebox.showinfo("Success", "Environment variables saved.")

    def load_env_vars(self):
        self.key = self.key_entry.get()
        if not self.key:
            messagebox.showerror("Error", "Encryption key is required")
            return

        version_control = EnvVaultVersionControl()
        env_vars = version_control.load_version(".envvault/version_latest.json", self.key)
        messagebox.showinfo("Loaded Variables", str(env_vars))

if __name__ == "__main__":
    root = tk.Tk()
    app = EnvVaultGUI(root)
    root.mainloop()