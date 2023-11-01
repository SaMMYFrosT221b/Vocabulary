import pandas as pd
import csv


class Vocab:
    def add_words(word, mean):
        new_row = [word, mean]
        with open("word.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_row)

    def see():
        df = pd.read_csv("word.csv")
        print(df)

    def check():
        df = pd.read_csv("word.csv")
        for i in df["Words"]:
            if i == new_word:
                return True
        return False


if __name__ == "__main__":
    Word = Vocab()

    print("To see: 1, To exit: -1")

    while True:
        new_word = input("Enter the word: ")

        if Word.check(new_word):
            print(f"{new_word} Already Exist")
            continue

        if new_word == "-1":
            break

        if new_word == "1":
            Word.see()

        new_mean = input("Enter the meaning: ")

        Word.add_words(new_word, new_mean)
