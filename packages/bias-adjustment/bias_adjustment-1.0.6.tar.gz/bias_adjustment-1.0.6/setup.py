# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bias_adjustment',
 'bias_adjustment.distributions',
 'bias_adjustment.quantile_mapping']

package_data = \
{'': ['*']}

install_requires = \
['conda-lock>=1.4.0,<2.0.0', 'numpy>=1.24.3,<2.0.0', 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'bias-adjustment',
    'version': '1.0.6',
    'description': 'Bias Adjusment by Quantile Mapping',
    'long_description': '# Bias Adjusment by Quantile Mapping\n\nBias adjustment techniques:\n- Quantile Mapping\n- Detrended Quantile Mapping\n- Quantile Delta Mapping ([Cannon et al., 2015](https://doi.org/10.1175/JCLI-D-14-00754.1))\n\n\n## Usage\n```python\nfrom bias_adjustment import BiasAdjustment\n```\n',
    'author': 'Emilio Gozo',
    'author_email': 'emiliogozo@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/emiliogozo/bias_adjustment',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.9',
}


setup(**setup_kwargs)
