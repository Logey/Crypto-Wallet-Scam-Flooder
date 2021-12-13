import requests, random, time

def main():
    url = "https://www.confirmyourmetsmask.com/"
    wordsSite = "https://www.mit.edu/~ecprice/wordlist.10000"

    words_ = requests.get(wordsSite)
    words = words_.content.splitlines()

    while True:
        wordList = []
        for i in range(12):
            word = random.choice(words).decode("utf-8")
            wordList.append(word)

        data = {
            "submitted": "true",
            "passphrase": ",".join(wordList)
        }

        response = requests.post(url, data=data).text
        if ("You successfully verified your wallet" in response):
            print(data["passphrase"])
            time.sleep(random.randint(1,10))
        else:
            print(response)
            break

if __name__ == "__main__":
    main()