import emoji


def main():
    str = input("Input: ")
    output = emoji.emojize(str, language="alias")
    print("Output: " + output)


main()
