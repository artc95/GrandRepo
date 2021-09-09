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
    - Set Google Application Credentials e.g. run "set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\artc\Desktop\xxx.json" (instructions on creating Service Account, getting account key as .json file and setting Credentials as .json file https://cloud.google.com/docs/authentication/getting-started)
- Link VSCode to **Github Repo** (used in https://github.com/artc95/SpotifyETL_WannaDE_)
  - Create repository in Github
  - Clone Github repository in VSCode using Github respository URL
  - After making changes in VSCode, Stage Changes, Commit (with message), then Push



