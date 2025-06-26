import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, ttk
import requests
import os

GITHUB_API = "https://api.github.com"

class GitHubArchiverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Archiver")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")  # Maximize window

        self.token = ''
        self.repos = []

        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill="both", expand=True)

        self.login_button = ttk.Button(self.frame, text="Login to GitHub", command=self.authenticate)
        self.login_button.pack(pady=5)
        
        self.download_button = ttk.Button(self.frame, text="Download Selected Repos", command=self.download_selected)
        self.download_button.pack(pady=5)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
        self.repo_listbox = tk.Listbox(self.frame, selectmode="multiple", width=80, height=20, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.repo_listbox.yview)
        self.repo_listbox.pack(side="left", fill="both", expand=True, pady=5)
        self.scrollbar.pack(side="right", fill="y")

    def authenticate(self):
        print("Starting authentication...")
        self.token = simpledialog.askstring("GitHub Token", "Enter your GitHub Personal Access Token:\nYou can create one at: https://github.com/settings/tokens", show='*')
        if not self.token:
            print("Authentication canceled.")
            return

        headers = {"Authorization": f"token {self.token}"}
        self.repos.clear()
        self.repo_listbox.delete(0, tk.END)

        page = 1
        print("Fetching repositories...")
        while True:
            print(f"Fetching page {page} of repositories...")
            resp = requests.get(f"{GITHUB_API}/user/repos?per_page=100&page={page}", headers=headers)
            if resp.status_code != 200:
                messagebox.showerror("Error", f"Failed to fetch repos: {resp.text}")
                print(f"Error fetching repositories: {resp.text}")
                return
            page_data = resp.json()
            if not page_data:
                print("No more repositories to fetch.")
                break
            for repo in page_data:
                full_name = repo['full_name']
                self.repos.append(full_name)
                self.repo_listbox.insert(tk.END, full_name)
                print(f"Added repository: {full_name}")
            page += 1
        print("Repository fetching complete.")

    def download_selected(self):
        selection = self.repo_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select at least one repository.")
            return

        output_dir = filedialog.askdirectory(title="Select Download Directory")
        if not output_dir:
            return

        headers = {"Authorization": f"token {self.token}"}
        for index in selection:
            repo_full_name = self.repos[index]
            branches_url = f"{GITHUB_API}/repos/{repo_full_name}/branches"
            r = requests.get(branches_url, headers=headers)
            if r.status_code != 200:
                messagebox.showerror("Error", f"Failed to get branches for {repo_full_name}")
                continue
            branches = r.json()
            for branch in branches:
                branch_name = branch['name']
                zip_url = f"https://api.github.com/repos/{repo_full_name}/zipball/{branch_name}"
                zip_resp = requests.get(zip_url, headers=headers, stream=True)
                if zip_resp.status_code == 200:
                    # Ensure the directory exists
                    filename = f"{repo_full_name.replace('/', '_')}_{branch_name}.zip"
                    filepath = os.path.join(output_dir, filename)
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    with open(filepath, 'wb') as f:
                        for chunk in zip_resp.iter_content(chunk_size=128):
                            f.write(chunk)
                else:
                    messagebox.showerror("Download Error", f"Failed to download {repo_full_name}@{branch_name}")

        messagebox.showinfo("Done", "Download complete.")

if __name__ == "__main__":
    print("Starting GitHub Repository Archiver...")
    root = tk.Tk()
    app = GitHubArchiverApp(root)
    root.mainloop()
    print("Application closed.")
