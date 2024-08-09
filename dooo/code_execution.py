import textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import requests
from collections import Counter, defaultdict
import itertools
import math
import statistics
import re

def execute_code(code, data):
    wrapped_code = f"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import requests
from collections import Counter, defaultdict
import itertools
import math
import statistics
import re

def _dooo_execute(data):
{textwrap.indent(code, '    ')}
    return result

result = _dooo_execute(data)
"""
    global_vars = {
        '__builtins__': __builtins__,
        'np': np,
        'pd': pd,
        'plt': plt,
        'stats': stats,
        'requests': requests,
        'Counter': Counter,
        'defaultdict': defaultdict,
        'itertools': itertools,
        'math': math,
        'statistics': statistics,
        're': re
    }
    local_vars = {'data': data}
    try:
        exec(wrapped_code, global_vars, local_vars)
        result = local_vars.get('result', None)
    except Exception as e:
        raise Exception(f"Error in code execution: {str(e)}")
    return result