{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "setup.py",
      "authorship_tag": "ABX9TyMnfPQBtmT9BPXY1a3Gusz6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Psubrat98/ML-Projects-With-Python/blob/main/ML%20Project/Projects/Student%20Marks/setup.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from setuptools import find_packages, setup"
      ],
      "metadata": {
        "id": "Q3_e5VxBNIPw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "setup(\n",
        "    name='mlproject',\n",
        "    version='0.0.1',\n",
        "    author='Subrat',\n",
        "    author_email='psub44@gmail.com',\n",
        "    packages=find_packages(),\n",
        "    install_requires=[],\n",
        ")"
      ],
      "metadata": {
        "id": "w6ARWJ3yOVng"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}