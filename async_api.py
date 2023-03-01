import openai
openai.api_key = "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"  # supply your API key however you choose

async def create_completion():
    completion_resp = await openai.Completion.acreate(prompt="This is a test", engine="davinci")




import openai
from aiohttp import ClientSession

openai.aiosession.set(ClientSession())
# At the end of your program, close the http session
await openai.aiosession.get().close()