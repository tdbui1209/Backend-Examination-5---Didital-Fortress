# BACK-END EXAMINATION Digital Fortress

## Project Overview
This project aims to develop a website for managing the light in the user's room.

## Database Diagrams
![db_diagram](https://github.com/tdbui1209/Backend-Examination-5---Didital-Fortress/assets/72682397/c01b88e5-279e-42a3-ba74-e80a55c835c9)

## Project structure
```
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── light_utils.py
│   ├── models.py
│   └── routes.py
│
├── tests/
│   ├── __init__.py
│   ├── test_light_utils.py
│   └── test_routes.py
├── Dockerfile
├── mqtt_cilent.py
├── mqtt_config.yml
├── requirements.txt
└── run.py
```

## How to use
Step 1:
```
docker build -t my-python-app .
```
Step 2:
```
docker run -p 5000:5000 my-python-app
```
