# mini-RAG

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.10 or later

### Install Python using MiniConda

1) Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/overview)
2) Create a new environment using the following command:

``` bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment using the following command:
``` bash
$ conad activate mini-rag
```

## Installation

### Install the required packages
``` bash
$ pip install -r requirements.txt
```

### Setup environment variables
``` bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPEN_API_KEY` value.

## Run FastAPI server 

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Postman Collection

You can download the Postman collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)