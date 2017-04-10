try:
    print("Enter the filename")
    name = input()
    file = open(name, 'w')
    # display(file)
except:
    print("Cannot open the file")
    print("Enter the filename")
    name = input()
    file = open(name, 'w')
    # display(file)
finally:
    file.close()