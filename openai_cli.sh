# list engines
openai api engines.list

# create a completion
openai api completions.create -e ada -p "Hello world"

# generate images via DALL·E API
openai api image.create -p "two dogs playing chess, cartoon" -n 1