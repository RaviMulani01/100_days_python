PLACEHOLDER = "[name]"


with open("../Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()


with open("../Letters/starting_letter.txt") as letter:

    letter_formate = letter.read()

    for name in name_list:

        stripped_name = name.strip()

        new_letter = letter_formate.replace(PLACEHOLDER, stripped_name)
        
        file_name = f"letter_for_{stripped_name}.txt"

        with open(file_name, "w") as invitation_letter:
            invitation_letter.write(new_letter)


    