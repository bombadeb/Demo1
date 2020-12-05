**Building the docker file**
```
sudo docker build --tag search-autocomplete-app .
```

**Running the docker file**
Make sure you are in root directory of the project and run the following command
```
sudo docker run --name search-autocomplete-app -p 5001:5001 search-autocomplete-app
```

**Prerequisite**
1. Docker installed in the machine for build
2. Redis installation (IP needs to be updated in the app.py for redis connection)
