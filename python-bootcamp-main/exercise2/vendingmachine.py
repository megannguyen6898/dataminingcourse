from threading import TIMEOUT_MAX
from typing import Dict, Any, Union

amount = int(input('Enter the amount paid:'))
purchase_ID = int(input('Put in purchase_ID:')) #1123 2 waters, 1 coke and 1 diet coke

change_denom = [100, 50, 20, 10, 5]
num_coins = [5, 5, 5, 5, 5]
coins_4_change = [0, 0, 0, 0, 0]

num_items = [10, 10, 10, 10, 10, 10, 10, 10, 10]
num_items_restocked = [10, 10, 10, 10, 10, 10, 10, 10, 10]
num_coins_restocked = [5, 5, 5, 5, 5]
selections = {'Water': 75, 'Coke': 120, 'Diet Coke': 120, 'Iced tea': 100, 'Swiss Chocolate': 150, 'Candy': 95, 'Chips': 110, 'Bubble Gum': 50, 'Turkish Delight': 120}
transactions = []
ids = []
coin_nb = []

items = [] #store price of item purchased
item_names = [] #store names of items purchased

class vending_machine:
    def __init__(self, purchase_ID, secret_PIN, amount):
        self.purchase_ID = purchase_ID
        self.secret_PIN = 00
        self.digits_purchase_ID = [int(d) for d in str(self.purchase_ID)]
        self.total_amount_to_pay = 0
        self.amount = amount
        self.change_amount = self.amount - self.total_amount_to_pay
    def show_menu(self):
        for a, b in selections.items():
            id = list(selections.keys()).index(a) + 1
            print(str(id), ":", a, " costs ", b, "cents")
            ids.append(id)
    def make_selection(self, purchase_ID):
        if self.purchase_ID == self.secrete_PIN:
            self.print_confidential_info()
        else:
            for i in range(len(self.digits_purchase_ID)):
                digit = self.digits_purchase_ID[i]
                if digit > len(ids) or self.purchase_ID <= 0:
                    self.error_message()
                else:
                    ids = set(ids)
                    if digit in ids:
                        item_chosen = list(selections.values())[digit-1]
                        item_name = list(selections.keys())[digit-1]
                        items.append(item_chosen)
                        item_names.append(item_name)
                        self.total_amount_to_pay = 0
                        for j in range(len(items)):
                            self.total_amount_to_pay = self.total_amount_to_pay + items[j]
                num_items[digit-1] = num_items[digit-1] - 1
            print("You gotta pay: " + str(self.total_amount_to_pay))
            return self.total_amount_to_pay

    total_amount_to_pay_per_transaction = make_selection(purchase_ID)
    transactions.append(total_amount_to_pay_per_transaction)
    
    def error_message(self):
        print("Error!")
    def return_change(self):
        print("Your change is: " + str(self.change_amount))
        if self.change_amount < 0:
            print("Please deposit more!")
        else:
            for i in range(len(change_denom)):
                coin_nb_for_denom = int(change_amount/change_denom[i])
                coin_nb.append(coin_nb_for_denom)
                if coin_nb[i] <= num_coins[i]:
                    change_amount = change_amount - change_denom[i] * coin_nb[i]
                    coins_4_change[i] = coins_4_change[i] + coin_nb[i]
                    num_coins[i] = num_coins[i] - coin_nb[i]
                    print("Please take " + str(coins_4_change[i]) + " of " + str(change_denom[i]))
                else:
                    coin_nb[i] = 0 #if the coins needed for change > coins available, not use that denom at all
                    print("We don't have enough " + str(change_denom[i]) + " cents for you!")
        print("End of transaction!")

    def sales_each_item():
        #find frequency of items chosen
        sales_per_item = {}
        # iterating over the list
        for item in item_names:
        # checking the element in dictionary
            if item in sales_per_item:
                # incrementing the count
                sales_per_item[item] += 1
            else:
                # initializing the count
                sales_per_item[item] = 1
        #find individual sales for each item 
        common_set = set(sales_per_item.keys()).intersection(set(selections.keys()))
        common_set = list(common_set)
        sales_each_item = {}
        for selection in selections:
            if selection in common_set:
                sales_each_item[selection] = selections[selection]
        for key, value in sales_each_item.items():
            sales_each_item[key] = value * sales_per_item[key]
    def print_confidential_info():
        print("The number of items after restock: ") 
        for index, num_item in enumerate(num_items):
            num_items[index] = num_items[index] + num_items_restocked[index]
            print(list(selections.keys())[index] + " : " + str(num_items[index]))
        print("The number of coins after restock: ") 
        for indexx, num_coin in enumerate(num_coins):
            num_coins[indexx] = num_coins[indexx] + num_coins_restocked[indexx]
            print(str(change_denom[indexx]) + " : " + str(num_items[indexx]))

    def monitor():
        for i in range(len(num_items)):
            if num_items[i] = 0:
                print("Hey lack" + selections.keys[i])

    def main():
        secret_PIN = 9999
        total_cost = make_selection()
        print("Pay:", cost)

        change = get_money(cost)
        if change > 0:
            return_change(change)
            #update item list
        else:
            print(' you have not given enough')

        #give them the chance to give again
    if __name__ == '__main__':
        main()

class machine_list:
    def __init__(self, machine_id, address, manager_name):
        self.machine_id = machine_id
        self.address = address
        self.manager_name = manager_name

    def total_income(self):
        for purchase_ID in range(transaction):
            total_amount_each_ID = make_selection(purchase_ID)
            total_income_machine += total_amount_each_ID
            print("This machine earns:" + total_income_machine)
        return total_income_machine

    def machine_info(self):
        print("Machine ID:" + self.machine_id)
        print("Machine address:" + self.address)
        print("Machine Manager:" + self.manager_name)









