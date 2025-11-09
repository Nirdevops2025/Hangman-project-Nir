def get_input():
    ltr=input("Enter your letter: ")
    ltr=ltr.lower()
    if len(ltr)==1:
        if ltr.isalpha():
            return ltr
        else:
            ltr = False
            return ltr
    else:
        ltr = False
        return ltr

if __name__=='__main__':
    get_input()
