# Score Gen Program

import random

sets_required = int(input("How many sets of score do you need?\n>> "))
array_length = 8
scores = []

# numgen1 generates the score for max score 10
def numgen1():
  number = random.randint(6,9)
  return number

# numgen1 generates the score for max score 15
def numgen2():
  number = random.randint(8,14)
  return number

# numgen1 generates the score for max score 20
def numgen3():
  number = random.randint(11,19)
  return number

for j in range(sets_required):
    for i in range(array_length):
        if i < 2:
            score = numgen1()
            scores.append(score)
        elif i >= 2 and i < 4:
            score = numgen2()
            scores.append(score)
        elif i >= 4 and i < 6:
            score = numgen3()
            scores.append(score)
        elif i == 6:
            total_score = 0
            for score in scores:
                total_score += score
            scores.append(total_score)
        elif i == 7:
            if scores[6] < 50:
                scores.append('F')
            else:
                scores.append('P')

    print(f"{j+1}: {scores}")
    scores.clear()