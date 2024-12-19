from matplotlib import pyplot as plt
import sys

plt.title("Hailstone Numbers")

#this function takes a starting value and returns a list of the hailstone numbers that take it to 1
def generate_hailstones(starting_value):
    y_values = [starting_value]
    while starting_value > 1:
        #print("Generating hailstones for ", starting_value)
        if starting_value % 2 == 0:
            starting_value /= 2
        else:
            starting_value *= 3
            starting_value += 1
        y_values.append(starting_value)
    
    #the y_values list now stores every hailstone number.
    return y_values

#this function takes a starting number, generates the hailstones for it, matches them with a list of their indexes, and plots the hailstone path to the graph (hailstone number vs step #)
def plot_hailstone_graph(hailstone):
    value_list = generate_hailstones(hailstone)
    x_values = []
    for i in range(len(value_list)):
        x_values.append(i)
    
    plt.xlabel("Step Number")
    plt.ylabel("Hailstone Number")
    plt.plot(x_values, value_list)

#this function takes a starting number and matches it with the stopping time (steps to get to 1)
def plot_stop_time(starting_number):
    stop_time = len(generate_hailstones(starting_number))
    
    plt.xlabel("Starting Number")
    plt.ylabel("Stopping Time")
    plt.scatter(starting_number, stop_time)

def choose_option():
    option = 0
    while (option != 1 and option != 2 and option != 3 and option != 4):
        print("Choose one of the below functionalities:")
        print("1. Graph individual hailstone paths")
        print("2. Graph hailstone paths up to a certain number")
        print("3. Graph individual stopping times")
        print("4. Graph stopping times up to a certain number")
        option = int(input(""))

    return option

def main():
    choice = choose_option()
    
    if (choice == 2 or choice == 4):
        while True:
            try:
                total = int(input("Enter the number of generations: "))
                if type(total) is int:
                    break
            except:
                print("That's not a number. Try again.")            
    
    if choice == 1:
        while True:
            try:
                plot_hailstone_graph(int(input("Enter a hailstone number: ")))
                plt.show(block=False)
            except:
                sys.exit()
    
    if choice == 2:
        for i in range(total):
            plot_hailstone_graph(i)
        plt.show()
    
    if choice == 3:
        while True:
            try:
                plot_stop_time(int(input("Enter a hailstone number: ")))
                plt.show(block=False)
            except:
                sys.exit()
    
    if choice == 4:
        for i in range(total):
            plot_stop_time(i)
        plt.show()

main()