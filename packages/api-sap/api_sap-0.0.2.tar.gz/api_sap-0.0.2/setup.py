"""Código para criar o setup para upload no PYPI."""
from setuptools import setup


def readme() -> str:
    """Função para abrir o arquivo leia-me.

    Returns:
        str: Retorna o arquivo leia-me.
    """
    with open('README.md', 'r', encoding="utf-8") as arq:
        return arq.read()


setup(
    name='api_sap',
    version='0.0.2',
    license='MIT License',
    author='Wilton Melo',
    long_description=readme(),
    requires_python='>=3.9.13',
    long_description_content_type='text/markdown',
    author_email='pmelo.wilton@gmail.com',
    keywords=['api sap', 'SAP', 'conectar ao SAP'],
    description='API de acesso ao SAP.',
    packages=['py_sap'],
    install_requires=['pywin32==306', 'psutil==5.9.5', 'PySimpleGUI==4.60.4']
)
