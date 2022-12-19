# UI for ML models


# Goal : reproduce a cemantix

to reproduce : https://cemantix.certitudes.org/


# Installation

1. Install a venv : see creation of venv

```bash
pip install virtualenv
virtualenv venv
```

2. Activate the environment

On Windows : `.\venv\Scripts\activate`  
Note : on linux path can change


3. Install requirements in the venv (1 by 1 or using requirements file)

Libraries : 
- streamlit : `pip install streamlit`
- plotly: `pip install plotly`
- pandas: `pip install pandas`
- scikit-learn: `pip install scikit-learn`
- python-dotenv: `pip install python-dotenv`
- pytest: `pip install pytest`
- opencv : `pip install opencv-python`


or

>pip install -r resources/install/requirements.txt


Note : 
- streamlit install doc : https://docs.streamlit.io/library/get-started/installation


4. Download the word2vec model :
>https://drive.google.com/file/d/1cUoBrCodYuF401eDJcAKRC9DjlJVMZWd/view?usp=sharing


# Launch on windows

>streamlit run .\app.py 

Normally a browser will open (or the adress will be displayed)

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

# Some gits command

Most used commands :
- clone repo : `git clone`
- add remote `git remote add origin <PATH of .git>`
- create branch `git checkout -b newbranch`
- change branch `git checkout master`
- add all files : `git add .`
- create commit + commentary : `git commit -m "some commit"`
- push to remote : `git push origin some_remote_branch`
- get modifications and try to merge : `git pull`

Other commands : 
- get modif without merging : `git fetch`
- show changes : `git diff`
- merge branch featureA into current : `git merge featureA`
- commit when forgot smthg :   `git commit --amend --no-edit`


# Notes on widgets
doc : https://docs.streamlit.io/library/api-reference/session-state

- var = st.checkbox() if we want to store result of checkbox in python variable
- st.checkbox(on_change=somefunc) if we want to trigger a callback
- st.checkbox(key=somename) if we want to reference it later using st.session_state.somename
- python UI page is run once each time a widget changes
- if there is a while true loop in the page, than widget will update but not variables in python because script will not finish