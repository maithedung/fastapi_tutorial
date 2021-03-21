from database import engine
import models
from fastapi import FastAPI
from routers import blog, user, authentication


app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)


'''
@app -> Path Operation Decorator
get -> Operation
('/') -> Path
def index(): ... -> Path Operation Function
'''


@app.get("/")
async def root():
    return {"message": "Hello Applications!"}


# if __name__ == '__main__':
#     uvicorn.run(app, host='localhost', port=8080)
