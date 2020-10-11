# onTheFly

## Server Daemon
API server responsible for all the interactions with the codebase

### Setup:

```
python3 -m pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
flask run
```

[Click](http://127.0.0.1:5000) here after setting it up to access it.

### API(s)
* Create a project:
```
curl --location --request POST '127.0.0.1:5000/project/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "abcd"
}'
```
* Delete the project created above project:
```
curl --location --request POST '127.0.0.1:5000/project/delete' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "abcd"
}'
```
