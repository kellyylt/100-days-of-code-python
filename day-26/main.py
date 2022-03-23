import pandas

#Read in dataframe
nato_df = pandas.read_csv("day-26/nato_phonetic_alphabet.csv")

#Dataframe to dictionary
nato_dic = {row.letter: row.code for (index,row) in nato_df.iterrows()}

#Create list
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dic[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()