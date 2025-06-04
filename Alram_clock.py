import tkinter as tk
from tkinter import messagebox
import time
import threading

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Alarm Clock")
        self.root.geometry("400x200")
        self.root.configure(bg="#282c34")

        self.current_time_label = tk.Label(root, font=("Arial", 48), fg="#61dafb", bg="#282c34")
        self.current_time_label.pack(pady=10)

        self.alarm_time_var = tk.StringVar()

        alarm_frame = tk.Frame(root, bg="#282c34")
        alarm_frame.pack(pady=10)

        tk.Label(alarm_frame, text="Set Alarm (HH:MM:SS):", font=("Arial", 14), fg="white", bg="#282c34").grid(row=0, column=0, padx=5)
        self.alarm_entry = tk.Entry(alarm_frame, textvariable=self.alarm_time_var, font=("Arial", 14), width=10)
        self.alarm_entry.grid(row=0, column=1, padx=5)

        self.set_alarm_button = tk.Button(alarm_frame, text="Set Alarm", font=("Arial", 14), command=self.set_alarm, bg="#61dafb", fg="#282c34", activebackground="#21a1f1", activeforeground="white")
        self.set_alarm_button.grid(row=0, column=2, padx=5)

        self.alarm_set_label = tk.Label(root, text="", font=("Arial", 14), fg="lightgreen", bg="#282c34")
        self.alarm_set_label.pack()

        self.alarm_time = None
        self.alarm_thread = None
        self.alarm_active = False

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.config(text=current_time)
        if self.alarm_active and current_time == self.alarm_time:
            self.ring_alarm()
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        alarm_time = self.alarm_time_var.get()
        if self.validate_time_format(alarm_time):
            self.alarm_time = alarm_time
            self.alarm_active = True
            self.alarm_set_label.config(text=f"Alarm set for {self.alarm_time}")
        else:
            messagebox.showerror("Invalid Time Format", "Please enter time in HH:MM:SS format")
            self.alarm_set_label.config(text="")
            self.alarm_active = False

    def validate_time_format(self, time_str):
        try:
            time.strptime(time_str, "%H:%M:%S")
            return True
        except ValueError:
            return False

    def ring_alarm(self):
        self.alarm_active = False
        messagebox.showinfo("Alarm", "Wake Up! Alarm Time Reached.")
        self.alarm_set_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()




