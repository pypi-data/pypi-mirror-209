# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['llambda', 'llambda.llm']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0', 'openai[datalib]>=0.27.4,<0.28.0']

setup_kwargs = {
    'name': 'llambda',
    'version': '0.1.0a1',
    'description': '',
    'long_description': '# LLambda\n\nLLambda is a library that makes it easy to integrate Large Language Models (LLM) and Python. It enables calling multiple pre-defined functions using natural language and executing them with appropriate arguments.\n\n## Installation\n\nYou can easily install LLambda using pip:\n\n```\npip install llambda\n```\n\n## Usage\n\nHere is a basic usage example. The following code defines two functions and calls them using natural language.\n\n### Registering Functions with Decorators\n\n```python\nfrom llambda import register\n\n@register\ndef make_coffee(n_cups: int) -> str:\n    """\n    Make coffee of the amount you want.\n    Can\'t make tea.\n    """\n    return "☕" * n_cups\n\n\n@register\ndef send_email(recipient_name: str, subject: str, content: str, your_name: str) -> str:\n    """\n    Send an email to someone.\n    """\n    return f"Sent email to {recipient_name} with subject \'{subject}\'\\nand content \'{content}\' from {your_name}"\n\n```\nNow we have two functions. Let\'s call them using natural language:\n\n```python\nfrom llambda import create_llambda, set_openai_api_key\n\nset_openai_api_key("Your OpenAI API Key")\n\nllambda = create_llambda()\n\nprint(llambda("I want to drink 3 cups of coffee"))\n# ☕☕☕\nprint(llambda("Write an email in which GPT shares the method for training neural networks with Adam."))\n# Sent email to Adam with subject \'Training Neural Networks\'\n# and content\'Hey there! I wanted to share my method for training neural networks. Let\'s discuss soon!\' from GPT\n```\nLLambda automatically recognizes the functions and their arguments, and calls the appropriate function with the arguments inferred from the instruction.\n```python\nprint(llambda("I want to drink 3 cups of tea"))\n# NotImplementedError: Can\'t make tea.\n```\nLLambda raises `NotImplementedError` when it cannot find a function that matches the instruction.\n\n### Directly Passing Functions\n\nIn addition to using the `@register` decorator, you can also directly pass the functions to `create_llambda`.\n\n```python\n\nllambda = create_llambda([make_coffee, send_email])\n\nprint(llambda("I want to drink 3 cups of coffee"))\n# ☕☕☕\n```\n\n## Custom Context\n\n### Using ContextVars Class\n\nFunctions\n\n can access context variables by defining a subclass of `ContextVars`. The class variables of this subclass will be automatically recognized as context variables:\n\n```python\nclass Context(ContextVars):\n    your_name: str = "GPT"\n    your_friends: list[str] = ["Adam", "Bert"]\n\nllambda = create_llambda(context=Context)\n\nprint(llambda("Share with your friend about your method for training neural networks"))\n# Sent email to Adam with subject \'Training Neural Networks\'\n# and content\'Hey there! I wanted to share my method for training neural networks. Let\'s discuss soon!\' from GPT\n```\n\n### Directly Passing ContextVar Instances\n\nYou can also pass the context directly as a list of `ContextVar` instances:\n\n```python\ncontext_vars = [\n    ContextVar("your_name", "str", "GPT"),\n    ContextVar("your_friends", "list[str]", ["Adam", "Bert"])\n]\n\nllambda = create_llambda(context=context_vars)\n```\n',
    'author': 'Ryuta-Yamamoto',
    'author_email': '43087138+Ryuta-Yamamoto@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
