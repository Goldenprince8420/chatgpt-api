import openai
openai.api_key = "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"

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)