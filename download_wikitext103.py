import os
from datasets import load_dataset

# Define the directory where the data will be saved
data_dir = './data/wikitext-103'
os.makedirs(data_dir, exist_ok=True)

# Load the Wikitext-103 dataset
dataset = load_dataset('wikitext', 'wikitext-103-v1')

# Function to save the dataset to a text file
def save_dataset(split, filename):
    with open(filename, 'w', encoding='utf8') as f:
        for line in dataset[split]['text']:
            if line.strip():
                f.write(line.strip() + '\n')

# Save the train, validation, and test splits
save_dataset('train', os.path.join(data_dir, 'train.txt'))
save_dataset('validation', os.path.join(data_dir, 'valid.txt'))
save_dataset('test', os.path.join(data_dir, 'test.txt'))

print(f"Data saved to {data_dir}")
