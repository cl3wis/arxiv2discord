from setuptools import setup


setup(
    name='arxiv2discord',
    version='0.0.1',
    author_email='devcl3wis@gmail.com',
    py_modules=['arxiv2discord'],
    entry_points={
        'console_scripts': [
            'arxiv2discord = arxiv2discord:main',
        ],
    },
    install_requires=[
		'discord.py==0.16.8',
		'feedparser==5.2.1',
		'sympy==1.01',
    ],
    classifiers=[
      'Environment :: Console'
    ],
)