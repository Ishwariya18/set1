s=input()
if s==s[::-1]:
    print("yes")
else:
    value=s.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=s.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
