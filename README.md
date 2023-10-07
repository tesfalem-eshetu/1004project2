Total Points: 100

You are welcome to discuss the problem with other students but the program you submit must be your own work. Please review the academic honesty policy for this course (see the syllabus).

Do not use Python modules other than those explicitly mentioned. 

Upload a single file called problem1.py to Courseworks.

 A Conversational Agent for Ordering Meals

A conversational agent is a computer program that communicates with the user in natural language, following a specific dialog structure to accomplish a tasks. Common examples are automatic phone systems for making reservations, purchasing, bank inquiries, or personal voice assistants such as Amazon Alexa or Apple Siri.

In this homework, we will use Python functions to create a conversational agent. Our conversational agent will be very simple with a limited vocabulary and a simplistic dialog structure. The goal of the agent will be to allow the user to order from an Italian restaurant serving pizza and salad. The dialog could look as follows (the text highlighted in bold is entered by the user):

Would you like pizza or salad? pizza
Small, medium, or large? large
Add a topping: pepperoni, mushrooms, spinach, or enter 'done'. mushrooms
Add a topping: pepperoni, mushrooms, spinach, or enter 'done'. spinach
Add a topping: pepperoni, mushrooms, spinach, or enter 'done'. done
You order contains a large pizza with mushrooms and spinach.
Would you like to continue ordering? (yes/no) yes
Would you like pizza or salad? salad
Garden or greek salad? greek
Choose a dressing: vinaigrette, ranch, blue cheese, or lemon. blue cheese
You order contains a large pizza with mushrooms and spinach and a greek salad with blue cheese dressing.
Would you like to continue ordering? (yes/no) no
Your order has been placed. Thank you come again!
Implement Python functions that repeatedly prompt the user for his/her selection and assemble the order, as illustrated in the following diagram:

meal-agent.png

The diagram shows the order in which the functions should be invoked, from top to bottom. For example, the function choose_salad() asks the user to select the type of the salad (garden or greek) and then invokes the choose_dressing() function which asks the user for a dressing type. All functions in the above diagram:

take no parameters;
ask the user for selection using the built-in method input();
return a string, except the main() function which returns nothing (None).
An example string returned by each function is shown in blue. For example, the choose_dressing() function returns a string like "blue cheese". The choose_salad() function combines the type of the salad and the dressing returned by choose_dressing() into a string like "a greek salad with blue cheese dressing". And so on.  

Checklist for individual functions:

main(): This function invokes the function choose_meal() repeatedly. After each invocation, it prints everything ordered so far ("Your order contains...") and then asks the user if they want to continue ordering. If the answer is "no", the function prints the final message "Your order has..." and terminates.
choose_pizza(): Make sure this function returns the correct string if the user adds no toppings. In this case, the function should return "a ... pizza" and not "a ... pizza with".
add_topings(): This function asks the user for toppings repeatedly until they enter "done". The return value of this function is a single string with all selected toppings, e.g., "pepperoni and mushrooms". If the user selects one topping more than once, the returned string should only contain the topping once. For example, selecting "pepperoni", "pepperoni", "mushroom" returns the string "pepperoni and mushroom".
Program development hints:

You do not have to validate inputs. The user always enters the correct string.
All text entered by the user will be in lower case.
The focus of this homework is on functions and their invocations, i.e., nested function invocations.
All functions should be side-effect free, i.e., they should not modify any data (variables) defined outside of the function body.
Use string formatting with {} placeholders to assemble the strings.
What string method (covered in class) could you use to join an iterable (list) into a string?
Surround each function with 1-2 empty lines. Your program will be easier to read and understand that way.
Put all your functions in the file problem1.py. At the end of the file, create the following main program to start the agent:

if __name__ == "__main__":
    main()
