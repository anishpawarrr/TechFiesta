# from env import *

def ask(image_url, key, sys_prompt, user_prompt, model, user_query = ""):
    from huggingface_hub import InferenceClient
    client = InferenceClient(api_key=key)
    messages = [{"role" : "system", "content" : [{"type":"text", "text":sys_prompt}]},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt + user_query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ]

    completion = client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=3500
    )

    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content
    

# image_url = "https://media.istockphoto.com/id/471457370/photo/x-ray-image-of-broken-forearm-ap-and-lateral-view.jpg?s=612x612&w=0&k=20&c=x9K8ITR-C7FI70xMoCOS2zEi1915bgdj0HYVyZbM81g="

# ask(image_url)