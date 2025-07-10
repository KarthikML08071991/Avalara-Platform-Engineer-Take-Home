# Import required libraries
import requests
import argparse

# Define a function to get the word definition from Merriam-Webster API
def get_definition(word, api_key):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        pronunciation = data[0]['phonetic']
        return definition, pronunciation
    else:
        return None, None

# Define the main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Merriam-Webster Dictionary CLI Tool")
    parser.add_argument("word", help="the word to look up")
    parser.add_argument("-k", "--api_key", help="Merriam-Webster API key", required=True)
    args = parser.parse_args()

    # Get the word definition
    definition, pronunciation = get_definition(args.word, args.api_key)

    if definition is not None and pronunciation is not None:
        print(f"{pronunciation}: {definition}")
    else:
        print("Word not found or API error")

if __name__ == "__main__":
    main()
