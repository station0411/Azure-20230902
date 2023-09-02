from fastapi import FastAPI
from pydantic import BaseModel

# START : uvicorn sample_fastapi:app --reload

# おまじない
app = FastAPI()

# GETの例
@app.get("/sample/get")
def sample_get(input_a: str, input_b: str):
    return {
        "output_a": input_a,
        "output_b": input_b,
    }

# POSTの例
class SamplePostItem(BaseModel):
    input_a: str
    input_b: str
@app.post("/sample/post")
def sample_post(sample_post_item: SamplePostItem):
    return {
        "output_a": sample_post_item.input_a,
        "output_b": sample_post_item.input_b,
    }