# UI for ML models


# Goal : reproduce a cemantix

to reproduce : https://cemantix.certitudes.org/


# Installation

1. Install a venv : see creation of venv

2. Activate the environment

3. Install requirements in the venv (1 by 1 or using requirements file)
Documentation: https://docs.streamlit.io/library/get-started/installation

>pip install -r install_scripts/requirements.txt

4. Download the word2vec model :
>https://drive.google.com/file/d/1cUoBrCodYuF401eDJcAKRC9DjlJVMZWd/view?usp=sharing


# Launch on windows

>streamlit run .\app.py 

# Work to do

Features :
- create the main UI having two tabs
- create the UI tab to find the word
- create the UI tab to discover the wikipedia page
- collaborate using git

# inspiration : 

Streamlit resources : 
- https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4
- https://github.com/alanjones2/Alan-Jones-article-code
- https://github.com/adenhaus/f1-data-viz

Word2vec resources : 
- https://github.com/eyaler/word2vec-slim
- https://radimrehurek.com/gensim/models/word2vec.html
