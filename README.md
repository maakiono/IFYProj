# IFY Project
  Intermediate Final Year Project

## Social Alert
  A Project that aims to leverage social media to improve disaster awareness and faciltate quicker access to aid and support required
  Social Alert scans social media (respecting its privacy policy) flagging potential posts that might require attention and tags them on a range of categories, posts are cached geo-tagged if possible for visualization on dashboard 

## Running The Project
  You will strictly need Python 3.10, project may be adapted to run on other versions and other non unix platforms but 3.10 is the sweet spot to ensure all dependencies are resolved.

  Ensure all keys and required paths are filled in `settings.json` an example file has been provided in the repo
  
  This project utilizes poetry the following commands should be enough to setup backend api:
```bash
poetry install
poetry run viz.py
```

  The front end hosts a web server of the dashboard containing all the scanned data and can be hosted using:
```bash
poetry install
poetry run dboard.py
```

  Secondarily, `init.sh` runs the dashboard and backend automagically assuming the above work fine with no issues
