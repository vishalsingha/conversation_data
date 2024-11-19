import tqdm
import json
import pandas as pd
import pickle  # You need to import pickle

def save_parsed_conversation(df, save_filename="final_conv"):
    parsed_output = []
    
    # Iterate over the 'response' column in the dataframe
    for out in tqdm.tqdm(df["response"].values):
        try:
            # Extract the JSON string from between the '```json' and '```' markers
            out = out.split('```json')[-1]
            out = out.split('\n```')[0]
            # Parse the JSON string into a Python dictionary
            tmp_json = json.loads(out)
            parsed_output.extend([v for k, v in tmp_json.items()])
        except Exception as e:  # Use except to handle exceptions
            print(f"Error parsing response: {e}")
            pass  # Skip this iteration and continue with the next one

    print(f"Conversation saved: {len(parsed_output)} items")
    
    # Save the parsed list to a pickle file
    with open(f'{save_filename}.pkl', 'wb') as file:
        pickle.dump(parsed_output, file)
