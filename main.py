from dooo import set_api_key, set_default_model, do
import os
from dotenv import load_dotenv
load_dotenv()

# Set API key
set_api_key('openai', os.environ['OPENAI_API_KEY'])

# Set default model (we recommend GPT-4o)
set_default_model("gpt-4o")

# Code example
data = [1, 2, 3, 4, 5]
result = do(data, "Calculate the mean and standard deviation using NumPy")
print(result)
print("data type:", type(result))

# Translation example
sentence = "the olympic games originated in greece"
translation = do(sentence, "translate to japanese")
print(translation)