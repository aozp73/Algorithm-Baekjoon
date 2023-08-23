while True :
    
    try :
        words = list(input())
        lower , upper, num, blank = 0, 0, 0, 0
        for word in words:
            if word == " " :
                blank += 1
            elif word.isupper() :
                upper += 1
            elif word.islower() :
                lower += 1
            elif word.isdigit() :
                num += 1
        print(lower,upper,num,blank)
    except EOFError :
        break