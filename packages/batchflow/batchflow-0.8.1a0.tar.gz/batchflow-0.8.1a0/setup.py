# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['batchflow',
 'batchflow.models',
 'batchflow.models.metrics',
 'batchflow.models.torch',
 'batchflow.models.torch.blocks',
 'batchflow.models.torch.callbacks',
 'batchflow.models.torch.layers',
 'batchflow.models.torch.losses',
 'batchflow.models.torch.modules',
 'batchflow.models.torch.optimizers',
 'batchflow.opensets',
 'batchflow.plotter',
 'batchflow.research',
 'batchflow.tests']

package_data = \
{'': ['*'], 'batchflow.tests': ['notebooks/*', 'plot_notebooks/*']}

install_requires = \
['dill>=0.3,<0.4',
 'llvmlite',
 'numba>=0.56,<0.57',
 'numpy>=1.18,<2.0',
 'scipy>=1.9,<2.0',
 'tqdm>=4.19,<5.0']

extras_require = \
{'datasets': ['requests'],
 'dev': ['pandas>=0.24,<0.25', 'pytest>=7.0,<8.0', 'pylint>=2.16,<3.0'],
 'image': ['pillow>=9.4,<10.0', 'matplotlib>=3.0,<4.0'],
 'jupyter': ['matplotlib>=3.0,<4.0',
             'nbformat',
             'nbconvert',
             'ipykernel',
             'ipython',
             'notebook',
             'jupyter_client',
             'jupyter_server',
             'requests'],
 'nn': ['psutil',
        'nvidia_smi',
        'torch>=1.13,<2.0',
        'torchvision>=0.14,<0.15',
        'einops>=0.3,<0.4',
        'ptflops>=0.6,<0.7'],
 'profile': ['matplotlib>=3.0,<4.0',
             'psutil',
             'nvidia_smi',
             'pandas>=0.24,<0.25'],
 'research': ['matplotlib>=3.0,<4.0',
              'multiprocess>=0.70,<0.71',
              'psutil',
              'pandas>=0.24,<0.25'],
 'telegram': ['urllib3>=1.25,<2.0']}

