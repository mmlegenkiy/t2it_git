# Банкомат видає суму максимально можливими купюрами

bills = [500, 200, 100, 50]
money = int(input())
answer = f"{money} = "
if not money:
    print("Improper number")
else:
    for bill in bills:
        num = money // bill
        if num:
            answer += str(num)+'*'+str(bill)+' '
            money -= num*bill
            if money:
                answer += '+ '
            else:
                break
    if money:
        print("Improper number")
    else:
        print(answer)

    

