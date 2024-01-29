def pizza_number():
    '''function to get the input of number of pizzas'''
    while True:
        try:
            num_of_pizza = int(input("How many pizzas ordered?"))
            if num_of_pizza >0:
                return num_of_pizza
            else:
                print("please enter a positive integer!")

        except ValueError:
            print("Please enter a number!")
def get_yes_no_input(prompt):
    '''handeling the exception if user is inputting the Y or N'''
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "n"]:
            return answer =="y"
        else:
            print("Please answer 'Y' or 'N'.")
def calculate_pizza_price(num_pizzas,delivery_required, is_tuesday, app_used):
    '''this function calculates the pizza final price considering the discounts applied or not'''
    price = num_pizzas * 12
    if delivery_required:
        '''applyong the delivery charge'''
        if num_pizzas >4:
            price +=0
        else:
            price +=2.50
    if is_tuesday:
        '''applying the tuesday discount, 50% on pizza price only'''
        price *= 0.5  
    if app_used:
        '''applying app discount of 25% '''
        price *= 0.75  
    return price
def main():
    a = "BPP Pizza price calculator"
    print(a)
    print("="*len(a))
    num_pizzas = pizza_number()
    delivery_required = get_yes_no_input("Is delivery required? ")
    is_tuesday = get_yes_no_input("Is it Tuesday? ")
    app_used = get_yes_no_input("Did the customer use the app? ")
    total_amount = calculate_pizza_price(num_pizzas,delivery_required, is_tuesday, app_used)
    print("\nTotal Price: £{:.2f}".format(total_amount))
main()