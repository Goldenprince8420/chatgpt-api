import openai
openai.api_key = "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"  # supply your API key however you choose

moderation_resp = openai.Moderation.create(input="Here is some perfectly innocuous text that follows all OpenAI content policies.")