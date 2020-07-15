# Programmer: Christine Doan
# Prompt: Read numbers from file into list. Calculate and prints labels.
# Prints minimum, maximum, average, and median density
# 
def median():
    # find median
    # odd entries = middle entry
    
    # if n // 2 != 0
    #   median = data[(n-1) // 2]
    # else
    #   median = (data[(n // 2)] + data[(n // 2) - 1] / 2.0)
    # 
    
def main():
    infile = open('density.txt', 'r')

    for line in infile:
        info = line.split(' ')
        planet = info[0]
        density = float(info[1])

    print(planet, ': The density is', density)

        # prints maximum and minimum density
    print('The maximum is: ', max(density), 'and the minimum is: ', min(density))
main()

    
