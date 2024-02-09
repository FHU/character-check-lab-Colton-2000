#Remove pass and complete the code
def check_character(word, index):
   check = word[index]
   if check.isalpha() == True:
       return 'letter'
   elif check.isdigit() == True:
       return 'number'
   elif check.isspace() == True:
       return 'white space'
   else:
       return 'unknown'

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

    #comment to resubmit