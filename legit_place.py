import openai

openai.api_key = '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'

place = "Lkvgdotlv"

prompt = f"Answer in only one word. Yes or No. Is {place} a real place?"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=4000,
    temperature=0.6,
    n=1,
    stop=None
)

print(response["choices"][0]["text"].strip())
