

def validate_isbn10(code_string):
    # Strip spaces and dashes
    code_string = code_string.replace("-", "").replace(" ", "")
    # Make sure string argument is valid
    if len(code_string) != 10:
        return False
    if not code_string[0:8].isdigit() or not (code_string[9].isdigit() or code_string[9].lower() == "x"):
        return False

    # Initialise result to 0
    result = 0

    # Iterate through code_string
    for i in range(9):
        # for each character, multiply by a different decreasing number: 10 - x
        result = result + int(code_string[i]) * (10 - i)

    # Handle last character
    if code_string[9].lower() == "x":
        result += 10
    else:
        result += int(code_string[9])

    #print(result)  # For debugging if required

    # Return whether the isbn is valid
    if result % 11 == 0:
        return True
    else:
        return False

    # If you prefer and understand why it is equivalent
    # return result % 11 == 0
print(validate_isbn10('1-55404-295-x'))

# isbn = "123"
# assert validate_isbn10(isbn) is False
# isbn = "abc"
# assert validate_isbn10(isbn) is False
# isbn = "0136091814"
# assert validate_isbn10(isbn) is True
# isbn = "1616550416"
# assert validate_isbn10(isbn) is False
# isbn = "0553418025"
# assert validate_isbn10(isbn) is True
# isbn = "3859574859"
# assert validate_isbn10(isbn) is False
# isbn = "1-55404-295-X"
# assert validate_isbn10(isbn) is True
