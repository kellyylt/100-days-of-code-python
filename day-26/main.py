import pandas

#Read in dataframe
nato_df = pandas.read_csv("100-days-of-code-python/day-26/nato_phonetic_alphabet.csv")

#Dataframe to dictionary
nato_dic = {row.letter: row.code for (index,row) in nato_df.iterrows()}

#Prompt user input
user_input = input("Enter a word: ").upper()

#Create list
nato_list = [nato_dic[letter] for letter in user_input]

print(nato_list)