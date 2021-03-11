def encrypt(string):
    # Step 1
    reversed = string[::-1]
    
    # Step 2
    reversed = reversed.replace("a", "0")
    reversed = reversed.replace("e", "1")
    reversed = reversed.replace("i", "2")
    reversed = reversed.replace("o", "2")
    reversed = reversed.replace("u", "3")
    
    # Step 3
    reversed += ("aca")
    
    print(reversed)

encrypt("apple")
encrypt("karaca")
encrypt("burak")
encrypt("alpaca")