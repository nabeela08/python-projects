PLACEHOLDER = "[name]"

with open(".\mail-merging\invited_names.txt") as names_file:
    # names = names_file.read()
    names = names_file.readlines()
    print(names)

with open(".\mail-meging\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(".\mail-merging\ReadytoSend\letter_for_{stripped_name}.txt", mode="w" ) as completed_letter:
            completed_letter = completed_letter.write(new_letter)
            print(completed_letter)
