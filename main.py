import openai

openai.api_key = "Fill your API key here"

days = 4
place = "Paris"

prompt = f"Make me a travel plan for {days} days to {place}"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=4000,
    temperature=0.6,
    n=1,
    stop=None
)

print(str(response["choices"][0]["text"]))
