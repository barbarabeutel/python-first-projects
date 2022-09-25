def greeting(name):
    print("Are you okay, ", name, "?", sep="")
def whats_up(answer):
    if input_whatsup.__contains__('Not' or 'no'): 
        print("Don't be sad. Take it easy today because tomorrow is another day.")
    else:
        print("That's great! I guess today the sky is the limit.")



    #Main program
input_name = input("Hi, I am Jonathan. What's your name?\n")
greeting(input_name)

input_whatsup = input()
whats_up(input_whatsup)