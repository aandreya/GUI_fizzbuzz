from Tkinter import *

def fizzbuzz():
    output=""
    from_number = int(enter_starting_number.get())
    to_number = int(enter_ending_number.get())

    for number in range(from_number, to_number+1):
        if (number % 3 == 0 and number % 5 == 0):
            output += "fizzbuzz\n"
        elif (number % 5 == 0):
            output += "buzz\n"
        elif (number % 3 == 0):
            output += "fizz\n"
        else:
            output += str(number) + "\n"
    game_result.config(text=output)

frame = Tk()
frame.geometry("400x1000")
frame.title("FIZZBUZZ")
greeting = Label(frame, text="Choose random numbers between 0 and 100...")
greeting.grid(row=0)
placeholder_label = Label(frame, text="")
placeholder_label.grid (row=1)

label_starting_number = Label(frame, text="Start FIZZBUZZ from number:")
label_starting_number.grid(row=2, column=0)
enter_starting_number = Entry(frame)
enter_starting_number.grid(row=2, column=1)

label_ending_number = Label(frame, text="Cout FIZZBUZZ to number:")
label_ending_number.grid(row=3, column=0)
enter_ending_number = Entry(frame)
enter_ending_number.grid(row=3, column=1)

play_button = Button(frame, text="Let's play", command=fizzbuzz)
play_button.grid(row=4, column=1)

game_result_label = Label(frame, text="")
game_result_label.grid(row=5, column = 0)
game_result = Label(frame, text="")
game_result.grid(row=6, column = 0, columnspan=2)

frame.mainloop()