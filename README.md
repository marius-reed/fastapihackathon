# 1. Cloud Hackathon FastAPI

In this hackathon we will 

- [1. Cloud Hackathon FastAPI](#1-cloud-hackathon-fastapi)
- [2. Setup and installation](#2-setup-and-installation)
  - [2.1. 2.1.Clone the FastApiHackathon repository](#21-21clone-the-fastapihackathon-repository)
  - [2.2. Create a virtual environment](#22-create-a-virtual-environment)
  - [Install all required python packages in the virutal environment](#install-all-required-python-packages-in-the-virutal-environment)
- [3. Host your first FastAPI locally](#3-host-your-first-fastapi-locally)

# 2. Setup and installation

## 2.1. 2.1.Clone the FastApiHackathon repository 

```
git clone https://github.com/marius-reed/fastapihackathon.git
```

## 2.2. Create a virtual environment

This is not mandatory, but a good practice to create a virual enviroment where the python packages can be installed to avoid conflicts with other versions.
```
virtualenv .venv
```

## Install all required python packages in the virutal environment
Install all required python packages from the requirements.txt file in the located in the repository.

```
pip install -r requirements.txt
```

# 3. Host your first FastAPI locally

In the repository there is a file called main.py where a very simple FastAPI is defined. To run this API locally on your computer run the following command:

```
uvicorn main:app
```

This will result in the following response.
```
INFO:     Started server process [10721]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Navigate to the URL in your preferred browser:

(/Pictures/fast_api_hello_world))