#!/usr/bin/env python3
import argparse
from llama_cpp import Llama

# Load your model once
llm = Llama(
    model_path="models/Llama-3.1-8B/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
    n_ctx=51200,   # context window
    n_threads=8,  # adjust to CPU cores
    verbose=False
)

def main():
    parser = argparse.ArgumentParser(description="LLaMA CLI")
    parser.add_argument("-p", "--prompt", type=str, help="Prompt to send to the model")
    parser.add_argument("-n", "--max_tokens", type=int, default=51200, help="Maximum tokens to generate")
    parser.add_argument("--stream", action="store_true", help="Stream tokens as they are generated")
    args = parser.parse_args()

    if not args.prompt:
        print("Please provide a prompt using -p or --prompt")
        return

    if args.stream:
        # Streaming output
        print("[Assistant]: ", end="", flush=True)
        for token in llm(args.prompt, max_tokens=args.max_tokens, stream=True):
            text = token["choices"][0]["text"]
            print(text, end="", flush=True)
        print()
    else:
        # Non-streaming
        output = llm(args.prompt, max_tokens=args.max_tokens)
        print("[Assistant]:", output["choices"][0]["text"].strip())

if __name__ == "__main__":
    main()

