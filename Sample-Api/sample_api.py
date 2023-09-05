from fastapi import FastAPI
from pydantic import BaseModel
from time import sleep

# START : uvicorn sample_api:app --reload --port=8901

# おまじない
app = FastAPI()

class SamplePostItem(BaseModel):
    some_input: str

@app.post("/api1")
def sample_post(sample_post_item: SamplePostItem):
    # DEBUG用
    print(f"START: sample_post")

    # 何かしらの処理
    print(f"INPUT:{sample_post_item.some_input}")
    sleep(3)

    # DEBUG用
    print(f"END  : sample_post")
    return {
        "some_list": ["A", "B", "C", "D"]
    }