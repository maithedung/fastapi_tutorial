Automatics Docs

- Swagger UI
- ReDoc

Based on open standards

- JSON Schema
- Open API

Security and authentication

- HTTP Basic
- OAuth2 (aslo with JWT tokens)
- API keys in Headers/Query parameters/Cookies/etc

Starlette Features

p

Part 0: Setup Virtual Environments + Packages

- python3 --version
- python3 -m venv .
- source bin/activate
- pip3 list
- python3 -m pip install --upgrade pip
- pip3 install fastapi
- pip3 install uvicorn | uvicorn --version
- uvicorn main:app --reload
- git init
- .gitignore file
- git status
- git add .
- git commit -m 'fast-api tutorial'

Part 1: Basics concepts

- Path parameters
- API Docs - swagger/redocs
- Query parameters
- Request body

Part 2: Intermediate Concepts

- Debugging FastAPI
- Pydantic Schemas
- SQLAlchemy database connection
- Models and table

Part 3: Database Tasks

- Store blog to database
- Get blogs from database
- Delete
- Update

Part 4: Responses

- Handling Exceptions
- Return response
- Define response model

Part 5: User and Password

- Create user
- Hash user password
- Show single user
- Define docs tags

Part 6: Relationship

- Define User to Blog relationship
- Define Blog to User relationship

Part 7: Refactor for bigger Application

- API Router
- API Router with parameters

Part 8: Authentication using JWT

- Create Login route
- Login and verify password
- Return JWT access token
- Routers behind authentication

Part 9: Deploy FastAPI

- Using Deta.sh website to deploy
