import json
import random

def generate_text(bedrock_client, user_prompt, system_prompt):

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

        try:
            response = bedrock_client.invoke_model(**input_data)
            response_body = json.loads(response["body"].read().decode())
            response_json_string = "{" + response_body["content"][0]["text"]
            response_body_json = json.loads(response_json_string)
            return response_body_json
        except Exception as error:
            print("Error calling Bedrock:", error)
            raise error


def get_random_seed():
    return random.randint(0, 2147483646)

def generate_images(bedrock_client, user_prompt, negative_prompt, resolution=[1024,576], seed=None, image_count=3):
    if seed is None:
        seed = get_random_seed()
        
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
