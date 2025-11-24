import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pygame

pygame.mixer.init()
pygame.mixer.music.load("pet_sound.mp3")  
pygame.mixer.music.play()

# **🐾 Virtual Pet GUI Class**
class VirtualPetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ My Cute Virtual Pet 🐾")
        self.root.geometry("600x450")
        self.root.configure(bg="#FFC0CB")  # Pastel pink background

        # **🐶 Ask user for a pet name**
        self.pet_name = simpledialog.askstring("Name Your Pet", "What do you want to name your pet? 💖")  
        if not self.pet_name:  
            self.pet_name = "SIMI"  # Default name if user leaves it empty

        # **🐾 Title with Pet Name**
        self.title_label = tk.Label(
            root, text=f"🐶 Meet {self.pet_name}! 🐾", 
            font=("Comic Sans MS", 16, "bold"), bg="#FFC0CB", fg="#000000"
        )
        self.title_label.pack(pady=10)

        # **🐾 Load & Resize Pet Image**
        try:
            self.pet_photo = tk.PhotoImage(file="pet.png").subsample(4, 4)  
            self.pet_label = tk.Label(root, image=self.pet_photo, bg="#FFC0CB")  
        except:
            self.pet_label = tk.Label(root, text=f"🐾 {self.pet_name} is missing! (No image found)", font=("Comic Sans MS", 14), bg="#FFC0CB")

        self.pet_label.pack(pady=10)

        # **🐾 Status Bars with Cute Text**
        self.hunger_bar = self.create_status_bar(f"🍩 {self.pet_name}'s Hunger", 5)
        self.happiness_bar = self.create_status_bar(f"💖 {self.pet_name}'s Happiness", 5)
        self.energy_bar = self.create_status_bar(f"😴 {self.pet_name}'s Energy", 5)

        # **🐾 Cute Buttons**
        btn_frame = tk.Frame(root, bg="#FFC0CB")
        btn_frame.pack(pady=10)

        self.create_cute_button(btn_frame, f"🍓 Feed {self.pet_name}!", self.feed, 0)
        self.create_cute_button(btn_frame, f"🎀 Play with {self.pet_name}!", self.play, 1)
        self.create_cute_button(btn_frame, f"🌙 Put {self.pet_name} to Sleep!", self.sleep, 2)

        # **🐾 Auto-update pet status**
        self.root.after(5000, self.update_pet)
    
# **🐾 Helper Functions**
    def create_status_bar(self, text, value):
        frame = tk.Frame(self.root, bg="#FFC0CB")
        frame.pack(pady=5)
        label = tk.Label(frame, text=text, bg="#FFC0CB", font=("Comic Sans MS", 12))
        label.pack(side="left")
        bar = ttk.Progressbar(frame, length=200, maximum=10)
        bar.pack(side="right")
        bar["value"] = value
        return bar

#----------------------------------------------------------------
    def create_cute_button(self, frame, text, command, column):
        btn = tk.Button(
            frame, text=text, command=command, 
            font=("Comic Sans MS", 10, "bold"), bg="#000000", fg="white",
            padx=10, pady=5, borderwidth=3, relief="ridge"
        )
        btn.grid(row=0, column=column, padx=5)

    def update_pet(self):
        self.hunger_bar["value"] += 1
        self.happiness_bar["value"] -= 1
        self.energy_bar["value"] -= 1

        if self.hunger_bar["value"] > 10 or self.happiness_bar["value"] < 1 or self.energy_bar["value"] < 1:
            messagebox.showerror("💔 Oh No!", f"{self.pet_name} is sad! Take better care next time 🥺💖")
            self.root.destroy()
        else:
            self.root.after(5000, self.update_pet)

    def feed(self):
        self.hunger_bar["value"] = max(0, self.hunger_bar["value"] - 3)
        self.energy_bar["value"] += 1
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.5)
        

    def play(self):
        if self.energy_bar["value"] > 1:
            self.happiness_bar["value"] += 2
            self.energy_bar["value"] -= 2

    def sleep(self):
        self.energy_bar["value"] += 3
        self.hunger_bar["value"] += 1

if __name__ == "__main__":
    root = tk.Tk()
    pet_game = VirtualPetGUI(root)
    root.mainloop()
