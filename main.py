import os 
import json
from google import genai

#opening a client using our api key to authenicate the connection
client = genai.Client(api_key = "ENTER YOUR API KEY HERE")

#opening text files and extracting the needed text and putting htem into a list 
prompts = []
try:
    with open("text.txt", "r" , encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line: #this will check the line is not empty so that we dont pass empty prompts 
                prompts.append(clean_line)
except FileNotFoundError: 
    print("File does not exist")
else:
    # print (prompts)
    results = {} #creating a ditionary which will eventually be put into our response json file
    count = 1
    for prompt in prompts:
        print("Asking the prompt: ",prompt)
        #calling the API 
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents = prompt
        )
        results[f"prompt_{count}"] = {
            "query":prompt,
            "answer":response.text
        }

        count += 1

    with open("responses.json","w",encoding = "utf-8") as f2:
        json.dump(results, f2, indent=4) 
        #indent is used here because without it everything is appearing on the same line amking it unreadable


    print("Done! The responses have been added to the responses.json file in the current directory")

    ifDisplay = input("Do you want to display the answers here (Y/N): ")
    if ifDisplay.upper() == "Y":
        with open("responses.json", "r", encoding="utf-8") as f3:
            data = json.load(f3)

        total = len(data)

        while True:
            print("\nQuestions:")
            for i in range(1, total + 1):
                key = "prompt_" + str(i)
                print(i, ".", data[key]["query"])
            print("0 . Exit")

            choice = input("\nPick a number: ")

            if choice == "0":
                print("Done!")
                break

            key = "prompt_" + choice
            if key in data:
                print("\nQuestion:", data[key]["query"])
                print("\nAnswer:", data[key]["answer"])
            else:
                print("Invalid choice, try again.")


