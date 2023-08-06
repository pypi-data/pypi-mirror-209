# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jira2branch', 'jira2branch.tests']

package_data = \
{'': ['*'], 'jira2branch': ['build_logs/*', 'job_json/*']}

install_requires = \
['GitPython==3.1.31',
 'Unidecode==1.3.6',
 'click==8.1.3',
 'halo==0.0.31',
 'jira==3.5.0',
 'python-gitlab==3.14.0']

setup_kwargs = {
    'name': 'jira2branch',
    'version': '0.1.17',
    'description': 'Takes a JIRA issue and creates a git branch',
    'long_description': '# JIRA 2 Branch\n\nTakes a JIRA issue and creates a git branch\n\n```\nUsage: jira2branch [OPTIONS] ISSUE_ID_OR_URL SOURCE_BRANCH\n\n  Simple program that takes a JIRA issue ID and creates a new local and\n  tracking remote branch\n\nOptions:\n  -n, --name-only      Generates the branch name and prints it, no actual\n                       branch will be created (default is False)\n  -p, --push           Push newly created branch to remote (default is False)\n  -t, --target PATH    Target repository (default is current directory)\n  -r, --merge-request  Create merge request. Requires --push. (default is\n                       False)\n  --help               Show this message and exit.\n```\n\n- Branch naming format is as follows:\n  - {CONVENTIONAL_COMMIT_PREFIX}/{ISSUE_ID}_{ISSUE_TITLE}\n\n## Requirements\n\nRequires Python 3.8\n\n### Dev env\n\n```\npip install pipenv\npipenv install\nvirtualenv venv\n. venv/bin/activate\npip install --editable .\n```\n\nAfterwards, your command should be available:\n\n```\n$ jira2branch WT3-227 develop\nfix/WT3-227_some-jira-issue\n```\n\n### Credentials\n\nJIRA credentials will be fetched from `[USER HOME]/.j2b/secrets.ini` with the following format:\n\n```ini\n[JIRA CREDENTIALS]\n\n# url = \n# email = \n# username = \n# password = \n# token = \n```\n\nWIP: GitLab credentials will also be required for automatic MR creation\n\n#### Required fields\n\n`url` and `email` are required.\n\nUse either `username` + `password` or `token` depending on how access is configured\n\n## Usage\n\n`python main.py [JIRA_ISSUE_ID|JIRA_ISSUE_URL]`\n\n### Examples\n\n`python main.py WT3-227`\n\n`python main.py https://company.atlassian.net/browse/WT3-227`\n',
    'author': 'Tiago Pereira',
    'author_email': 'tiago.pereira@infraspeak.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
