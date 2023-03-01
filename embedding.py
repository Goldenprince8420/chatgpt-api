import openai
openai.api_key = "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"  # supply your API key however you choose

# choose text to embed
text_string = "sample text"

# choose an embedding
model_id = "text-similarity-davinci-001"

# compute the embedding of the text
embedding = openai.Embedding.create(input=text_string, engine=model_id)['data'][0]['embedding']