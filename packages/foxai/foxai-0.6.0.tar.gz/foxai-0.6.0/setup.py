# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foxai',
 'foxai.callbacks',
 'foxai.cli',
 'foxai.explainer',
 'foxai.explainer.computer_vision',
 'foxai.explainer.computer_vision.algorithm',
 'foxai.explainer.computer_vision.object_detection']

package_data = \
{'': ['*']}

install_requires = \
['captum>=0.5.0,<1.0.0',
 'hydra-core>=1.3.1,<2.0.0',
 'numpy>=1.21.4,<2.0.0',
 'opencv-python>=4.7.0.68,<5.0.0',
 'pandas>=1.1.0,<2.0.0',
 'pytorch-lightning>=1.5.0,<2.0.0',
 'seaborn>=0.12.2,<0.13.0',
 'single-source>=0.3.0,<1.0.0',
 'torch>=1.12.1,<2.0.0',
 'wandb>=0.13.7,<1.0.0']

entry_points = \
{'console_scripts': ['foxai-wandb-updater = foxai.cli.experiment_update:main']}

setup_kwargs = {
    'name': 'foxai',
    'version': '0.6.0',
    'description': 'Model Interpretability for PyTorch.',
    'long_description': '# FoXAI\n\nFoXAI simplifies the application of e**X**plainable **AI** algorithms to explain the\nperformance of neural network models during training. The library acts as an\naggregator of existing libraries with implementations of various XAI algorithms and\nseeks to facilitate and popularize their use in machine learning projects.\n\nCurrently, only algorithms related to computer vision are supported, but we plan to\nadd support for text, tabular and multimodal data problems in the future.\n\n## Table of content:\n* [Installation](#installation)\n    * [GPU acceleration](#gpu-acceleration)\n    * [Manual installation](#manual-installation)\n* [Getting started](#getting-started)\n* [Development](#development)\n    * [Requirements](#requirements)\n    * [CUDA](#cuda)\n    * [pyenv](#pyenv)\n    * [Poetry](#poetry)\n    * [pre-commit hooks](#pre-commit-hooks-setup)\n    * [Note](#note)\n        * [Artifacts directory structure](#artifacts-directory-structure)\n        * [Examples](#examples)\n\n# Installation\n\nInstallation requirements:\n* `Python` >=3.7.2,<3.11\n\n**Important**: For any problems regarding installation we advise to refer first to our [FAQ](FAQ.md).\n\n## GPU acceleration\n\nTo use the torch library with GPU acceleration, you need to install\na dedicated version of torch with support for the installed version of CUDA\ndrivers in the version supported by the library, at the moment `torch>=1.12.1,<2.0.0`.\nA list of `torch` wheels with CUDA support can be found at\n[https://download.pytorch.org/whl/torch/](https://download.pytorch.org/whl/torch/).\n\n## Manual installation\n\nIf you would like to install from the source you can build a `wheel` package using `poetry`.\nThe assumption is that the `poetry` package is installed. You can find how to install\n`poetry` [here](#poetry). To build `wheel` package run:\n\n```bash\ngit clone https://github.com/softwaremill/FoXAI.git\ncd FoXAI/\npoetry install\npoetry build\n```\n\nAs a result you will get `wheel` file inside `dist/` directory that you can install\nvia `pip`:\n```bash\npip install dist/foxai-x.y.z-py3-none-any.whl\n```\n\n# Getting started\n\nTo use the FoXAI library in your ML project, simply add an additional object of type\n`WandBCallback` to the `Trainer`\'s callback list from the `pytorch-lightning` library.\nCurrently, only the Weights and Biases tool for tracking experiments is supported.\n\nBelow is a code snippet from the example (`example/mnist_wandb.py`):\n\n```python\nimport torch\nfrom pytorch_lightning import Trainer\nfrom pytorch_lightning.loggers import WandbLogger\n\nimport wandb\nfrom foxai.callbacks.wandb_callback import WandBCallback\nfrom foxai.context_manager import CVClassificationExplainers, ExplainerWithParams\n\n    ...\n    wandb.login()\n    wandb_logger = WandbLogger(project=project_name, log_model="all")\n    callback = WandBCallback(\n        wandb_logger=wandb_logger,\n        explainers=[\n            ExplainerWithParams(\n                explainer_name=CVClassificationExplainers.CV_INTEGRATED_GRADIENTS_EXPLAINER\n            ),\n            ExplainerWithParams(\n                explainer_name=CVClassificationExplainers.CV_GRADIENT_SHAP_EXPLAINER\n            ),\n        ],\n        idx_to_label={index: index for index in range(0, 10)},\n    )\n    model = LitMNIST()\n    trainer = Trainer(\n        accelerator="gpu",\n        devices=1 if torch.cuda.is_available() else None,\n        max_epochs=max_epochs,\n        logger=wandb_logger,\n        callbacks=[callback],\n    )\n    trainer.fit(model)\n```\n\n## CLI\n\nA CLI tool is available to update the artifacts of an experiment tracked in\nWeights and Biases. Allows you to create XAI explanations and send them to\nW&B offline. This tool is using `hydra` to handle the configuration of `yaml` files.\nTo check options type:\n\n```bash\nfoxai-wandb-updater --help\n```\n\nTypical usage with configuration in `config/config.yaml`:\n```bash\nfoxai-wandb-updater --config-dir config/ --config-name config\n```\n\nContent of `config.yaml`:\n```bash\nusername: <WANDB_USERANEM>\nexperiment: <WANDB_EXPERIMENT>\nrun_id: <WANDB_RUN_ID>\nclassifier: # model class to explain\n  _target_: example.streamlit_app.mnist_model.LitMNIST\n  batch_size: 1\n  data_dir: "."\nexplainers: # list of explainers to use\n - explainer_with_params:\n    explainer_name: CV_GRADIENT_SHAP_EXPLAINER\n    kwargs:\n      n_steps: 1000\n```\n\n# Development\n\n## Requirements\n\nThe project was tested using Python version `3.8`.\n\n## CUDA\n\nThe recommended version of CUDA is `10.2` as it is supported since version\n`1.5.0` of `torch`. You can check the compatibility of your CUDA version\nwith the current version of `torch`:\nhttps://pytorch.org/get-started/previous-versions/.\n\nAs our starting Docker image we were using the one provided by Nvidia: ``nvidia/cuda:10.2-devel-ubuntu18.04``.\n\nIf you wish an easy to use docker image we advise to use our ``Dockerfile``.\n\n## pyenv\nOptional step, but probably one of the easiest way to actually get Python version with all the needed aditional tools (e.g. pip).\n\n`pyenv` is a tool used to manage multiple versions of Python. To install\nthis package follow the instructions on the project repository page:\nhttps://github.com/pyenv/pyenv#installation. After installation You can\ninstall desired Python version, e.g. `3.8.16`:\n```bash\npyenv install 3.8.16\n```\n\nThe next step is required to be able to use a desired version of Python with\n`poetry`. To activate a specific version of Python interpreter execute the command:\n```bash\npyenv local 3.8.16 # or `pyenv global 3.8.16`\n```\n\nInside the repository with `poetry` You can select a specific version of Python\ninterpreter with the command:\n```bash\npoetry env use 3.8.16\n```\n\nAfter changing the interpreter version You have to once again install all\ndependencies:\n```bash\npoetry install\n```\n\n## Poetry\n\nTo separate runtime environments for different services and repositories, it is\nrecommended to use a virtual Python environment. You can configure `Poetry` to\ncreate a new virtual environment in the project directory of every repository. To\ninstall `Poetry` follow the instruction at https://python-poetry.org/docs/#installing-with-the-official-installer. We are using `Poetry` in version\n`1.2.1`. To install a specific version You have to provide desired package\nversion:\n```bash\ncurl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.1 python3 -\n```\nAdd poetry to PATH:\n```bash\nexport PATH="/home/ubuntu/.local/bin:$PATH"\necho \'export PATH="/home/ubuntu/.local/bin:$PATH"\' >> ~/.bashrc\n```\n\nAfter installation, configure the creation of virtual environments in the directory of the project.\n```bash\npoetry config virtualenvs.create true\npoetry config virtualenvs.in-project true\n```\n\nThe final step is to install all the dependencies defined in the\n`pyproject.toml` file.\n\n```bash\npoetry install\n```\n\nOnce all the steps have been completed, the environment is ready to go.\nA virtual environment by default will be created with the name `.venv` inside\nthe project directory.\n\n## Pre-commit hooks setup\n\nTo improve the development experience, please make sure to install\nour [pre-commit](https://pre-commit.com/) hooks as the very first step after\ncloning the repository:\n\n```bash\npoetry run pre-commit install\n```\n\n## Note\n---\nAt the moment only explainable algorithms for image classification are\nimplemented. In the future more algorithms and more computer vision tasks will\nbe introduced. In the end, the module should work with all types of tasks (NLP, etc.).\n\n### Examples\n\nIn `example/notebooks/` directory You can find notebooks with example usage of this\nframework. Scripts in `example/` directory contain samples of training models using\ndifferent callbacks.\n',
    'author': 'ReasonField Lab Team',
    'author_email': 'None',
    'maintainer': 'Adam Jan Kaczmarek',
    'maintainer_email': 'adam.kaczmarek@reasonfieldlab.com',
    'url': 'https://github.com/softwaremill/FoXAI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
