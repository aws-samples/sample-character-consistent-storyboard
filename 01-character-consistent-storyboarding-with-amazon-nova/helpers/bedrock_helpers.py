import json
import random
from botocore.exceptions import ClientError
import os
import time


MAX_RETRIES = 50
INITIAL_BACKOFF = 5


def generate_text(bedrock_client, user_prompt, system_prompt):
    retries = 0
    backoff = INITIAL_BACKOFF

    messages = [
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": "{"},
    ]

    input_data = {
        "modelId": "anthropic.claude-3-5-sonnet-20240620-v1:0",
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


def generate_images(bedrock_client, user_prompt, negative_prompt, resolution=[1280,720], seed=None, image_count=3):
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
                modelId="amazon.nova-canvas-v1:0", body=json.dumps(payload)
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
