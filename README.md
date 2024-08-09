# Dooo

Dooo is a Python package for AI-assisted data analysis and task execution.

## Installation

You can install Dooo using pip:

```
pip install dooo
```

## Usage

Here's a basic example of how to use Dooo:

```python
from dooo import set_api_key, set_default_model, do

# Set your API key
set_api_key('openai', 'your-api-key-here')

# Set the default model
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