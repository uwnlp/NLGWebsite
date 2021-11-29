# NLG interactive demo template
This is a python / HTML template that you can hook up your NLG model to for people to interact with.
 
## Dependencies
- python3 (`http.server` and `urllib.parse` native libraries)

## Running the NLG demo
### Connect your NLG model
The easiest thing to do is to create a symbolic link from the repo to the project/model folder:
```bash
cd your_project_directory
ln -s SOMEWHERE/NLGWebsite .
```

From a file in `your_project_directory`, import the main server method:
```python
sys.path.append("NLGWebsite")
from server import run
```

Your NLG model must be created, instantiated and loaded
```python
myNLGmodel = myNLGClass(hyperparams) # myNLGClass could be a from_pretrained transformer model, for example
```

It must also have a method that takes in an input string (it doesn't have to do anything with it if you don't want that) and returns an ouput string (your NLG response). For instance:
```python
myNLGmodel.getOutput("Hello this is an input string!")
# returns a generated output string
```

### Start up the web server
Start up the demo server by calling the `run` method, feeding your nlg model to it:
```python
run(nlg = myNLGmodel)
```
Then go to your web browser and access the page through http://localhost:8000 (or wherever your server is running).

You can also run the server with just an output function that takes a str and outputs a str (e.g., `model.getOutput` is one of those functions)
```python
runNoClass(myOutputFunction)
```
## See [example running script](testProjectDir/README.md)

### Authors
Maarten Sap (& maybe other peeps!)
