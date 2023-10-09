while True:
    input_string = input("Please enter a string (type 'done' to exit): ")

    if input_string.lower() == 'done':
        break

special_characters = ",.:!? "
for char in special_characters:
    input_string = input_string.replace(char, " ")

input_string = input_string.upper()
print(input_string)