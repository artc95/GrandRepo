# GrandRepo
Directory of projects and their documentation.

_General_
- Uninstall all local Python packages (https://www.codegrepper.com/code-examples/shell/delete+all+python+packages , by Nervous Nightingale)

_Sentimental_
- Linux "nohup" command (i.e. "no hang up" executes command that does not stop when user exits)
  - **nohup python3 path/to/file.py &** = Run a python file which does not stop even when user logs out (https://stackoverflow.com/questions/47455680/running-a-python-script-on-google-cloud-compute-engine)
  - **cat nohup.out** = See output of nohup process (https://stackoverflow.com/questions/47455680/running-a-python-script-on-google-cloud-compute-engine)
  - **ps -ef|grep python3** = Get Process ID(s) of python3 processes (https://stackoverflow.com/questions/17385794/how-to-get-the-process-id-to-kill-a-nohup-process)
  - **kill 1234** = Replace 1234 with Process ID to kill process, or **kill -9 1234** to force kill process (https://stackoverflow.com/questions/17385794/how-to-get-the-process-id-to-kill-a-nohup-process)
- **.gitignore** to ignore changes (https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/)
- GCP
  - Apache Beam for **Dataflow** (https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#cloud-console)
    - In Python virtual environment, run "pip install wheel" then "pip install apache-beam[gcp]" which takes awhile
  - **Pub/Sub**
    - Sample publish (pub.py) and subscribe (sub.py) code at https://github.com/googleapis/python-pubsub/tree/master/samples/snippets/quickstart
    - Publish using Cloud Functions (https://cloud.google.com/functions/docs/calling/pubsub)
  - **Functions**
    - To test Functions - open Cloud Shell, run "gcloud functions call <function>" e.g. (gcloud functions call stream_prices)  
- **Twitter + GCP + Telegram** (for tweets with keyword+sentiment analysis+send updates) (https://github.com/artc95/Sentimental/blob/master/Twitter_GCP_Telegram.py)
- **BeautifulSoup** to parse webscraped HTML (https://realpython.com/beautiful-soup-web-scraper-python/)

_Pyglot https://github.com/artc95/Pyglot_
- Setup **Python Virtual Environment** in VSCode (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
  - (In CLI or code editor e.g. Visual Studio Code), go to (i.e. cd for Windows) project directory, run "py -m venv env"
  - In project directory, run ".\env\Scripts\activate"
  - Install modules using pip/pip3
  - Run "deactivate" to leave virtual environment
- Use **GCP in Python Virtual Environment**
  - Ensure virtual environment is activated with (env) at the start of command line
  - Install necessary GCP modules (e.g. run "pip install --upgrade google-cloud-language")
  - Before running .py scripts:
    - Use virtual environment's interpreter (in Visual Studio Code, interpreter option is at the bottom OR enter path to virtual env's python.exe)
    - Set Google Application Credentials e.g. run "set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\artc\Desktop\xxx.json" (instructions on creating Service Account, getting account key as .json file and setting Credentials as .json file https://cloud.google.com/docs/authentication/getting-started)
- PyWebIO with Flask webapp
- Docker Containerization with GCP (Container Registry, Cloud Run)

_Bullsheet https://github.com/artc95/Bullsheet_
- Python, SQL on Google Cloud Platform (Compute Engine, Cloud Storage, Cloud Functions, BigQuery) and Google Data Studio
- (Legacy) Dash webapp hosted on Heroku

_SpotifyETL_WannaDE https://github.com/artc95/SpotifyETL_WannaDE_
- Link VSCode to Github Repo
  - Create repository in Github
  - Clone Github repository in VSCode using Github respository URL
  - After making changes in VSCode, Stage Changes, Commit (with message), then Push  


