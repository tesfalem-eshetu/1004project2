def add_toppings():
    topping_input = input("Add a topping: pepperoni ,mushrooms ,spinach ,or enter 'done'.")
    topping_list = []
    while topping_input != "done":
        if topping_input not in topping_list:
            topping_list.append(topping_input)
        topping_input = input("Add a topping: pepperoni ,mushrooms ,spinach ,or enter 'done'.")
    topping_return = " and ".join(topping_list)
    if len(topping_list) != 0:
         return topping_return


def choose_dressing():
    dressing_input = input("Choose a dressing: vinaigrette, ranch, blue cheese, or lemon. ")
    return dressing_input


def choose_pizza():
    pizza_size = input("Small, medium, or large? ")
    result = add_toppings()
    if result != None:
        return "a {0} pizza with {1} ".format(pizza_size, result)
    if result == None:
        return "a {0} pizza".format(pizza_size)


def choose_salad():
    salad_choice = input("Garden or greek salad? ")
    result = choose_dressing()
    return "a {} salad with {} dressing ".format(salad_choice, result)


def choose_meal():
    meal_choice = input("Would you like pizza or salad? ")
    if meal_choice == "pizza":
        return choose_pizza()
    else:
        return choose_salad()


def main():
    order_meal = True
    result_list = []
    while order_meal:
        result = choose_meal()
        result_list.append(result)
        print("your order contains {0} ".format(" and ".join(result_list)))
        add = input("Would you like to continue ordering? (yes/no) ")
        if add == "no":
            order_meal = False
            break
    print("Your order has been placed. Thank you come again! ")
    return " "


if __name__ == '__main__':
    main()
