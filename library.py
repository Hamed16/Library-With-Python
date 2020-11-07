#python library

#books
books =  ["Harry Potter", "Perrsy Jackson", "Romeo and Juliet", "Ethan Frome", "Java Head on", "Red book", "Blue book", "How to play tennis", "Taekwondo kicks", "Learn Python"]

#borrow price
booksBorrowPayments = { "Harry Potter": 2, "Perrsy Jackson": 1, "Romeo and Juliet": 2, "Ethan Frome": 1.5, "Java Head on": 0.5, "Red book": 0.2, "Blue book": 0.8, "How to play tennis": 2, "Taekwondo kicks": 3, "Learn Python": 5
}

#borrow times
booksBorrowTimes = { "Harry Potter": "2 weeks", "Perrsy Jackson": "10 days", "Romeo and Juliet": "2 weeks", "Ethan Frome": "12 days", "Java Head on": "15 days", "Red book": "5 days", "Blue book": "3 weeks", "How to play tennis": "9 days", "Taekwondo kicks": "20 days", "Learn Python": "1 month"
}


basket = []
total = []
borrowLimit = []


clients_answer = input(f"Hi and welcome to Toronto Library.\nHere we have many books. Here are your options, prices, and borrow times.\n {booksBorrowPayments}\n {booksBorrowTimes}\n\n what would you like to borrow today?  ")

while clients_answer != "thats it":
    if clients_answer in books:
        basket.append(clients_answer)
        clients_answer = input("Okay i will add that to your basket, is their anything else you would like to borrow? "
              "Type 'thats it' to end  ")

    else: #if book is not available
        clients_answer =  input("sorry we do not have that book in are library, is their anything else you would like to borrow: "
        "Type 'thats it' to end   ")


print(f"Okay you have {basket} in your basket ")

clients_answer = input("Is the ir anything else you would like to buy: ")

while clients_answer != "thats it":
    if clients_answer in books:
        basket.append(clients_answer)
        clients_answer = input("Okay i will add that to your basket, is their anything else you would like to borrow? "
              "Type 'thats it' to end   ")


#order total
for books in basket:
    total.append(booksBorrowPayments[books])
amount_to_pay = sum(total)

# time limit for each book
for book in basket:
    borrowLimit.append(booksBorrowTimes[book])


print(f"\n{basket}")
print(f"\n You can borrow each book for the given times, each time period coresposds to the order of the books. The first time period is the for the first book you chose and so on.\n{borrowLimit}")
print(f"\n You have to pay {amount_to_pay} dollar")