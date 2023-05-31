# FastAPI Suggestion Service ![build](https://github.com/Buuntu/fastapi-react/workflows/build/badge.svg)


A Search Suggestion service in python fastAPI, Using 
Trie Data Structure And Redis .

---

## Features

- **[FastAPI](https://fastapi.tiangolo.com/)** (Python 3.8)
  - JWT authentication using [OAuth2 "password
    flow"](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/) and
    PyJWT


 the **redis** package to connect to an in-memory Redis database. The Trie class represents the Trie data structure, with the insert, search, and starts_with methods for inserting words, searching for complete words, and searching for words with a given prefix, respectively. Each node in the Trie is stored as a Redis set, where the key represents the current prefix and the set contains the complete words associated with that prefix.


## Quick Start

First, install the install requirements:

```bash
pip install -r requirements.txt
```

Second, install docker-compose if you don't already have it:

[docker-compose installation official
docs](https://docs.docker.com/compose/install/).

