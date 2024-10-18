correct_password = "python123"
loggedin = False

while loggedin == False:
    ievads = str(input("Ievadi paroli: "))
    if ievads == correct_password:
        print("Piekļuve atļauta!")
        loggedin = True
    elif ievads != correct_password:
        print("Piekļuve liegta")
