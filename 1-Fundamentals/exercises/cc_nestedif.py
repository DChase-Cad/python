from random import randint

def getPrice():
    low = int(input('Enter the lowest a price can be: '))
    high = int(input('Enter the highest a price can be: '))
    return [low,high]

prices=getPrice()

if prices[0] < prices[1]:
    price = randint(prices[0], prices[1])
else:
    print("Low price needs to be less than high price")
    prices=getPrice()

print("Testing purposes price = ", price)

while True:
    guess = int(input("Enter the price: "))
    if guess == price:
        print("Price is exactly that!")
        break
    elif guess < price-5:
        print("Price is too low!")
    elif guess > price+5:
        print("Price is too high!")

    elif guess >= price-5 and guess < price:
        print("Price is almost there just a tad higher!")
    else:
        print("Price is almost there just a tad lower!")
