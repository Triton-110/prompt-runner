# Prompt Runner

A Python script that reads prompts from a text file sends each one to the
Gemini API and saves the responses in a JSON file

## Features
- Reads prompts from `text.txt` (blank lines are skipped)
- Calls the Gemini API for each prompt
- Saves queries and answers to `responses.json`

## Setup

1. Install requirements (gemini API):
```
   pip install -r requirements.txt
```
2. Get a free API key from Google AI Studio.
3. Replace your API key in place of "ENTER API KEY HERE" in main()


## Example output
```json
{
    "prompt_1": {
        "query": "What is an API?",
        "answer": "..."
    }
}
```

## Project structure
- `main.py`: the script
- `text.txt`: input prompts
- `responses.json`: saved output
- `requirements.txt`: requirements needed to run the program

## Notes
The API key I used is not stored in the code.