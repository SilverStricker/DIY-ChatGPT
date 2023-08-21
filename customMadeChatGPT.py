import openai

openai.api_key = "openAPIKey"
while True:
    prompt = input("Enter command/question\n")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(completion.choices[0].message.content)
