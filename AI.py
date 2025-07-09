import tkinter as tk
from tkinter import ttk

# Function to predict stress level
def predict_stress():
    # Get values from sliders
    sleep = sleep_slider.get()
    study = study_slider.get()
    screen = screen_slider.get()
    mood = mood_slider.get()

    # Stress score calculation
    score = 0

    if sleep < 6:
        score += 2
    elif sleep < 7:
        score += 1

    if study > 6:
        score += 2
    elif study > 4:
        score += 1

    if screen > 5:
        score += 1

    if mood <= 2:
        score += 2
    elif mood <= 3:
        score += 1

    # Determine stress level
    if score <= 2:
        level = "Low"
        color = "green"
        tip = "✅ You're doing well! Keep a healthy balance."
    elif score <= 4:
        level = "Medium"
        color = "orange"
        tip = "💡 Try to take breaks and relax your mind."
    else:
        level = "High"
        color = "red"
        tip = "⚠️ You need rest. Sleep well and reduce screen time."

    # Show result
    result_label.config(text=f"📊 Stress Level: {level}", fg=color)
    tip_label.config(text=tip)

# Create main window
root = tk.Tk()
root.title("🧠 Exam Stress Predictor")
root.geometry("400x500")
root.config(bg="white")

# Title
tk.Label(root, text="Exam Stress Level Predictor", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Sleep Input
tk.Label(root, text="😴 Sleep Hours (0-12):", bg="white").pack()
sleep_slider = ttk.Scale(root, from_=0, to=12, orient="horizontal")
sleep_slider.pack(pady=5)

# Study Input
tk.Label(root, text="📚 Study Hours (0-12):", bg="white").pack()
study_slider = ttk.Scale(root, from_=0, to=12, orient="horizontal")
study_slider.pack(pady=5)

# Screen Time Input
tk.Label(root, text="📱 Screen Time (0-12):", bg="white").pack()
screen_slider = ttk.Scale(root, from_=0, to=12, orient="horizontal")
screen_slider.pack(pady=5)

# Mood Input
tk.Label(root, text="😊 Mood (1 = Bad, 5 = Great):", bg="white").pack()
mood_slider = ttk.Scale(root, from_=1, to=5, orient="horizontal")
mood_slider.pack(pady=5)

# Predict Button
ttk.Button(root, text="🔍 Predict Stress", command=predict_stress).pack(pady=20)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white")
result_label.pack()

# Tip Display
tip_label = tk.Label(root, text="", wraplength=350, font=("Arial", 10), bg="white")
tip_label.pack(pady=10)

# Start the app
root.mainloop()
