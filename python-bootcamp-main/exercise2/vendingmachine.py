from typing import Dict, Any, Union

amount = int(input('Enter the amount paid:'))
purchase_ID = int(input('Put in purchase_ID:')) #1123 2 waters, 1 coke and 1 diet coke

change_denom = [100, 50, 20, 10, 5]
num_coins = [5, 5, 5, 5, 5]
coins_4_change = [0, 0, 0, 0, 0]

num_items = [10, 10, 10, 10, 10, 10, 10, 10, 10]
selections = {'Water': 75, 'Coke': 120, 'Diet Coke': 120, 'Iced tea': 100, 'Swiss Chocolate': 150, 'Candy': 95, 'Chips': 110, 'Bubble Gum': 50, 'Turkish Delight': 120}
transaction = []

class vending_machine:
    def show_menu():
        for a, b in selections.items():
            id = list(selections.keys()).index(a) + 1
            print(str(id), ":", a, " costs ", b, "cents")

    def make_selection(purchase_ID):
        while purchase_ID != 0:
            digit = purchase_ID % 10
            total_amount += selections.values[digit-1]
            purchase_ID //= 10
            return total_amount
        print("The total amount to pay:" + total_amount)
        for i in range(purchase_ID):
            if i = showmenu():  # if the digit in item ID matches the items, we subtract the selection from aval items
                num_items[i-1] -= len(i)
        transaction.append(purchase_ID)

    def return_change():
        coin_nb = []
        print("Your change is:" + change_amount)
        while change_amount > 0:
            for i in range(len(change_denom)):
                coin_nb_i = int(change_amount/change_denom[i])
                coin_nb.append(coin_nb_i)
                if coin_nb[i] < num_coins[i]:
                    coins_4_change += coin_nb[i]
                        if coins_4_change > 0: #only when vm has enough coins for change
                            change_amount = change_amount - (coin_nb[i] * change_denom[i])
                            print(change_denom[i] + "cents : " + coin_nb[i])
                        else:
                            print("Your selection is not valid")
                else:
                    coin_nb[i] = 0 #if the coins needed for change > coins available, not use that denom at all

    def get_money(make_selection):
        change = amount - total_amount
        print('your  change is : ', change)
        return change

    def print_confidential_info():
        for i in range(len(num_items)):
            num_selections += purchase_ID % 10
            while num_selections >= 99:
                secret_code = int(input("Where is secret PIN code?"))
                if secret_code == secret_PIN:
                    print(num_selections)
                    total_income += num_items[i] * selections.values[i]
                    print("We earned" + total_income)
                else:
                    print("Sorry under maintenance")

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









