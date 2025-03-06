from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount static folder to serve frontend
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing! Set it in your .env file.")

openai.api_key = OPENAI_API_KEY

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    chat_history = []  # Store chat history for each session

    while True:
        try:
            user_message = await websocket.receive_text()  # Receive user input
            print(f"User: {user_message}")  

            # Add user message to chat history
            chat_history.append({"role": "user", "content": user_message})

            # Send chat history to OpenAI for context-aware response
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=chat_history
            )

            bot_reply = response["choices"][0]["message"]["content"]  
            print(f"Bot: {bot_reply}") 

            # Add bot reply to chat history
            chat_history.append({"role": "assistant", "content": bot_reply})

            await websocket.send_text(bot_reply)

        except Exception as e:
            print("Error:", e)
            await websocket.send_text("Error: " + str(e))
