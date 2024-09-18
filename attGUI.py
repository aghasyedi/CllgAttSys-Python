

from pathlib import Path
import attendance as at
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1066x720")
window.configure(bg = "#FFCBC8")


canvas = Canvas(
    window,
    bg = "#FFCBC8",
    height = 720,
    width = 1066,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))




canvas.place(x = 0, y = 0)
image_1 = canvas.create_image(
    533.0,
    360.0,
    image=image_image_1
)

image_2 = canvas.create_image(
    540.0,
    386.0,
    image=image_image_2
)

canvas.create_rectangle(
    0.0,
    0.0,
    1066.0,
    80.0,
    fill="#847A7A",
    outline="")

image_3 = canvas.create_image(
    637.0,
    27.0,
    image=image_image_3
)

image_4 = canvas.create_image(
    107.0,
    386.0,
    image=image_image_4
)
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda subnum = 1:imgg(subnum),
    relief="flat"
)
button_1.place(
    x=30.0,
    y=204.0,
    width=145.0,
    height=39.42982482910156
)

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda subnum = 2:imgg(subnum),
    relief="flat"
)
button_2.place(
    x=30.0,
    y=249.7894744873047,
    width=145.0,
    height=39.42982482910156
)

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda subnum = 3:imgg(subnum),
    relief="flat"
)
button_3.place(
    x=30.0,
    y=295.5789489746094,
    width=145.0,
    height=39.42982482910156
)

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda subnum = 4:imgg(subnum),
    relief="flat"
)
button_4.place(
    x=30.0,
    y=341.368408203125,
    width=145.0,
    height=39.42982482910156
)

button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda subnum = 5:imgg(subnum),
    relief="flat"
)
button_5.place(
    x=30.0,
    y=388.4298095703125,
    width=145.0,
    height=39.42982482910156
)

image_5 = canvas.create_image(
    107.0,
    159.0,
    image=image_image_5
)
image_6 = canvas.create_image(
    959.0,
    386.0,
    image=image_image_6
)

image_7 = canvas.create_image(
    560.0,
    176.0,
    image=image_image_7
)



def imgg(subnum):
    at.Initialize(subnum) #connects to subject database
       
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.percentAttendance(),
        relief="flat"
    )
    button_6.place(
        x=347.86798095703125,
        y=216.0,
        width=354.7247619628906,
        height=54.43103790283203
    )

    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.updateAttendance(),
        relief="flat"
    )
    button_7.place(
        x=347.86798095703125,
        y=274.03448486328125,
        width=342.9962463378906,
        height=56.298851013183594
    )

    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.addStudent(),
        relief="flat"
    )
    button_8.place(
        x=347.86798095703125,
        y=332.0689697265625,
        width=342.9962463378906,
        height=56.298851013183594
    )

    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.delStudent(),
        relief="flat"
    )
    button_9.place(
        x=349.00372314453125,
        y=389.97125244140625,
        width=342.9962463378906,
        height=52.298851013183594
    )

    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.updateAttendance(setAtt=2),
        relief="flat"
    )
    button_10.place(
        x=349.00372314453125,
        y=446.66668701171875,
        width=342.9962463378906,
        height=56.298851013183594
    )

    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: at.deleteAttendace(),
        relief="flat"
    )
    button_11.place(
        x=349.00372314453125,
        y=503.66668701171875,
        width=342.9962463378906,
        height=60.33330535888672
    )
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: closesx(), #close button
        relief="flat"
    )
    button_12.place(
        x=736.0,
        y=176.0,
        width=37.0,
        height=36.0
    )
    image_13 = canvas.create_image(
        724.0,
        596.0,
        image = globals()[f'button_image_{subnum}']
        # image=image_image_13
    )

    def closesx():
        button_6.destroy()
        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_10.destroy()
        button_11.destroy()
        button_12.destroy()
        canvas.delete(image_13)




window.resizable(False, False)
window.mainloop()
