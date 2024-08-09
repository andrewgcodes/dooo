def generate_code_prompt(task, data):
  return f"""Generate Python code to perform the following task:
Task: {task}
Data: {data}
Requirements:
1. You can use the following libraries: NumPy (as np), Pandas (as pd), Matplotlib (as plt), SciPy (stats), Requests, Collections (Counter, defaultdict), Itertools, Math, Statistics, Re.
2. Assign the final result to a variable named 'result'.
3. Do not include any print statements or return statements.
4. The code will be executed in a context where 'data' is already defined.
5. Do not include any markdown formatting or code block indicators.

Provide only the Python code without any explanations or formatting."""

def extract_answer_prompt(original_task, raw_result):
  return f"""Extract the essential answer from the following text, considering the original task. The answer should be minimally complete and have zero extraneous commentary.
Original task: {original_task}
Raw result: {raw_result}
Output the result as a JSON object with a single key named "answer"."""