#Create a Mail Merge Project

PLACEHOLDER = "[name]"

with open("100-days-of-code-python/day-24/Mail Merge Project/Input/Names/invited_names.txt") as names_file:
    namelist = names_file.readlines()

for name in namelist:
    stripped_name = name.strip()
    with open("100-days-of-code-python/day-24/Mail Merge Project/Input/Letters/starting_letter.txt") as read_file:
        letter_contents = read_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"100-days-of-code-python/day-24/Mail Merge Project/Output/ReadyToSend/{stripped_name}.txt", "w") as write_file:
                write_file.write(new_letter)