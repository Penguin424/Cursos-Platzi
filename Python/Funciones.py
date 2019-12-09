import turtle as tl

def make_line_and_turn(t, length):
    t.forward(length)
    t.left(90)


def make_square(t):
    length = int(input('Cual quieres que sea la longitud de la linea? '))
    for i in range(4):
        make_line_and_turn(t, length)





def main():
    window = tl.Screen()
    pablo = tl.Turtle()

    make_square(pablo)

    tl.mainloop()

if __name__ == '__main__':
    main()