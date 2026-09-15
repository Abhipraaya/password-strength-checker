import string

def checkCommon(password):
    with open('100k-most-used-passwords-NCSC.txt', 'r') as f:
        commonPasswords = f.read().splitlines()
    if password in commonPasswords:
        return True
    return False

def passwordStrength(password):
    score = 0
    length = len(password)

    upperCase = any(c.isupper() for c in password)
    lowerCase = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = sum([upperCase + lowerCase + special + digits])

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters) - 1

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

def feedback(password):
    if checkCommon(password):
        return "Password was found in a common password list"

    strength, score = passwordStrength(password)

    return f"Password strength: {strength} (Score: {score}/7)\n"

password = input("Enter the password: ")
print(feedback(password))