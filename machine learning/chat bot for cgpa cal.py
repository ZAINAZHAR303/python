


def cgpa_calculator(gpa1,gpa2,gpa3,gpa4):
    cgp=gpa1+gpa2+gpa3+gpa4
    return cgp/4


qna={
"hi":"hello!how can i assist you?",
"what is the way to succeeed?": "work,work and work.",
"how are you?":"i am fine.thanks."

}
def lowercase_input(user_input):
    return user_input.lower()

while True:
    user_input= input("you: ")
    user_input_lower=lowercase_input(user_input)

    if user_input_lower == "exit":
        print("bot: Goodbye")
        break;
    elif not user_input:
        print("Bot: you don't enter something,please enter,so i can answer")

    elif user_input_lower=="can ycou calculate cgpa for me":
        print("of course!")

        try:

            gpa1 =float(input("\n please enter you gpa of 1st semester: \n"))

            gpa2 =float(input("\n please enter you gpa of 2nd semester: \n"))
            gpa3 =float(input("\n please enter you gpa of 3rd semester: \n"))
            gpa4 =float(input("\n please enter you gpa of 4rd semester: \n"))
            cgpa=cgpa_calculator(gpa1,gpa2,gpa3,gpa4)
            print("Bot : your total cgpa is :",cgpa)

        except ValueError:
            print("you enter wrong input format!! ")



    elif user_input_lower not in qna:
        print("Bot : i don't understand please try in another way.")



    else:
        print("Bot:",qna[user_input_lower])








