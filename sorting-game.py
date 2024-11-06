import tkinter as tk
import random

# QuickSort function
def quicksort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] if ascending else [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] if ascending else [x for x in arr if x < pivot]
    return quicksort(left, ascending) + middle + quicksort(right, ascending)


order = "ascending"  
numbers = random.sample(range(1, 100), 10)
numbers_sorted = quicksort(numbers, ascending=(order == "ascending"))
current_index = 0  
selected_numbers = []  


root = tk.Tk()
root.title("Sorting Game with QuickSort")
root.geometry("900x400")

welcome_frame = tk.Frame(root)
game_frame = tk.Frame(root)

def show_game_screen():
    welcome_frame.pack_forget()
    game_frame.pack()

welcome_message = tk.Label(welcome_frame, text="Welcome to the Sorting Game!\nSort the numbers in order!", font=("Comic Sans MS", 18), pady=20)
welcome_message.pack()

start_button = tk.Button(welcome_frame, text="Start Game", font=("Comic Sans MS", 14), command=show_game_screen)
start_button.pack(pady=20)

message_label = tk.Label(game_frame, text="Click the numbers in sorted order.", font=("Comic Sans MS", 16))
message_label.pack(pady=10)

button_frame = tk.Frame(game_frame)
button_frame.pack(pady=20)

buttons = {}

selected_label = tk.Label(game_frame, text="Ordered numbers: ", font=("Comic Sans MS", 14), fg="black")
selected_label.pack(pady=10)

def update_message(text, color):
    message_label.config(text=text, fg=color)

def update_selected_label():
    selected_label.config(text="Selected: " + " ".join(map(str, selected_numbers)))

def on_button_click(number, idx):
    global current_index
    if number == numbers_sorted[current_index]:
        selected_numbers.append(number)
        update_selected_label()
        buttons[idx].config(state="disabled", bg="green")
        current_index += 1
        if current_index == len(numbers_sorted):
            update_message("You sorted it correctly! Completed!", "black")
    else:
        update_message("Error! Try Again.", "red")


for idx, num in enumerate(numbers):
    button = tk.Button(button_frame, text=str(num), font=("Comic Sans MS", 14), width=4, height=2,
                       bg="blue", fg="black", command=lambda num=num, idx=idx: on_button_click(num, idx))
    button.grid(row=0, column=idx, padx=5)
    buttons[idx] = button


welcome_frame.pack()
root.mainloop()