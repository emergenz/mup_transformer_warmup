import os
import requests
import zipfile
import argparse

def download_wikitext103(data_dir):
    url = 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-v1.zip'
    zip_path = os.path.join(data_dir, 'wikitext-103-v1.zip')
    extracted_dir = os.path.join(data_dir, 'wikitext-103')
    
    if not os.path.exists(extracted_dir):
        os.makedirs(data_dir, exist_ok=True)
        
        print("Downloading Wikitext-103 dataset...")
        response = requests.get(url, stream=True)
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
                
        print("Extracting Wikitext-103 dataset...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        
        os.remove(zip_path)
        print(f"Wikitext-103 dataset extracted to {extracted_dir}")
    else:
        print(f"Wikitext-103 dataset already exists in {extracted_dir}")
        
    return extracted_dir

def main(args):
    data_dir = download_wikitext103(args.data_dir)
    print(f"Wikitext-103 dataset ready at {data_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download and prepare Wikitext-103 dataset.')
    parser.add_argument('--data-dir', type=str, default='./data/wikitext-103',
                        help='location to save the data corpus')
    args = parser.parse_args()
    main(args)