setup_kwargs = {
    'name': 'batchflow',
    'version': '0.8.1a0',
    'description': 'ML pipelines, model configuration and batch management',
    'long_description': "[![License](https://img.shields.io/github/license/analysiscenter/batchflow.svg)](https://www.apache.org/licenses/LICENSE-2.0)\n[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://python.org)\n[![PyTorch](https://img.shields.io/badge/PyTorch-1.7-orange.svg)](https://pytorch.org)\n[![codecov](https://codecov.io/gh/analysiscenter/batchflow/branch/master/graph/badge.svg)](https://codecov.io/gh/analysiscenter/batchflow)\n[![PyPI](https://badge.fury.io/py/batchflow.svg)](https://badge.fury.io/py/batchflow)\n[![Status](https://github.com/analysiscenter/batchflow/workflows/status/badge.svg)](https://github.com/analysiscenter/batchflow/actions?query=workflow%3Astatus)\n\n\n# BatchFlow\n\n`BatchFlow` helps you conveniently work with random or sequential batches of your data\nand define data processing and machine learning workflows even for datasets that do not fit into memory.\n\nFor more details see [the documentation and tutorials](https://analysiscenter.github.io/batchflow/).\n\nMain features:\n- flexible batch generaton\n- deterministic and stochastic pipelines\n- datasets and pipelines joins and merges\n- data processing actions\n- flexible model configuration\n- within batch parallelism\n- batch prefetching\n- ready to use ML models and proven NN architectures\n- convenient layers and helper functions to build custom models\n- a powerful research engine with parallel model training and extended experiment logging.\n\n## Basic usage\n\n```python\nmy_workflow = my_dataset.pipeline()\n              .load('/some/path')\n              .do_something()\n              .do_something_else()\n              .some_additional_action()\n              .save('/to/other/path')\n```\nThe trick here is that all the processing actions are lazy. They are not executed until their results are needed, e.g. when you request a preprocessed batch:\n```python\nmy_workflow.run(BATCH_SIZE, shuffle=True, n_epochs=5)\n```\nor\n```python\nfor batch in my_workflow.gen_batch(BATCH_SIZE, shuffle=True, n_epochs=5):\n    # only now the actions are fired and data is being changed with the workflow defined earlier\n    # actions are executed one by one and here you get a fully processed batch\n```\nor\n```python\nNUM_ITERS = 1000\nfor i in range(NUM_ITERS):\n    processed_batch = my_workflow.next_batch(BATCH_SIZE, shuffle=True, n_epochs=None)\n    # only now the actions are fired and data is changed with the workflow defined earlier\n    # actions are executed one by one and here you get a fully processed batch\n```\n\n\n## Train a neural network\n`BatchFlow` includes ready-to-use proven architectures like VGG, Inception, ResNet and many others.\nTo apply them to your data just choose a model, specify the inputs (like the number of classes or images shape)\nand call `train_model`. Of course, you can also choose a loss function, an optimizer and many other parameters, if you want.\n```python\nfrom batchflow.models.torch import ResNet34\n\nmy_workflow = my_dataset.pipeline()\n              .init_model('model', ResNet34, config={'loss': 'ce', 'classes': 10})\n              .load('/some/path')\n              .some_transform()\n              .another_transform()\n              .train_model('ResNet34', inputs=B.images, targets=B.labels)\n              .run(BATCH_SIZE, shuffle=True)\n```\n\nFor more advanced cases and detailed API see [the documentation](https://analysiscenter.github.io/batchflow/).\n\n\n## Installation\n\n> `BatchFlow` module is in the beta stage. Your suggestions and improvements are very welcome.\n\n> `BatchFlow` supports python 3.6 or higher.\n\n### Stable python package\n\nWith [poetry](https://python-poetry.org/)\n```\npoetry add batchflow\n```\n\nWith old-fashioned [pip](https://pip.pypa.io/en/stable/)\n```\npip3 install batchflow\n```\n\n### Development version\n\nWith [poetry](https://python-poetry.org/)\n```\npoetry add --editable git+https://github.com/analysiscenter/batchflow\n```\n\nWith old-fashioned [pip](https://pip.pypa.io/en/stable/)\n```\npip install --editable git+https://github.com/analysiscenter/batchflow\n```\n\n### Extras\nSome `batchflow` functions and classed require additional dependencies.\nIn order to use that functionality you might need to install `batchflow` with extras (e.g. `batchflow[nn]`):\n\n- image - working with image datasets and plotting\n- nn - for neural networks (includes torch, torchvision, ...)\n- datasets - loading standard datasets (MNIST, CIFAR, ...)\n- profile - performance profiling\n- jupyter - utility functions for notebooks\n- research - multiprocess research\n- telegram - for monitoring pipelines via a telegram bot\n- dev - batchflow development (pylint, pytest, ...)\n\nYou can install several extras at once, like `batchflow[image,nn,research]`.\n\n\n## Projects based on BatchFlow\n- [SeismiQB](https://github.com/gazprom-neft/seismiqb) - ML for seismic interpretation\n- [SeismicPro](https://github.com/gazprom-neft/SeismicPro) - ML for seismic processing\n- [PetroFlow](https://github.com/gazprom-neft/petroflow) - ML for well interpretation\n- [PyDEns](https://github.com/analysiscenter/pydens) - DL Solver for ODE and PDE\n- [RadIO](https://github.com/analysiscenter/radio) - ML for CT imaging\n- [CardIO](https://github.com/analysiscenter/cardio) - ML for heart signals\n\n\n## Citing BatchFlow\nPlease cite BatchFlow in your publications if it helps your research.\n\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1041203.svg)](https://doi.org/10.5281/zenodo.1041203)\n\n```\nRoman Khudorozhkov et al. BatchFlow library for fast ML workflows. 2017. doi:10.5281/zenodo.1041203\n```\n\n```\n@misc{roman_kh_2017_1041203,\n  author       = {Khudorozhkov, Roman and others},\n  title        = {BatchFlow library for fast ML workflows},\n  year         = 2017,\n  doi          = {10.5281/zenodo.1041203},\n  url          = {https://doi.org/10.5281/zenodo.1041203}\n}\n```\n",
    'author': 'Roman Kh',
    'author_email': 'rhudor@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
