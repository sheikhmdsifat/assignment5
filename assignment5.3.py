def count_characters(input_string):
    num_count = 0
    uppercase_count = 0
    lowercase_count = 0
    other_count = 0

    for char in input_string:
        if char.isdigit():
            num_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        else:
            other_count += 1

    return num_count, uppercase_count, lowercase_count, other_count

input_string = input("Enter a string: ")
num_count, uppercase_count, lowercase_count, other_count = count_characters(input_string)

print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")
print(f"numbers: {num_count}")
print(f"other characters: {other_count}")
