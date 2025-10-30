# kaggle_downloader.py
import os
import kaggle
from dotenv import load_dotenv
import json
def setup_kaggle():
    """Set up Kaggle API credentials"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Get credentials from environment variables
    kaggle_username = os.getenv('KAGGLE_USERNAME')
    kaggle_key = os.getenv('KAGGLE_KEY')
    
    if not kaggle_username or not kaggle_key:
        raise ValueError("Kaggle credentials not found in environment variables")
    
    # Create .kaggle directory if it doesn't exist
    kaggle_dir = os.path.expanduser('~/.kaggle')
    os.makedirs(kaggle_dir, exist_ok=True)
    
    # Create kaggle.json file
    kaggle_json = {
        "username": kaggle_username,
        "key": kaggle_key
    }
    
    kaggle_json_path = os.path.join(kaggle_dir, 'kaggle.json')
    with open(kaggle_json_path, 'w') as f:
        json.dump(kaggle_json, f)
    
    # Set appropriate permissions
    os.chmod(kaggle_json_path, 0o600)
    
    print("Kaggle credentials configured successfully!")

def download_kaggle_dataset(dataset_name, download_path='./data'):
    """Download a dataset from Kaggle"""
    # Setup credentials first
    setup_kaggle()
    
    # Ensure download directory exists
    os.makedirs(download_path, exist_ok=True)
    
    try:
        # Download the dataset
        kaggle.api.dataset_download_files(
            dataset_name, 
            path=download_path, 
            unzip=True
        )
        print(f"Dataset '{dataset_name}' downloaded successfully to '{download_path}'")
        return True
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        return False