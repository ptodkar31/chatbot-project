from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing! Set it in your .env file.")

openai.api_key = OPENAI_API_KEY

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            user_message = await websocket.receive_text()  
            print(f"User: {user_message}")  

            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": user_message}]
            )

            bot_reply = response["choices"][0]["message"]["content"]  
            print(f"Bot: {bot_reply}") 

            await websocket.send_text(bot_reply)

        except Exception as e:
            print("Error:", e)
            await websocket.send_text("Error: " + str(e))
