from random import choice
questions=["why is the sky blue?","why is face moon?","where are dinosours?"]
question=choice(questions)
answer=input(question).strip.lower()
while answer!="just because":
    answer=input("why?:").strip.lower()
print("oh....okay")
