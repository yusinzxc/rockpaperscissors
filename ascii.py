result = ["You Win!","You Lose!","Tie!"]
asci1 = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
"""
  ___ _ __ _ __ ___  _ __
/ _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |
\___|_|  |_|  \___/|_|
"""
]

def newLine(space):
    for i in range(space):
        print()

def stadium(user,comp,result):
    newLine(10)
    print("--------------------------")
    print()
    print("User")
    print(user)
    print()
    print(comp)
    print("Computer")
    print()
    print(result)
    print()
    print("--------------------------")

