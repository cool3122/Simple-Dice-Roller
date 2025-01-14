import tkinter as tk
import random

def roll_dice():
    try:

        Number_of_Dice = int(entry1.get())
        Number_of_Sides = int(entry2.get())
        Dice_Label = []
        General_Dice_Label.config(text = f"{Number_of_Dice} D {Number_of_Sides}")
        total = 0
        Total_Label.config(text=total)

        for label in Result_Frame.winfo_children():
            label.grid_forget()

        row, col = 0, 0
        for i in range(Number_of_Dice):
            roll = random.randint(1,Number_of_Sides)
            Dice_Label.append(f"Die {i + 1}: {roll}") # create a label for each roll
            Roll_Label = tk.Label(Result_Frame, text=f"Die {i + 1}: {roll}")
            Roll_Label.grid(row=row, column=col, padx=10, pady=5, sticky="w")  # Place the label in the grid
            total += roll
            col += 1
            if col == 3:  # If we reach 3 columns, move to the next row
                col = 0
                row += 1

        Total_Label.config(text=f"Total: {total}")

    #hi
    except ValueError:
        Total_Label.config(text="Please enter valid numbers.")

def check_fields():
    if entry1.get() != "" and entry2.get() != "":
        button.config(state=tk.NORMAL)  # Enable the button
    else:
        button.config(state=tk.DISABLED)  # Disable the button

def validate_input(P):
    if P == "" or P.isdigit() and int(P) > 0:
        return True
    else:
        return False

root = tk.Tk()
root.title("Dice Roll Simulator")
root.geometry("300x400")

vcmd = (root.register(validate_input), "%P")


label1 = tk.Label(root, text = "Number of Dice")
label2 = tk.Label(root, text = "Number of Sides")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

General_Dice_Label = tk.Label(root, text="Total: \n")
Total_Label = tk.Label(root, text="\n")

Result_Frame = tk.Frame(root)

button = tk.Button(root, text="Submit", command=roll_dice, state=tk.DISABLED)

root.grid_rowconfigure(0, weight=0)  # Make row 0 expand
root.grid_rowconfigure(1, weight=0)  # Entry rows don't need to expand
root.grid_rowconfigure(2, weight=0)  # Button doesn't need to expand
root.grid_rowconfigure(3, weight=0)  # Result_Frame will expand with content
root.grid_rowconfigure(4, weight=0)  # Result_Frame will expand with content
root.grid_rowconfigure(5, weight=1)  # Result_Frame will expand with content

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

entry1.bind("<KeyRelease>", lambda event: check_fields())  # Whenever a key is released, check fields
entry2.bind("<KeyRelease>", lambda event: check_fields())  # Same for the second field


label1.grid(row=0, column=0, padx=10,pady=5, sticky="nesw")
entry1.grid(row=0, column=1, padx=10,pady=5, sticky="nesw")
label2.grid(row=1, column=0, padx=10,pady=5, sticky="nesw")
entry2.grid(row=1, column=1, padx=10,pady=5, sticky="nesw")
button.grid(row=2, column=0, columnspan=2, padx=10,pady=5, sticky="nesw")
General_Dice_Label.grid(row=3, column=0, columnspan=2, padx=10,pady=5, sticky="nesw")
Total_Label.grid(row=4, column=0, columnspan=2, padx=10,pady=5, sticky="nesw")
Result_Frame.grid(row=5, column=0, columnspan=2, padx=10,pady=5, sticky="nesw")


# Run the application
root.mainloop()