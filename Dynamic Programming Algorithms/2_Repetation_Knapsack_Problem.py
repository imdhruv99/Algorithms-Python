"""
Consider a backpack (or "knapsack") that can hold up to a certain amount of weight. 
You have a set of items at your disposal, each being worth a different value and having a different weight. 
You want to fill the backpack with the most valuable combination of items without overburdening it and 
going over the weight limit. This is the Knapsack Problem.  
"""
# Pandas is just for visualising 2d array as table
from pandas import DataFrame

class Knapsack:

    @staticmethod
    def knapsack(items_weights, items_values, weight):

        n = len(items_weights)

        k = [0] * (weight + 1)

        # Base case redundant

        k[0] = 0

        for weight in range(1, weight + 1):

            max_sub_result = 0

            for i in range(1, n):

                wi = items_weights[i]

                vi = items_values[i]

                if wi <= weight:

                    subproblem_value = k[weight - wi] + vi

                    if subproblem_value> max_sub_result:

                        max_sub_result = subproblem_value
        
        k[weight] = max_sub_result
        
        print("Result: ", k[weight])
        
        print("K Table: ")

        print(DataFrame(k))

class Main:

    items_weight = []
    
    items_value = []

    weight = int(input("Enter Total weight capacity: "))
    
    num = int(input("Enter Number For how much items you want: "))
    
    print("-------------------------------------")

    # Creating List with items weight

    for i in range(num):
    
        weight_of_item = int(input("Enter items weight:"))
    
        items_weight.append(weight_of_item)
    
    print("--->>>", items_weight)

    print("-------------------------------------")

    # Creating List with items value

    for i in range(num):
    
        value_of_item = int(input("Enter items value:"))
    
        items_value.append(value_of_item)

    print("--->>>", items_value)

    obj_of_knapsack = Knapsack()

    obj_of_knapsack.knapsack(items_weight, items_value, weight)