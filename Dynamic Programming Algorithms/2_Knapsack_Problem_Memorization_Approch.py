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

        k = [[0 for weight in range(weight + 1)] for i in range(n)]

        for i in range(1, n):

            for weight in range(1, weight + 1):

                wi = items_weights[i]

                vi = items_values[i]

                if wi <= weight:

                    k[i][weight] = max([k[i - 1][weight - wi] + vi, k[i - 1][weight]])

                else:

                    k[i][weight] = k[i - 1][weight]

        print("Result: ", k[n - 1][weight])
        
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