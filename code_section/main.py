from tqdm import tqdm
import time
import wikipedia

def main():

    val = input("Enter your search: ")
    t = wikipedia.page(val).url
    with open('urlsearchhistory.txt', 'a') as file:
        file.write(t + "\n")
    for _ in tqdm(range(100), desc="Writing..."):
        time.sleep(0.001)
    print("Done")


if __name__ == "__main__":
    main()
