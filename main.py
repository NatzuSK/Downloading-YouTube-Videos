import tkinter as tk
import os
from tkinter import ttk, messagebox
from pytubefix import YouTube
import threading


def download_audio():
    url = entry.get()
    format_choice = format_var.get() 
    if not url:
        messagebox.showwarning("แจ้งเตือน", "กรุณาใส่ลิงก์ YouTube")
        return


    def download_thread():
        try:
            download_folder = "downloads"
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)
            yt = YouTube(url)  
            if format_choice == "mp3":
                stream = yt.streams.filter(only_audio=True).first()
                messagebox.showinfo("กำลังดาวน์โหลด", f"กำลังดาวน์โหลดเพลง MP3: {yt.title}")
                stream.download(output_path=download_folder, filename_prefix="music_")
                messagebox.showinfo("เสร็จสิ้น", "ดาวน์โหลดเพลง MP3 เรียบร้อยแล้ว")
            elif format_choice == "mp4":
                stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
                messagebox.showinfo("กำลังดาวน์โหลด", f"กำลังดาวน์โหลดวิดีโอ MP4: {yt.title}")
                stream.download(output_path=download_folder, filename_prefix="video_")
                messagebox.showinfo("เสร็จสิ้น", "ดาวน์โหลดวิดีโอ MP4 เรียบร้อยแล้ว")
        except Exception as e:
            messagebox.showerror("เกิดข้อผิดพลาด", f"ไม่สามารถดาวน์โหลดได้\n{e}")
    

    threading.Thread(target=download_thread).start()


root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("500x300")
root.config(bg="#1e1e1e")


header_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e")
header_label.pack(pady=20)


tk.Label(root, text="ใส่ลิงก์ YouTube:", font=("Arial", 12), fg="white", bg="#1e1e1e").pack(pady=5)
entry = tk.Entry(root, width=50, font=("Arial", 12), bd=2, relief="solid", justify="center")
entry.pack(pady=10)


format_var = tk.StringVar(value="mp3") 
tk.Label(root, text="เลือกฟอร์แมต:", font=("Arial", 12), fg="white", bg="#1e1e1e").pack(pady=5)
mp3_radio = tk.Radiobutton(root, text="MP3", variable=format_var, value="mp3", font=("Arial", 12), bg="#1e1e1e", fg="white", selectcolor="green")
mp4_radio = tk.Radiobutton(root, text="MP4", variable=format_var, value="mp4", font=("Arial", 12), bg="#1e1e1e", fg="white", selectcolor="green")
mp3_radio.pack()
mp4_radio.pack()


download_button = tk.Button(root, text="ดาวน์โหลด", command=download_audio, bg="#4CAF50", fg="white", font=("Arial", 14), relief="raised", bd=2)
download_button.pack(pady=10)


progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
progress_bar.pack(pady=20)


root.mainloop()
