# def format_name(f_name, l_name):
#     """This fuction take you first name and last name then combine it together."""
#     A = f_name.title()
#     a = l_name.title()
#     print(f"Your name is {A} {a}.")
#
#
#
# format_name(input("what is yoyr first name?"), input("what is your last name?"))
#
#


#CALCULATOR


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide,
}
def calculator():
    a = float(input("what is the first number?"))
    should_accumulate= True
    while should_accumulate:

        for symbol in operation:
            print(symbol)
        b = input("select the operation you want to operate: ")
        c = float(input("what's the 2nd number for operation?"))
        answer = operation[b](a,c)
        print(f"{a} {b} {c} = {answer}")

        respond = input(f"type 'y' to continue calculating with {answer}, type 'n' to start calculating with intial.")

        if respond == "y":
            answer = a
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()