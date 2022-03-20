# GrandRepo
Documentation for reference.

_General / Python_
- **Visualizations**:
  - Matplotlib 
      - Line graph with axis labels, title (add # %% to indicate Jupyter notebook cell for interactive plt.show()):
```python
# %%
x = range(1,50)
y = [value*3 for value in x]

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line.")
plt.show()
```
  - Seaborn
    - Introduction https://seaborn.pydata.org/introduction.html
- **Twitter + GCP + Telegram** (for tweets with keyword+sentiment analysis+send updates) (https://github.com/artc95/Sentimental/blob/master/Twitter_GCP_Telegram.py)
- **BeautifulSoup** to parse webscraped HTML (https://realpython.com/beautiful-soup-web-scraper-python/)
- **JSON in Python** (https://www.programiz.com/python-programming/json)
  - **json.loads()** converts JSON string to Python dict, or json.load() to read JSON file into Python dict ; **json.dumps()** converts Python dict to JSON object, or json.dump() to write to file 
- **PyWebIO** with **Flask** webapp (used in https://github.com/artc95/Pyglot)
- Uninstall all local Python packages (https://www.codegrepper.com/code-examples/shell/delete+all+python+packages , by Nervous Nightingale)

_Google Cloud Platform_
- Apache Beam for **Dataflow** (https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#cloud-console)
  - In Python virtual environment, run "pip install wheel" then "pip install apache-beam[gcp]" which takes awhile
- **Pub/Sub** (used in https://github.com/artc95/Sentimental)
  - Sample publish (pub.py) and subscribe (sub.py) code at https://github.com/googleapis/python-pubsub/tree/master/samples/snippets/quickstart
  - Publish using Cloud Functions (https://cloud.google.com/functions/docs/calling/pubsub), working code:
```python
"""
in requirements.txt:
requests>=2.26.0
google-cloud-pubsub>=2.7.0
"""
import requests
from google.cloud import pubsub_v1
import base64
import json

def stream_prices_to_pubsub(request):
  publisher = pubsub_v1.PublisherClient()
  
  project_id = "sentimental-319904"
  topic_id = "prices_stream"
  topic_path = publisher.topic_path(project_id,topic_id)
      
  message_json = json.dumps({
    "data": {"message": "prices!"},
  })
  message_bytes = message_json.encode('utf-8')
      
  try:
    publish_future = publisher.publish(topic_path, data=message_bytes)
    publish_future.result()  # Verify the publish succeeded
    return 'Message published.'
   except Exception as e:
     print(e)
     return (e, 500)
 ``` 
- **Functions** (used in https://github.com/artc95/Sentimental)
  - To test Functions - open Cloud Shell, run "gcloud functions call (FUNCTION)" e.g. (gcloud functions call stream_prices)
  - Only can write files in "/tmp/" directory (https://towardsdatascience.com/how-to-schedule-a-serverless-google-cloud-function-to-run-periodically-249acf3a652e)
- **Scheduler**
  - To trigger Cloud Function, choose "Target type" as "HTTP", "URL" as Cloud Function's HTTP Trigger URL (e.g. https://us-central1-sentimental-319904.cloudfunctions.net/test_scheduler), "HTTP Method" as "POST", "Auth Header" as "Add OIDC token", "Service account" use service account with Owner or invoke Cloud Function permissions (e.g. senti-482@sentimental-319904.iam.gserviceaccount.com) (https://cloud.google.com/community/tutorials/using-scheduler-invoke-private-functions-oidc)
- Python, SQL on Google Cloud Platform (Compute Engine, Cloud Storage, Cloud Functions, BigQuery) and Google Data Studio (used in https://github.com/artc95/Bullsheet)

_SQL (Structured Query Language)
- Basics:
```SQL
SELECT [column names] 
FROM [table name] JOIN [table name] ON [matching keys]
WHERE [column name] [logical operator] [reference] 
GROUP BY [column names]
```
```SQL
e.g. wildcards *, %
SELECT matchid, player FROM goal
WHERE player LIKE 'Mario%'

e.g. SELECT DISTINCT, multiple conditions
SELECT DISTINCT player
  FROM game JOIN goal ON matchid = id 
    WHERE (team1='GER' OR team2='GER') AND (goal.teamid != 'GER')

e.g. COUNT(), GROUP BY() https://sqlzoo.net/wiki/The_JOIN_operation 11.
SELECT matchid, mdate, COUNT(goal.matchid) AS goals_scored
  FROM game JOIN goal ON id = matchid 
 WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY game.id, game.mdate, goal.matchid

e.g. SUM(), CASE WHEN https://sqlzoo.net/wiki/The_JOIN_operation 13.
SELECT mdate,team1,
  SUM(CASE 
    WHEN teamid=team1 THEN 1 
    ELSE 0 END) AS score1,
    team2,
  SUM(CASE 
    WHEN teamid=team2 THEN 1 
    ELSE 0 END) AS score2
  FROM game JOIN goal ON matchid = id
GROUP BY mdate, team1, team2
ORDER BY mdate
```
- Practice with feedback https://sqlzoo.net/wiki/SQL_Tutorial ; Professional book https://goalkicker.com/SQLBook/
- Categories of Commands i.e. Data _ Language - Definition (DDL), Query (DQL), Manipulation (DML), Control (DCL) https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/

_Linux_
- Linux "nohup" command (i.e. "no hang up" executes command that does not stop when user exits)
  - **nohup python3 path/to/file.py &** = Run a python file which does not stop even when user logs out (https://stackoverflow.com/questions/47455680/running-a-python-script-on-google-cloud-compute-engine)
  - **cat nohup.out** = See output of nohup process (https://stackoverflow.com/questions/47455680/running-a-python-script-on-google-cloud-compute-engine)
  - **ps -ef|grep python3** = Get Process ID(s) of python3 processes (https://stackoverflow.com/questions/17385794/how-to-get-the-process-id-to-kill-a-nohup-process)
  - **kill 1234** = Replace 1234 with Process ID to kill process, or **kill -9 1234** to force kill process (https://stackoverflow.com/questions/17385794/how-to-get-the-process-id-to-kill-a-nohup-process)

_Docker_
- Docker Containerization with GCP (Container Registry, Cloud Run) (used in https://github.com/artc95/Pyglot)

_Heroku_
- Host Dash webapp (used in https://github.com/artc95/Bullsheet)

_VSCode_
- **.gitignore** to ignore changes (https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/)
- Setup **Python Virtual Environment** (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (used in https://github.com/artc95/Pyglot)
  - (In CLI or code editor e.g. Visual Studio Code), go to (i.e. cd for Windows) project directory, run "py -m venv env"
  - In project directory, run ".\env\Scripts\activate"
  - Install modules using pip/pip3
  - Run "deactivate" to leave virtual environment
- **GCP in Python Virtual Environment** (used in https://github.com/artc95/Pyglot)
  - Ensure virtual environment is activated with (env) at the start of command line
  - Install necessary GCP modules (e.g. run "pip install --upgrade google-cloud-language")
  - Before running .py scripts:
    - Use virtual environment's interpreter (in Visual Studio Code, interpreter option is at the bottom OR enter path to virtual env's python.exe)
    - Set Google Application Credentials (instructions on creating Service Account, getting account key as .json file and setting Credentials as .json file https://cloud.google.com/docs/authentication/getting-started)
      - Powershell, run '$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\artc\Desktop\...\xxx.json"'
      - Command Prompt, run 'set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\artc\Desktop\...\xxx.json' 
- Link VSCode to **Github Repo** (used in https://github.com/artc95/SpotifyETL_WannaDE_)
  - Create repository in Github
  - Clone Github repository in VSCode using Github respository URL
  - After making changes in VSCode, Stage Changes, Commit (with message), then Push

_Github Actions_
- **Basic Workflow** (used in https://github.com/artc95/Sentimental)
  - Ensure Personal Access Token has "workflow" scope to allow update of workflow code (Settings > Developer Settings > Personal access tokens > Select the token, then check "workflow" scope)
  - In project directory, create a directory ".github/workflows" to store .yml files
  - Basic workflow skeleton (in a .yml file):
```yml
name: Test Github Actions
on:
  push: 
    branches: 
      - master

jobs:
  test_action:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository # must checkout!
        uses: actions/checkout@v2
      - name: Check Github Action works
        run: echo You pushed!
```
  - Deploy and Run GCP Cloud Function (deploy-cloud-functions https://github.com/google-github-actions/deploy-cloud-functions and specifying source_dir https://github.com/google-github-actions/deploy-cloud-functions/issues/37 ; setup-gcloud and use GCP CLI https://github.com/google-github-actions/setup-gcloud#example-workflows) :
```yml
name: Test Cloud Functions
on:
  push: 
    branches: 
      - master

jobs:
  Cloud_Functions:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository # must checkout!
        uses: actions/checkout@v2

      - name: Setup GCP SDK
        uses: google-github-actions/setup-gcloud@master
        with:
          project_id: "sentimental-323305"
          service_account_key: ${{ secrets.SENTIMENTAL323305JSON }}
          export_default_credentials: true

      - name: Deploy Cloud Function
        uses: google-github-actions/deploy-cloud-functions@main
        with:
          name: candle_stream_minutely
          runtime: python39
          entry_point: main
          # credentials: ${{ secrets.SENTIMENTAL323305JSON }} - set in "Setup GCP SDK"
          source_dir: CloudFunctions/candle_stream_minutely
          # project_id: "sentimental-323305" - set in "Setup GCP SDK"

      - name: Run Cloud Function
        run: gcloud functions call candle_stream_minutely
```
  - Documentation and other sample .ymls: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions ; github.com/datarootsio/rootsacademy-pyspark-101-ci/blob/arthur
  - Billing https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions

_Git_
- **Deconflict changes in master and another branch**
  - Checkout master branch, pull it for latest changes
  - Go back to own branch, then select master branch and select "Merge selected into current", then "Choose yours" when merging to only keep your own changes, then Push from own branch

_Github_
- **Clone repositories**
  - On the repo's github page, in the "Code" dropdown, copy and paste the Github CLI command, e.g. "gh repo clone datarootsio/ai-song-contest"
  - Run this gh command in the directory you want to clone in, e.g. in Windows Powershell C:\Users\Arthur\Desktop, run "gh repo clone datarootsio/ai-song-contest"

_Jupyter Notebook_
- **Using Virtual Environment as Kernel**
  - i.e. isolated environment with specific packages/dependecies for a notebook
  - install, use, uninstall tutorial https://www.geeksforgeeks.org/using-jupyter-notebook-in-virtual-environment/

_Magenta (in Ubuntu)_
- **Install conda env: magenta** (https://github.com/magenta/magenta > under Automated Install (w/ Anaconda)
  - (may need to install conda or miniconda first)
  - curl https://raw.githubusercontent.com/tensorflow/magenta/main/magenta/tools/magenta-install.sh > /tmp/magenta-install.sh
  - bash /tmp/magenta-install.sh

- **Install nb_conda_kernels to show other environment kernels in Jupyter notebook** (https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874)
  - (in base environment) conda install nb_conda_kernels
  - (to enter magenta environment) conda activate magenta
  - (in magenta environment) conda install ipykernel
  - (still in magenta environment) pip install magenta
  - (still in magenta environment) pip install pyfluidsynth pretty_midi (basically follow dependency installation in Hello Magenta.ipynb https://colab.research.google.com/notebooks/magenta/hello_magenta/hello_magenta.ipynb)
(then run "conda deactivate" to return to base environment, launch "jupyter notebook" and use conda env: magenta)

- **sudo install fluidsynth** to play magenta note_sequences in Jupyter notebook
  - (as root user) sudo apt-get install fluidsynth (https://github.com/FluidSynth/fluidsynth/wiki/Download)
