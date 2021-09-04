#hello lets do this
import urllib.request


def download_image(url):
    name = ".jpg"
    urllib.request.urlretrieve(url, name)


download_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Ho_Chi_Minh_1946.jpg")

def download_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n") #take line by line
    dest_url = r'goog.csv'
    #open file we download
    fe = open(dest_url, "w")
    for line in lines: #loop through lines one by one
        fe.write(line + "\n") #xuong dong for every line

#Exception = prepare to prevent the alg from breaking
while True:
    try:
        number = int(input("Hey"))
        print(18/number)
        break #If no wrong value occurs -> break out of loop
    except ValueError: #exception 1
        print("Try")
    except ZeroDivisionError: #exception 2
        print("Dont")
    except: #handle errors in general but that hides a lot of probs
        break
    finally: #execute the finally code no matter what
        print("hay")

#Inheritance
class Parent:
    def print_first(self):
        print('Rob')

class Child(Parent): #the functions from parents are included in class Child
    def print_last(self):
        print("Meg")
 #Child can also overwrite fns by creating a new fns with the exact previous fn
    def print_first(self):
        print("Ha")
bucky = Child()
bucky.print_last()

#Multiple inheritances
class Fullname(Parent, Child):
    pass #get rid of red squiggly line

#Run multiple tasks like send and listen to messages
import threading

class BuckyMessenger(threading.Thread): #access Parent class Threading
    def run(self):
        for _ in range(10): #when we dont care what value of vars we are looping
            print(threading.currentThread().getName()) #give every thread a name
#The class above means we can have multiple objects run at the same time
x = BuckyMessenger(name='Send out message') #an arg of threading.thread
y = BuckyMessenger(name='Receive message')
#instead of accesing the function, we start the thread
x.start()
y.start()
#we can see the thread jumbled t ogether -> computers are much faster

#Zip
first = ["Buckly", "Tom"]
last = ["Meg", "Ha"]

names = zip(fist, last)

for a,b in names:
    print(a, b)

#Using zip for dict
stocks = [{'Goog': 52, 'FB': 50}]
print(min(zip(stocks.values(),stock.keys())))
#print: (50, 'FB')

#Lambda
answer = lambda x: x*7 #input:expression of what you want input to do
print(answer(5))

#MAP
income = [10, 20, 20]

def double(dollars):
    return dollars * 2

map(double, income) #for every value of list, it will run through double function
new_income = list(map(double, income))

#Sort largest smallest items on a list
import heapq

print(heapq.nlargest(1, income))
#use for your custom sets
print(heapq.nsmallest(2, stocks, key=lambda stock:stock['price'])) #since dict has number, ticker, name,... so if want to sort by price, add last arg as attribute u want

#Most frequent items in text
from collection import Counter #collection is module, counter is class
text = "We love pancakes"

words = text.split() #to create a list for each word

counter = Counter(words)
top_three = counter.most_common(3) #counter is object, most_common is function

##Dict Multiple Key Sort
from operator import itemgetter

users = [{'fname': 'nma', 'lname': 'na'}, {'fname': 'hma', 'lname': 'pna'}]
#First sort by first name and sort further by last name
for x in sorted(users, key=itemgetter('fname', 'lname')) #what attribute u want
    print(x)

##Sort by attributes u want in a list
from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self): #you want to print out Bucky, but what attribute to sort?
        return self.name + ":" + str(self.user_id)
users = [User('Bucky', 43), User('Sally', 5)]
for user in sorted(users, key=attrgetter('name')): #sort by name
    print(user)


