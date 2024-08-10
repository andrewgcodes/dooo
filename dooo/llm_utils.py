import litellm

def make_llm_call(prompt, model):
    try:
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error calling LLM: {str(e)}")