import json
import os
from google import genai

#used in this program
INPUT_FILE = "text.txt"
OUTPUT_FILE = "responses.json"
MODEL_NAME = "gemini-3.5-flash-lite"  


def read_prompts(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        cleaned_lines = []
        for line in f:
            stripped_line = line.strip()
            if stripped_line:  # We keep only lines which are not empty so we dont pass empty lines into the AI 
                cleaned_lines.append(stripped_line)
        return cleaned_lines
    

def get_responses(client, prompts):
    results = {} #creating a ditionary which will eventually be put into our response json file
    count = 1
    for prompt in prompts:
        print("Asking the prompt: ",prompt)
        #calling the API 
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents = prompt
        )
        results[f"prompt_{count}"] = {
            "query":prompt,
            "answer":response.text
        }
    return results

def save_responses(results, file_path):
    with open(file_path, "w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=4) #indent is used here because without it everything is appearing on the same line amking it unreadable


def main():
    client = genai.Client(api_key="ENTER API KEY HERE")
    try:
        prompts = read_prompts(INPUT_FILE)
    except FileNotFoundError:
        print(f"{INPUT_FILE} does not exist.")
        return
    results = get_responses(client, prompts)
    save_responses(results, OUTPUT_FILE)
    print(f"Done! Responses saved to {OUTPUT_FILE}.")




main()