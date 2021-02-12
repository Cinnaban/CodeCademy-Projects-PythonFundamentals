import random

name = "Charles"
question = "Will I win the lottery?"
answer = ""

random_value = random.randint(1, 9)
print(random_value)

if random_value == 1:
  answer = "Yes - definitely."
elif random_value == 2:
  answer = "It is decidedly so"
elif random_value == 3:
  answer = "Without a doubt."
elif random_value == 4:
  answer = "Reply hazy, try again."
elif random_value == 5:
  answer = "Ask again later."
elif random_value == 6:
  answer = "Better not tell you now."
elif random_value == 7:
  answer = "My sources say no."
elif random_value == 8:
  answer = "Outlook not so good."
elif random_value == 9:
  answer = "Very doubtful."
elif random_value == 10:
  answer = "Signs point to yes"
else:
  answer = "Error"

if name == "":
  print("Question: " + str(question))
else:
  print(str(name) + " asks: " + str(question))

if question == "":
  print("Please ask a question")
else:
  print("Magic 8-Ball's answer: " + str(answer))


