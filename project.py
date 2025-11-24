import tkinter as tk
import random
class PopBalloonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pop The Balloons Game")
        self.root.geometry("600x500")
        
        self.score = 0
        self.time_left = 20
        self.game_running = False
        
        self.start_frame = tk.Frame(root)
        self.start_frame.pack(expand=True)

        tk.Label(self.start_frame, text="POP THE BALLOONS!", font=("Impact", 34)).pack(pady=20)
        
        tk.Button(self.start_frame, text="Start Game", font=("Impact", 18),
                  command=self.start_game).pack(pady=10)
        tk.Button(self.start_frame, text="Quit", font=("Impact", 18),
                  command=root.quit).pack()

        self.game_frame = tk.Frame(root)

        self.score_label = tk.Label(self.game_frame, text="Score: 0", font=("Arial", 16))
        self.score_label.grid(row=0, column=0, padx=10)

        self.timer_label = tk.Label(self.game_frame, text="Time: 20", font=("Arial", 16))
        self.timer_label.grid(row=0, column=1, padx=10)

        self.pause_button = tk.Button(self.game_frame, text="Pause", font=("Arial", 14),
                                      command=self.pause_resume_game)
        self.pause_button.grid(row=0, column=2, padx=10)

        self.canvas = tk.Canvas(self.game_frame, width=550, height=400, bg="green")
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        self.end_frame = tk.Frame(root)

    def start_game(self):
        self.start_frame.pack_forget()
        self.end_frame.pack_forget()

        self.score = 0
        self.time_left = 20
        self.game_running = True
        
        self.score_label.config(text="Score: 0")
        self.timer_label.config(text="Time: 20")
        self.pause_button.config(text="Pause")

        self.game_frame.pack()
        self.spawn_balloon()
        self.update_timer()

    def pause_resume_game(self):
        if self.game_running:
            self.game_running = False
            self.pause_button.config(text="Resume")
        else:
            self.game_running = True
            self.pause_button.config(text="Pause")
            self.update_timer()
            self.spawn_balloon()

    def spawn_balloon(self):
        if not self.game_running:
            return
        if self.time_left <= 0:
            return
        
        x = random.randint(50, 500)
        y = random.randint(50, 350)
        radius = random.randint(20, 40)

        balloon = self.canvas.create_oval(
            x-radius, y-radius, x+radius, y+radius,
            fill=random.choice(["red", "yellow", "light blue", "pink", "purple"])
        )
        self.canvas.tag_bind(balloon, "<Button-1>", lambda e, b=balloon: self.pop_balloon(b))

        self.root.after(700, self.spawn_balloon)

    def pop_balloon(self, balloon):
        self.canvas.delete(balloon)
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    
    def update_timer(self):
        if not self.game_running:
            return

        if self.time_left <= 0:
            self.end_game()
            return
        
        self.time_left -= 1
        self.timer_label.config(text=f"Time: {self.time_left}")

        self.root.after(1000, self.update_timer)


    def end_game(self):
        self.game_running = False
        self.game_frame.pack_forget()

    
        for widget in self.end_frame.winfo_children():
            widget.destroy()

        self.end_frame.pack(expand=True)

        tk.Label(self.end_frame, text="Time's Up!", font=("Arial", 26)).pack(pady=20)
        tk.Label(self.end_frame, text=f"Your Score: {self.score}", font=("Arial", 22)).pack(pady=10)

        tk.Button(self.end_frame, text="Play Again", font=("Arial", 18),
                  command=self.start_game).pack(pady=10)
        tk.Button(self.end_frame, text="Quit", font=("lexend", 18),
                  command=self.root.quit).pack()
        
root = tk.Tk()
app = PopBalloonGame(root)
root.mainloop()