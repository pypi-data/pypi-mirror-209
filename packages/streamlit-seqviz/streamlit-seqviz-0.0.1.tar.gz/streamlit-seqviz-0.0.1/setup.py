import setuptools

import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pypi_readme.rst'), 'r') as f:
  long_des = f.read()

setuptools.setup(
    name="streamlit-seqviz",
    version="0.0.1",
    author="Nicola Landro",
    author_email="nicolaxx94@live.it",
    description="This library is a streamlit app for chemical or medical use that show DNA sequences effectively",
    long_description=long_des,
    long_description_content_type="text/plain",
    url="https://gitlab.com/nicolalandro/streamlit-seqviz",
    keywords = ['dna', 'streamlit', 'chemistry'],
    project_urls={
        'Source': 'https://gitlab.com/nicolalandro/streamlit-seqviz',  
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
