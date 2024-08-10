import os
from .llm_utils import make_llm_call
from .code_execution import execute_code
from .prompts import generate_code_prompt, extract_answer_prompt

class Dooo:
    CODE_MARKER = "###PYTHON_CODE###"

    def __init__(self):
        self.default_model = None

    def set_default_model(self, model):
        self.default_model = model

    def set_api_key(self, provider, key):
        provider = provider.lower()
        if provider in ['openai', 'anthropic', 'huggingface', 'openrouter']:
            os.environ[f"{provider.upper()}_API_KEY"] = key
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def do(self, data_or_prompt, task=None, model=None):
        model = model or self.default_model
        if model is None:
            raise ValueError("No model specified. Set a default model or provide one.")

        if task is None:
            # If only one argument is provided, treat it as a prompt
            return self._perform_task(None, data_or_prompt, model)
        else:
            # If two arguments are provided, treat them as data and task
            requires_coding = self._determine_if_coding_required(task, model)

            if requires_coding:
                code = self._generate_python_code(data_or_prompt, task, model)
                result = execute_code(code, data_or_prompt)
            else:
                raw_result = self._perform_task(data_or_prompt, task, model)
                result = self._extract_answer(raw_result, task, model)

            return result

    def _perform_task(self, data, task, model):
        prompt = task if data is None else f"Perform the following task:\nTask: {task}\nData: {data}\nProvide a direct and concise answer."
        return self._make_llm_call(prompt, model)

    def _determine_if_coding_required(self, task, model):
        prompt = f"Does the following task require writing Python code to solve? Answer with 'Yes' or 'No':\n\nTask: {task}"
        response = make_llm_call(prompt, model)
        return response.lower().strip() == 'yes'

    def _generate_python_code(self, data, task, model):
        prompt = generate_code_prompt(task, data)
        return self._clean_generated_code(make_llm_call(prompt, model))

    def _clean_generated_code(self, code):
        import re
        code = re.sub(r'^```[\w]*\n|```$', '', code, flags=re.MULTILINE)
        return code.strip()

    def _perform_task(self, data, task, model):
        prompt = f"Perform the following task:\nTask: {task}\nData: {data}\nProvide a direct and concise answer."
        return make_llm_call(prompt, model)

    def _extract_answer(self, raw_result, original_task, model):
        prompt = extract_answer_prompt(original_task, raw_result)
        response = make_llm_call(prompt, model)
        try:
            import json
            json_response = json.loads(response)
            return json_response["answer"]
        except json.JSONDecodeError:
            prompt = f"""The previous attempt to extract the answer failed. Please try again to extract the essential answer from the following text, ensuring it's complete and relevant to the original task. Do not use JSON formatting.
Original task: {original_task}
Raw result: {raw_result}"""
            return make_llm_call(prompt, model).strip()