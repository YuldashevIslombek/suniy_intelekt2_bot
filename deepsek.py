from openai import AsyncClient

async def generate_response(prompt, api_key):
    client = AsyncClient(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    completion = await client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content



# generate_response()
