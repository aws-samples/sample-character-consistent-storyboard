import json
import os
import boto3
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse
from tqdm import tqdm
from PIL import Image
from typing import List, Dict

s3_client = boto3.client('s3')

def upload_to_s3(file_path: str, bucket: str, prefix: str) -> str:
    
    file_name = os.path.basename(file_path)
    s3_key = f"{prefix.rstrip('/')}/{file_name}"
    
    try:
        s3_client.upload_file(file_path, bucket, s3_key)
        return f"s3://{bucket}/{s3_key}"
    except Exception as e:
        print(f"Error uploading {file_path}: {str(e)}")
        return None
        
def check_image_dimensions(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return 1000 <= width <= 4096 and 1000 <= height <= 4096
    except Exception as e:
        print(f"Error checking dimensions for {image_path}: {str(e)}")
        return False

def process_folders(
    folder_paths: List[str],
    s3_bucket: str,
    s3_prefix: str,
    max_workers: int = 10
) -> List[Dict]:
    """
    Process multiple folders containing JSONL and image files, upload images to S3,
    and update image references.
    """

    all_data = []
    total_uploads = 0
    
    # First, count total number of uploads needed
    for folder_path in folder_paths:
        jsonl_file = next(Path(folder_path).glob("*.jsonl"))
        with open(jsonl_file, 'r') as f:
            total_uploads += sum(1 for _ in f)

    # Create progress bars
    folder_pbar = tqdm(
        total=len(folder_paths),
        desc="Processing folders",
        position=0
    )
    
    upload_pbar = tqdm(
        total=total_uploads,
        desc="Uploading images",
        position=1,
        leave=True
    )

    def get_filename_from_s3_path(s3_path: str) -> str:
        """Extract filename from S3 path"""
        return os.path.basename(urlparse(s3_path).path)

    def upload_to_s3(image_path: str, folder_path: str, original_s3_path: str) -> str:
        """Upload single image to S3 and return the new S3 path"""
        image_name = get_filename_from_s3_path(original_s3_path)
        s3_key = f"{s3_prefix}/{image_name}"
        full_image_path = os.path.join(folder_path, image_path)
        
        try:
            if os.path.exists(full_image_path):
                s3_client.upload_file(
                    full_image_path,
                    s3_bucket,
                    s3_key
                )
                upload_pbar.update(1)
                return f"s3://{s3_bucket}/{s3_key}"
            else:
                print(f"\nFile not found: {full_image_path}")
                upload_pbar.update(1)
                return None
        except Exception as e:
            print(f"\nError uploading {full_image_path}: {str(e)}")
            upload_pbar.update(1)
            return None

    for folder_path in folder_paths:
        jsonl_file = next(Path(folder_path).glob("*.jsonl"))
        
        # Load JSONL data
        data = []
        with open(jsonl_file, 'r') as f:
            for line in f:
                data.append(json.loads(line.strip()))
        
        # Create mapping of image references to upload tasks
        upload_tasks = {}
        for item in data:
            original_s3_path = item['image-ref']
            filename = get_filename_from_s3_path(original_s3_path)

            if check_image_dimensions(os.path.join(folder_path, filename)):
                upload_tasks[original_s3_path] = (filename, folder_path, original_s3_path)
        
        # Upload images concurrently
        s3_paths = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_path = {
                executor.submit(upload_to_s3, filename, folder_path, original_s3_path): original_s3_path
                for original_s3_path, (filename, folder_path, original_s3_path) in upload_tasks.items()
            }
            
            for future in future_to_path:
                original_s3_path = future_to_path[future]
                s3_paths[original_s3_path] = future.result()
        
        # Update image references with new S3 paths
        new_data = []
        for item in data:
            if item['image-ref'] in s3_paths and s3_paths[item['image-ref']] is not None:
                new_item = dict()
                new_item['image-ref'] = s3_paths[item['image-ref']]
                new_item['caption'] = item['caption']
                new_item['id'] = folder_path
                new_data.append(new_item)
                
        all_data.extend(new_data)
        folder_pbar.update(1)
    
    # Close progress bars
    folder_pbar.close()
    upload_pbar.close()
    
    return all_data