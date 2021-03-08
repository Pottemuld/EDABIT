def number_length(number):
    counter = 0;
    number_list = [int(x) for x in str(number)]
    for i in number_list:
        counter = counter + 1
    
    print(counter)

number_length(10)
number_length(5000)
number_length(0)