## Real-Time Chatbot with GPT-4o-mini

This project is a real-time AI chatbot built using FastAPI, WebSockets, and OpenAI's GPT-4o-mini model. 
It allows users to chat with the bot and get instant responses.

### Features:
1.Real-time messaging using WebSockets

2.Powered by OpenAI's GPT-4o-mini

3.FastAPI for backend processing

4.HTML, CSS, and JavaScript frontend

5.Interactive chat interface

### Setup Instructions :

Step 1 : Create a Virtual Environment and Activate
       
        python -m venv venv
        venv\Scripts\activate 

Step 2 : Install Required Dependencies
         
         pip install -r requirements.txt

Step 3 : Set Up Your OpenAI API Key

Step 4 : Run the FastAPI Server
         
         uvicorn main:app --reload
         This will start the server at http://localhost:8000

Step 6 : Open the Chat Interface
         Open your browser.
         Go to http://localhost:8000/static/index.html.
         Start chatting with the bot!


### How It Works:

#### Backend (FastAPI) - 
1.Handles WebSocket connections for real-time chat.

2.Sends user messages to GPT-4o-mini API.

3.Returns chatbot responses instantly.

4.Serves static frontend files.


#### Frontend (HTML + JavaScript) - 
1.Connects to the WebSocket server.

2.Sends user messages when Enter is pressed or the Send button is clicked.

3.Receives and displays responses from the chatbot.
