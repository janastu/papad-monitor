# Papad Monitor
Scripts to manage export import from papad database to handover to syncthing folders.

* `main.py` is the watcher for changes in the configured (syncthing folders) and if any changes will `import_json()` content into db
* `dump.py` exports the contents of db and saves into json file in the configured path (syncthing folders), this should be run in a crontab to run in intervals
* The dumped JSON file naming convention is macid.json

## Install
1. Clone this repository `git clone https://github.com/janastu/papad-monitor.git`
2. Setup python virtual environment and activate (for more on how to setup virtual env https://docs.python.org/3.6/tutorial/venv.html)
3. Install all dependencies, run this command `pip install -r requirements.txt`
4. Run this command `python main.py path/to/sync/folder` to start the watcher
5. In another terminal, activate virtual env in the root of the project
6. set environment variable `export SYNCTHING_FOLDER=path/to/sunc/folder`
7. run this command `python dump.py` (although this should be run in crontab for automatically exporting in fixed intervals)

## Use Cases
* Device A and Device B are running papad web application (api server and frontend client)
* User X and Y access papad through Device A via the url https://deviceA.local
* User Z access papad through Device B via the url https://deviceB.local
* User X adds a tag "gulab jamoon recipe" to `jamoon.mp3` at https://deviceA.local
* User Y adds a image of gulab jamoon to `jamoon.mp3` at https://deviceA.local
* User Z should be able to see `jamoon.mp3` with the tags and images  User X and Y at https://deviceB.local

## Passed Test cases
TBA

## References
The dry run user stories, and other test cases are documented in the below document with diagrams. 
https://hackmd.io/@sagesalus/ByUUI1BT8
