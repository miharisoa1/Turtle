import turtle


def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 5
    t.forward(taille)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1) * taille_depart
        carre(taille)


t = turtle.Turtle()

# escalier(30, 5)
# carre(100)
carres(20, 5)

turtle.done()
