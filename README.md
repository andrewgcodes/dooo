# Dooo
<img src="https://github.com/andrewgcodes/dooo/raw/main/dooo.png" alt="Dooo Logo" width="200"/>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/162I3A7f1RIM4d_tgEIix-yOQE25ZmQNb?usp=sharing)

Dooo makes LLMs ridiculously easy to use. There is **only one function**, do(), with nearly no abstraction. Thanks to litellm integration, do() is compatible with 100s of LLMs, including OpenAI and Anthropic's, by just changing the model name!

You shouldn't use Dooo for any conversational tasks requiring message history. Try LangChain for that.
Dooo is for fun, but might be somewhat useful!

## Installation

You can install Dooo using pip:

```
pip install dooo
```

## Usage

Here's a basic example of how to use Dooo:

```python
from dooo import set_api_key, set_default_model, do

# Set your API key. Dooo works with OpenAI, Anthropic, OpenRouter, and Hugging Face.
set_api_key('openai', 'your-api-key-here') 

# Set the default model (GPT-4o is recommended, GPT-3.5-turbo is a bit too dumb)
set_default_model('gpt-4o')

# Perform a task
result = do([1, 2, 3, 4, 5], "Calculate the mean and standard deviation")
print(result)
```

## Features

- AI-assisted task execution
- Automatic code generation for data analysis tasks
- Support for various AI providers (OpenAI, Anthropic, HuggingFace, OpenRouter)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
