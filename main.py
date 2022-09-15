from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.demoucron import Demoucron
from api.middlewares import valid_matrix

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/{choice}")
def api(demoucron: Demoucron= Depends(valid_matrix)):
    print(demoucron._origin)
    return demoucron.find_path()
