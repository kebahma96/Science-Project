import tkinter as tk


def search_element(entry):
    """

    :param entry: 
    :return: 
    """

    def get_row(entry):
        """

        :param entry:
        :return:
        """
        with open("elements.csv") as csv_file:
            for row in csv_file:
                if str(entry) in row:
                    return row
            return row

    result = get_row(entry)
    label3.config(text=result)


def PressedReturn(event):
    search_element(inputs.get())


root = tk.Tk()
root.title("Science Database")


canvas = tk.Canvas(root, height=350, width=400)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

background_image = tk.PhotoImage(file="backround.gif")
background_label = tk.Label(frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame2 = tk.Frame(background_label, background="#3295a8", height=25, width=283)
frame2.place(rely=0.2925, relx=0.145)

inputs = tk.Entry(frame, bg="white")
inputs.place(rely=0.36, relx=0.33)


label = tk.Label(frame, text="Write down the element whose data u want to know", bg="#32a2a8")
label.place(rely=0.3, relx=0.15)
label2 = tk.Label(frame, text="Created by Ahmadou Bamba Kebe", bg="gray")
label2.pack(side="bottom")
label4 = tk.Label(frame, bg="green", text="name, mass num, atomic num, electronic config")
label4.place(rely=0.53, relx=0.15, relwidth=0.7)

label3 = tk.Label(frame, bg="white", borderwidth=2, relief="ridge")
label3.place(rely=0.6, relx=0.15, relwidth=0.7)

search = tk.Button(frame, text="Write elements stats", bg="#327ba8", command=lambda: search_element(inputs.get()))
search.place(relx=0.35, rely=0.41384175, relwidth=0.275, relheight=0.1)
inputs.bind('<Return>', PressedReturn)

root.mainloop()
