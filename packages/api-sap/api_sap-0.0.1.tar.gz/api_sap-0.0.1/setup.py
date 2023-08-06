from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(
    name='api_sap',
    version='0.0.1',
    license='MIT License',
    author='Wilton Melo',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='pmelo.wilton@gmail.com',
    keywords='api sap',
    description='Teste de geração de biblioteca',
    packages=['py_sap'],
    install_requires=['pywin32', 'psutil', 'PySimpleGUI']
)
