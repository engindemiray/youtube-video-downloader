import customtkinter as ctk
from tkinter import filedialog, messagebox
from downloader.video_downloader import download_video
from downloader.audio_downloader import download_audio
import threading
import time
from ui.texts import texts

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def run_gui():
    root = ctk.CTk()
    root.title("🎬 YouTube Downloader (WebM/MP3)")
    root.geometry("500x450")
    root.resizable(False, False)

    start_time = None  # Download start time

    # ---- LANGUAGE SELECTION ----
    language_var = ctk.StringVar(value="Türkçe")
    language_combo = ctk.CTkComboBox(
        root, values=["Türkçe", "English"], variable=language_var, width=100
    )
    language_combo.place(relx=0.98, rely=0.02, anchor="ne")

    # ---- URL INPUT ----
    url_label = ctk.CTkLabel(root, text=texts[language_var.get()]["url"], font=("Arial", 14))
    url_label.pack(pady=(40, 5))
    url_entry = ctk.CTkEntry(root, width=400)
    url_entry.pack(pady=(0, 10))

    # ---- VIDEO/AUDIO FRAME ----
    video_frame = ctk.CTkFrame(root, fg_color=root._fg_color, corner_radius=0)
    video_frame.pack(pady=5, padx=0, fill="x")

    # ---- MODE SELECTION ----
    download_mode = ctk.StringVar(value=texts[language_var.get()]["video"])
    mode_label = ctk.CTkLabel(video_frame, text=texts[language_var.get()]["mode"], font=("Arial", 12))
    mode_label.pack(pady=5)
    download_mode_combobox = ctk.CTkComboBox(
        video_frame, values=[texts["Türkçe"]["video"], texts["Türkçe"]["audio"]],
        variable=download_mode
    )
    download_mode_combobox.pack()

    # ---- RESOLUTION SELECTION ----
    resolution_var = ctk.StringVar(value="720p")
    resolution_label = ctk.CTkLabel(video_frame, text=texts[language_var.get()]["resolution"], font=("Arial", 12))
    resolution_combobox = ctk.CTkComboBox(video_frame, values=["360p", "720p", "1080p"], variable=resolution_var)
    resolution_label.pack(pady=5)
    resolution_combobox.pack()

    # ---- DOWNLOAD BUTTON ----
    download_button = ctk.CTkButton(root, text=texts[language_var.get()]["download"], width=150)
    download_button.pack(pady=20)

    # ---- NEW DOWNLOAD BUTTON ----
    def reset_fields():
        url_entry.delete(0, "end")
        progress_bar.set(0)
        progress_label.configure(text="0%")
        remaining_label.configure(text="")
        download_mode.set(texts[language_var.get()]["video"])
        resolution_var.set("720p")
        reset_button.pack_forget()

    reset_button = ctk.CTkButton(root, text=texts[language_var.get()]["new_download"], command=reset_fields)
    reset_button.pack_forget()

    # ---- PROGRESS BAR ----
    progress_bar = ctk.CTkProgressBar(root, width=400)
    progress_bar.set(0)
    progress_bar.pack(pady=10)
    progress_label = ctk.CTkLabel(root, text="0%", font=("Arial", 12))
    progress_label.pack(pady=5)

    # ---- REMAINING TIME AND SPEED LABEL ----
    remaining_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
    remaining_label.pack(pady=5)

    # ---- LANGUAGE CHANGE ----
    def on_language_change(*args):
        lang = language_var.get()
        if lang not in texts:
            return
        url_label.configure(text=texts[lang]["url"])
        mode_label.configure(text=texts[lang]["mode"])
        resolution_label.configure(text=texts[lang]["resolution"])
        download_button.configure(text=texts[lang]["download"])
        reset_button.configure(text=texts[lang]["new_download"])

        mode_values = [texts[lang]["video"], texts[lang]["audio"]]
        download_mode_combobox.configure(values=mode_values)
        if download_mode.get() not in mode_values:
            download_mode.set(mode_values[0])

    language_var.trace_add("write", on_language_change)

    # ---- MODE CHANGE ----
    def on_mode_change(*args):
        if download_mode.get() == texts[language_var.get()]["video"]:
            resolution_label.pack(pady=5)
            resolution_combobox.pack()
        else:
            resolution_label.pack_forget()
            resolution_combobox.pack_forget()

    download_mode.trace_add("write", on_mode_change)

    # ---- START DOWNLOAD ----
    def start_download():
        nonlocal start_time
        url = url_entry.get().strip()
        path = filedialog.askdirectory()
        mode = download_mode.get()
        resolution = resolution_var.get()
        lang = language_var.get()

        if not url or not path:
            messagebox.showwarning(texts[lang]["warning"], texts[lang]["warning"])
            return

        start_time = time.time()
        threading.Thread(target=download_thread, args=(url, path, mode, resolution), daemon=True).start()

    # ---- DOWNLOAD THREAD ----
    def download_thread(url, path, mode, resolution):
        try:
            lang = language_var.get()
            progress_bar.set(0)
            progress_label.configure(text="0%")
            remaining_label.configure(text="")
            if mode == texts[lang]["video"]:
                download_video(url, path, resolution, progress_callback)
            else:
                download_audio(url, path, progress_callback)

            progress_bar.set(1)
            progress_label.configure(text="100%")
            remaining_label.configure(text="")
            progress_label.configure(text="✅ " + texts[lang]["done"])
            messagebox.showinfo(texts[lang]["done"], "✅ " + texts[lang]["done"])

            reset_button.pack(pady=0)
        except Exception as e:
            progress_bar.set(0)
            progress_label.configure(text="0%")
            remaining_label.configure(text="")
            messagebox.showerror("Error", str(e))

    # ---- PROGRESS CALLBACK ----
    def progress_callback(percent, downloaded_bytes=None, total_bytes=None):
        progress_bar.set(percent / 100)
        progress_label.configure(text=f"{int(percent)}%")
        
        if downloaded_bytes and total_bytes:
            elapsed_time = time.time() - start_time
            speed = downloaded_bytes / elapsed_time if elapsed_time > 0 else 0
            remaining_bytes = total_bytes - downloaded_bytes
            remaining_time = remaining_bytes / speed if speed > 0 else 0
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            remaining_label.configure(text=f"Time left: {minutes:02d}:{seconds:02d} | Speed: {int(speed/1024)} KB/s")

    download_button.configure(command=start_download)

    root.mainloop()