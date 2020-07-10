numb = input("Please enter a positive number :")

ast = len(numb)

i = 0

sum = 0

if not numb.isdigit() :

    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

elif float(numb) < 0:

    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

else:

    while i < ast:

        digit = int(numb[i]) ** ast

        sum += digit

        i +=1

    if sum == int(numb):

        print("This is an armstrong number")

    else:

        print("This is not an armstrong number")