def most_frequent(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    print("{}\n".format(str(frequencies)))
      
s = str(input("Please enter a string: "))
most_frequent(s)
