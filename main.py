import os

from dotenv import load_dotenv
from google import genai
import argparse 

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    parser = argparse.ArgumentParser(description = "CLI-Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt,
    )
    
    if response.usage_metadata is None:
        raise RuntimeError("No prompt metadata found")
    else:   
        metadata_dict = response.usage_metadata
        prompt_tokens = metadata_dict.prompt_token_count
        response_tokens = metadata_dict.candidates_token_count


    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

