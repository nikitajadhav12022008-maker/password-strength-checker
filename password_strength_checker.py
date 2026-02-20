#python based password strength checker:
def check_password_strength(password):
    score = 0
#length check
    if len(password) >= 8:
        score += 1
#uppercase check
    if any(char.isupper() for char in password):
        score += 1
#lowercase check
    if any(char.islower() for char in password):
        score += 1
digit check
    if any(char.isdigit() for char in password):
        score += 1
#special character check
    special_chars = "!@#$%^&*()-_+=<>?/|"
    if any(char in special_chars for char in password):
        score += 1

    return score
def show_result(score):
    if score <= 2:
        return "weak"
    elif score == 3 or score == 4:
        return "medium"
    else:
        return "strong"
 #main program   
print("=========password strength checker==============")
password = input("enter your password:")

score = check_password_strength(password)
result = show_result(score)

print("\npassword strength:",result)


