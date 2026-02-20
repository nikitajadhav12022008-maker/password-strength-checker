def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

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
    
print("=========password strength checker==============")
password = input("enter your password:")

score = check_password_strength(password)
result = show_result(score)

print("\npassword strength:",result)
