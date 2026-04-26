questions = [
    ["Which piece checkmates in Legal's checkmate?","King","Rook","Knight","Bishop",3],                                        
    ["What country is the biggest by a land mass?","Russia","USA","China","Canada",1],
    ["Who wrote 'Crime and punishment'?","F.Dostoevskiy","L.Tolstoy","A.Pushkin","W.Shakespeare",1],
    ["What is the chemical symbol for gold?","Ag","Cl","Au","H",3],
    ["Which country hosted the 2016 Summer Olympics?","China","Brazil","UK","USA",2],
    ["Which mathematician is known for the Last Theorem proven in 1994?","Isaac Newton","Carl Gauss","Euclid","Andrew Wiles",4],
    ["In computing, what does 'CPU' stand for?","Central Process Unit","Central Processing Unit","Computer Personal Unit","Control Program Utility",2],
    ["Which gas is most abundant in the Earth's atmosphere?","Oxygen","Carbon Dioxide","Nitrogen","Hydrogen",3],
    ["What is the smallest prime number greater than 100?","101","103","107","109",1],
    ["Who painted the ceiling of the Sistine Chapel?","Leonardo da Vinci","Raphael","Donatello","Michelangelo",4],
    ["What is the derivative of x²?","x","2x","x²","2",2],
    ["Which country has the most time zones?","USA","Russia","China","France",4],
    ["What is the value of Planck's constant (approximately)?","6.63 * 10⁻³⁴ Js","9.81 m/s²","3.00 * 10⁸ m/s","1.60 * 10⁻¹⁹ C",1],
    ["Which of these numbers is irrational?","0.25","√2","1/3","0.75",2],
    ["What is the only mammal capable of true flight?","Flying squirrel","Bat","Eagle","Sugar glider",2],
    ]

prizes = [500,1000,2000,3000,5000,7500,10000,12500,15000,25000,50000,100000,250000,500000,1000000]

game_over = False
i = 0
while not game_over:
    try:
        for question in questions:
            print(question[0])
            print(f"a. {question[1]}")
            print(f"b. {question[2]}")
            print(f"c. {question[3]}")
            print(f"d. {question[4]}")
            a = int(input("Enter your answer(1 for a, 2 for b, 3 for c,4 for d): "))
            if question[5]==a:
                print("Great! That's the right answer!")
                
            else:
                correct = question[5]
                print(f"Unfortunately it's wrong. The correct answer was {question[correct]}")
                print("Better luck next time :)")
                game_over = True
                break
            print(f"Your prizepool right now is {prizes[i]}$")
            if i==len(prizes)-1:
                print("You won!!!")
                game_over = True
                break
            i+=1
    except ValueError as e:
        print("Please try again, enter a number from 1 to 4.")
    