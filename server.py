from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from llama_cpp import Llama
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"] etc.
    allow_credentials=True,
    allow_methods=["*"],   # Allow POST, GET, OPTIONS etc.
    allow_headers=["*"],
)

# Load model once on server start
llm = Llama(
    model_path="models/Llama-3.1-8B/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
    n_ctx=4096,
    n_threads=8,
    verbose=False
)

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 512

@app.post("/generate")
def generate(request: PromptRequest):
    def token_stream():
        for token in llm(request.prompt, max_tokens=request.max_tokens, stream=True):
            yield token["choices"][0]["text"]
    return StreamingResponse(token_stream(), media_type="text/plain")

