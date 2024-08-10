from .core import Dooo

dooo = Dooo()

def set_default_model(model):
    dooo.set_default_model(model)

def set_api_key(provider, key):
    dooo.set_api_key(provider, key)

def do(data_or_prompt, task=None, model=None):
    return dooo.do(data_or_prompt, task, model)