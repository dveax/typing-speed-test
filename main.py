import random
import time
import tkinter as tk


class TypingSpeedTest:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("800x600")
        self.window.configure(bg="lightblue")

        with open("texts.txt", "r", encoding="UTF-8") as file:
            self.texts = file.read().split()

        #---------------UI------------------
        self.label = tk.Label(self.window, text="", font=("Helvetica", 18), wraplength=700,
                              justify="center", bg="lightblue")
        self.label.pack(pady=120)

        self.label_frame = tk.Frame(self.window, bg="lightblue")
        self.label_frame.pack(pady=10)

        self.time_label = tk.Label(self.label_frame, text="", font=("Helvetica", 14), bg="lightblue")
        self.time_label.pack(padx=20, side="left")

        self.score_label = tk.Label(self.label_frame, text="", font=("Helvetica", 14), bg="lightblue")
        self.score_label.pack(padx=20, side="right")

        self.entry = tk.Entry(self.window, font=("Helvetica", 16), width=60)
        self.entry.bind("<space>", self.on_key_press)
        self.entry.pack(pady=50)

        self.button = tk.Button(self.window, text="Start", width=22, bg="black", fg="white", font=("Helvetica", 15),
                                command=self.start_test)
        self.button.pack(pady=50)

        self.score = 0

    def start_test(self):
        self.score = 0
        self.score_label.config(text="Score: 0")

        self.button.config(state=tk.DISABLED)  #Test başladığında start butonu devre dışı kalması için
        self.entry.config(state="normal") #Entryi düzenlenebilir hale getirmek için

        self.entry.focus() #Entry widgetına odaklanması için

        #Texts.txt dosyasından rastgele seçim yapmak için:
        selected_text = random.choice(self.texts).strip()
        self.display_text(selected_text) #Seçilen satırı göstermek için

        self.start_time = time.time()
        self.end_time = self.start_time + 60  # 1 dk süre

        self.timer()

    def display_text(self, text):
        self.label.config(text=text)  #Etiketi seçilen satırla güncellemek için

    def timer(self):
        current_time = time.time()
        remaining_time = self.end_time - current_time

        if remaining_time > 0:
            self.time_label.config(text=f"Time: {int(remaining_time)}")
            self.window.after(1000, self.timer)
        else:
            self.end_test()

    def end_test(self):
        self.entry.config(state="disabled")  #Entry widgetının düzenlenememesi için:
        self.time_label.config(text="Time's up!")
        remaining_time = time.time() - self.start_time
        print(f"Time elapsed: {remaining_time:.2f} seconds")

        self.button.config(state=tk.NORMAL)

    def on_key_press(self, event):
        if time.time() > self.end_time:
            return "break"  #Süre dolduğunda tuş girişini iptal etmek için

        if event.keysym == "space":
            entered_text = self.entry.get().strip()
            self.check_words(entered_text)
            self.entry.delete(0, tk.END)


##Eğer Doğruysa
    def check_words(self, entered_text):
        current_text = self.label.cget("text").strip()

        if entered_text == current_text:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        selected_text = random.choice(self.texts).strip()
        self.display_text(selected_text)


if __name__ == "__main__":
    app = TypingSpeedTest()
    app.window.mainloop()


