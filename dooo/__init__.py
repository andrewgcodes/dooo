from .core import Dooo

# Create a global instance
dooo = Dooo()

# Convenience functions
def set_default_model(model):
    dooo.set_default_model(model)

def set_api_key(provider, key):
    dooo.set_api_key(provider, key)

def do(data, task, model=None):
    return dooo.do(data, task, model)