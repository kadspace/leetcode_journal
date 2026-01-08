import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from groq import Groq

app = FastAPI()

# Configuration
PRACTICE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(PRACTICE_DIR)
SESSION_FILE = os.path.join(PRACTICE_DIR, "practice_session.py")

client = Groq()

class ChatRequest(BaseModel):
    message: str
    code: str

class SaveRequest(BaseModel):
    code: str

def get_repo_context(start_path):
    context = ""
    structure = ""
    for root, dirs, files in os.walk(start_path):
        # Exclude hidden dirs and practice_mode itself
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != "practice_mode" and d != "__pycache__"]
        
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        structure += f"{indent}{os.path.basename(root)}/\n"
        
        for f in files:
            if f.startswith('.'): continue
            
            subindent = ' ' * 4 * (level + 1)
            structure += f"{subindent}{f}\n"

            # If it's a solution or notes file, read content
            if f in ["solution.py", "notes.md"]:
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, start_path)
                try:
                    with open(file_path, "r", encoding="utf-8") as file_content:
                        content = file_content.read()
                        # Simple safety check: don't include huge files
                        if len(content) < 10000:
                            context += f"\n--- BEGIN FILE: {rel_path} ---\n{content}\n--- END FILE ---\n"
                except Exception:
                    pass # Ignore read errors
                    
    return structure, context

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join(PRACTICE_DIR, "index.html"), "r") as f:
        return f.read()

@app.get("/api/context")
async def get_context():
    structure, _ = get_repo_context(ROOT_DIR)
    return {"structure": structure}

@app.post("/api/save")
async def save_code(request: SaveRequest):
    try:
        with open(SESSION_FILE, "w") as f:
            f.write(request.code)
        return {"status": "saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat(request: ChatRequest):
    if not os.environ.get("GROQ_API_KEY"):
         raise HTTPException(status_code=500, detail="GROQ_API_KEY environment variable not set.")

    structure, file_contents = get_repo_context(ROOT_DIR)
    
    # Read AGENTS.md for custom instructions
    agents_file = os.path.join(PRACTICE_DIR, "AGENTS.md")
    custom_instructions = ""
    if os.path.exists(agents_file):
        with open(agents_file, "r") as f:
            custom_instructions = f.read()
    
    system_prompt = (
        "You are a coding coach assisting a user with their LeetCode practice. "
        f"{custom_instructions}\n\n"
        f"The user is working in the following repository structure:\n\n{structure}\n\n"
        "Here is the content of the existing solutions and notes in the repository. "
        "Use this exclusively as reference for the 'correct' or 'past' approaches the user has taken "
        "if they ask about it or if you need to understand their previous work. "
        f"Do NOT leak these solutions unless explicitly asked or if it helps guide them.\n\n{file_contents}\n\n"
        "The user's current code is provided below. Use this context to answer their questions."
    )

    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"My Code:\n```python\n{request.code}\n```\n\nQuestion: {request.message}",
                },
            ],
            model="llama-3.3-70b-versatile", # Using the requested model
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
