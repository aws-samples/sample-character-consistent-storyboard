import json
import random
from botocore.exceptions import ClientError
import time


MAX_RETRIES = 50
INITIAL_BACKOFF = 5

def call_nova_lite(bedrock_client, user_prompt, system_prompt=None):

    retries = 0
    backoff = INITIAL_BACKOFF

    body_json = {
        "inferenceConfig": {
            "max_new_tokens": 2000
        },
        "messages": [{"role": "user", "content": [{"text": user_prompt}]}],
    }

    if system_prompt:
        body_json["system"] = [{"text": system_prompt}]

    input_data = {
        "modelId": "amazon.nova-lite-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps(body_json)
    }

    while retries < MAX_RETRIES:
        try:
            response = bedrock_client.invoke_model(**input_data)
            response_body = json.loads(response["body"].read().decode())
            return response_body["output"]["message"]["content"][0]["text"]
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print(f"Error: {error_code}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            retries += 1
            backoff += 1
    
    raise Exception("Max retries reached. Unable to invoke model.")


def generate_text(bedrock_client, model_id, user_prompt, system_prompt):
    
    retries = 0
    backoff = INITIAL_BACKOFF

    messages = [
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": "{"},
    ]

    input_data = {
        "modelId": model_id,
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 20000,
                "messages": messages,
                "system": system_prompt if system_prompt else "",
                "temperature": 0.3,
                "top_k": 40,
                "top_p": 0.9,
            }
        ),
    }
    while retries < MAX_RETRIES:
        try:
            response = bedrock_client.invoke_model(**input_data)
            response_body = json.loads(response["body"].read().decode())
            response_json_string = "{" + response_body["content"][0]["text"]
            response_body_json = json.loads(response_json_string)
            return response_body_json
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print(f"Error: {error_code}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            retries += 1
            backoff += 1
    
    raise Exception("Max retries reached. Unable to invoke model.")


def get_random_seed():
    return random.randint(0, 2147483646)


def get_task_status(bedrock_client, invocation_arn):
    response = bedrock_client.get_async_invoke(
        invocationArn=invocation_arn
    )
    return response["status"]


def generate_images(bedrock_client, model_id, user_prompt, negative_prompt, resolution=[1280,720], seed=None, image_count=3):
    retries = 0
    backoff = INITIAL_BACKOFF
    
    if seed is None:
        seed = get_random_seed()

    while retries < MAX_RETRIES:
        try:
            payload = {
                "taskType": "TEXT_IMAGE",
                "textToImageParams": {
                    "text": user_prompt,
                    "negativeText": negative_prompt,
                },
                "imageGenerationConfig": {
                    "seed": seed,
                    "quality": "standard",
                    "numberOfImages": image_count,
                    "width": resolution[0],
                    "height": resolution[1],
                },
            }
        
            response = bedrock_client.invoke_model(
                modelId=model_id, body=json.dumps(payload)
            )
        
            model_response = json.loads(response["body"].read())
            return model_response["images"]
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print(f"Error: {error_code}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            retries += 1
            backoff += 1
    
    raise Exception("Max retries reached. Unable to invoke model.")

def generate_videos(bedrock_client, model_id, user_prompt, image_bytes, output_bucket, seed=None):
    retries = 0
    backoff = INITIAL_BACKOFF
    
    if seed is None:
        seed = get_random_seed()
        
    model_input = {
        "taskType": "TEXT_VIDEO",
        "textToVideoParams": {
            "text": user_prompt,
            "images": [{ "format": "png", "source": { "bytes": image_bytes} }]
        },
        "videoGenerationConfig": {
            "durationSeconds": 6,
            "fps": 24,
            "dimension": "1280x720",
            "seed": seed
        }
    }

    # Start async invocation with retries
    while retries < MAX_RETRIES:
        try:
            invocation = bedrock_client.start_async_invoke(
                modelId=model_id,
                modelInput=model_input,
                outputDataConfig={"s3OutputDataConfig": {"s3Uri": f"s3://{output_bucket}"}}
            )
            
            invocation_arn = invocation["invocationArn"]
            s3_prefix = invocation_arn.split('/')[-1]
            s3_location = f"s3://{output_bucket}/{s3_prefix}"
            print(f"\nS3 URI: {s3_location}")
            
            # Poll for completion
            while True:
                status = get_task_status(bedrock_client, invocation_arn)
                print(f"Status: {status}")
                
                if status == "Completed":
                    return s3_location
                elif status in ["Failed"]:
                    print(f"Task failed with status: {status}")
                    raise Exception(f"Video generation failed with status: {status}")
                    
                time.sleep(10)
                
        except ClientError as e:
            print(e)
            error_code = e.response['Error']['Code']
            print(f"Error: {error_code}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            retries += 1
            backoff += 1
    
    raise Exception("Max retries reached. Unable to generate video.")


def invoke_model_with_retry(modelId, body):
    retries = 0
    backoff = INITIAL_BACKOFF

    while retries < MAX_RETRIES:
        try:
            response = bedrock_client.invoke_model(
                body=body, modelId=modelId, accept=accept, contentType=contentType
            )
            return response
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print(f"Error: {error_code}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            retries += 1
            backoff += 1
    
    raise Exception("Max retries reached. Unable to invoke model.")
