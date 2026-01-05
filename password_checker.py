while True:
    password=input("Enter the password=")
    has_upper=False
    has_digit=False
    has_spl=False
    spl="!@#$%^&*()+-"
    if len(password)>=8:
        for ch in password:
            if ch.isupper():
                has_upper=True
            elif ch.isdigit():
                has_digit=True
            elif ch in spl:
                has_spl=True
        if has_upper and has_digit and has_spl:
            print("strong password")
            break
        else:
            print("weak password")
    else:
        print("password too short")
    
