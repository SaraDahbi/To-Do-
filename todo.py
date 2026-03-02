import customtkinter as ctk
import os

# ===== Theme Configuration =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TodoApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Modern To-Do App")
        self.geometry("800x500")
        self.minsize(700, 450)

        self.tasks = []
        self.filename = "tasks.txt"

        # Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()
        self.load_tasks()
        self.update_list()

    # =========================
    # UI
    # =========================
    def create_widgets(self):

        # ===== Sidebar =====
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.pack_propagate(False)

        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="📝 To-Do App",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=30)

        self.entry = ctk.CTkEntry(
            self.sidebar,
            placeholder_text="Enter new task...",
            height=40,
            corner_radius=10
        )
        self.entry.pack(pady=10, padx=20, fill="x")

        # Add Button
        self.add_button = ctk.CTkButton(
            self.sidebar,
            text="➕ Add Task",
            fg_color="#2563EB",
            hover_color="#1E40AF",
            corner_radius=12,
            height=40,
            command=self.add_task
        )
        self.add_button.pack(pady=8, padx=20, fill="x")

        # Clear Button
        self.clear_button = ctk.CTkButton(
            self.sidebar,
            text="🗑 Clear All",
            fg_color="#374151",
            hover_color="#1F2937",
            corner_radius=12,
            height=40,
            command=self.clear_tasks
        )
        self.clear_button.pack(pady=8, padx=20, fill="x")

        # Theme Switch Button
        self.theme_button = ctk.CTkButton(
            self.sidebar,
            text="🌗 Switch Theme",
            fg_color="#7C3AED",
            hover_color="#5B21B6",
            corner_radius=12,
            height=40,
            command=self.switch_theme
        )
        self.theme_button.pack(pady=25, padx=20, fill="x")

        # Task Counter
        self.counter_label = ctk.CTkLabel(
            self.sidebar,
            text="Total Tasks: 0",
            font=("Arial", 13)
        )
        self.counter_label.pack(pady=10)

        # ===== Main Area =====
        self.main_area = ctk.CTkFrame(self, corner_radius=15)
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        self.task_list = ctk.CTkTextbox(
            self.main_area,
            corner_radius=15,
            font=("Arial", 14)
        )
        self.task_list.pack(fill="both", expand=True, padx=20, pady=20)

    # =========================
    # Functional Methods
    # =========================

    def add_task(self):
        task = self.entry.get()

        if task.strip() != "":
            self.tasks.append(task)
            self.entry.delete(0, "end")
            self.update_list()
            self.save_tasks()

    def clear_tasks(self):
        self.tasks = []
        self.update_list()
        self.save_tasks()

    def update_list(self):
        self.task_list.delete("1.0", "end")

        for i, task in enumerate(self.tasks, 1):
            self.task_list.insert("end", f"{i}. {task}\n")

        self.counter_label.configure(text=f"Total Tasks: {len(self.tasks)}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = file.read().splitlines()

    def switch_theme(self):
        current = ctk.get_appearance_mode()

        if current == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")


# ===== Run App =====
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()