# NLG interactive demo template
This is a python / HTML template that you can hook up your NLG model to for people to interact with.
 
## Dependencies
- python3
- ?

## Running the NLG demo
### Connect your NLG model
The easiest thing to do is to create a symbolic link from the repo to the project/model folder
```bash
ln -s SOMEWHERE/nlgwebsite YOUR_PROJECT_DIRECTORY
```

Import the main server method
```python
from nlgwesbite.server import run
```

Your NLG model must be create, instantiated and loaded
```python
myNLGmodel = myNLGClass(hyperparams)
```

It must also have a method that takes in an input string (it doesn't have to do anything with it if you don't want that) and returns an ouput string (your NLG response). For instance:
```python
myNLGmodel.getOutput("Hello this is an input string!")
# returns a generated output
```

### Start up the web server
Start up the demo server by calling the `run` method, feeding your nlg model to it:
```python
run(nlg = myNLGmodel)
```
Then go to your web browser and access the page through http://localhost:8000 (or wherever your server is running).

### Authors
Maarten Sap, other peeps!
