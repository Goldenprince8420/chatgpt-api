import openai
import matplotlib.pyplot as plt
openai.api_key = "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"  # supply your API key however you choose

image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")
