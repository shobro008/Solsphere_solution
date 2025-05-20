from fastapi import FastAPI
from API import routes, models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routes.router)
