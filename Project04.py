def mad_libs():
    print("Welcome to Mad Libs!")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    story = f"One day, a {adjective} {noun} decided to {verb} {adverb}."
    print("\nYour Mad Lib story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
