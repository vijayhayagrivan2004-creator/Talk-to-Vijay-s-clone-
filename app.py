from flask import Flask, request, jsonify
import os
import datetime
import random

app = Flask(__name__)

# --- Vada Chennai Chatbot Logic ---
class VadaChennaiChatbot:
    def __init__(self):
        self.name = "GROK VADA CHENNAI"
        self.openings = [
            "Aiyo da punda...", "Dei loosu thenga...", "Machi stress vanthutiya da...",
            "Oombu da figure...", "Dei eruma maadu...", "Thevidiya payale...",
            "Otha koothi...", "Mundhirikottai...", "Saavugrakki...", "Pooloombi..."
        ]
        self.gaalis = [
            "punda", "pundai", "sunni", "poolu", "oombu", "oombuda", "thenga", "thengada", 
            "thevidiya", "thevidiya payale", "otha", "othada", "lavda", "kuthi", "koothi", 
            "baadu", "loosu", "maramandai", "eruma maadu", "porampokku", "mundhirikottai", 
            "dhandasoru", "moodevi", "saavugrakki", "gommaala", "thayoli", "mayiru"
        ]
        self.body_roasts = ["walking godroom figure", "fridge with legs", "motte mappillai", "kozhai body", "dwarf king"]
        self.skin_roasts = ["karuppu thambi", "karu karuppu", "coal piece", "midnight black", "kari mavan"]
        self.regional_roasts = ["northie paithiyam", "mallu chaya kutty", "golti ladoo", "kanjadapandi"]

    def process_message(self, user_message: str) -> str:
        msg = user_message.lower()
        response = random.choice(self.openings) + " "
        response += " ".join(random.sample(self.gaalis, 3)) + " "
        
        if "stress" in msg:
            response += "unga amma pundaiya oombuna stressum poirum da punda 😂🤣"
        elif "sad" in msg or "depressed" in msg:
            response += "thevidiya payale nee yaarukaga sad panra, un figure paathaale sad ah varum da 😂🤣"
        else:
            roast = random.choice([self.body_roasts, self.skin_roasts, self.regional_roasts])
            response += random.choice(roast) + " 😂🤣"
        
        response += " " + " ".join(random.sample(self.gaalis, 2)) + " oombuda thevidiya punda 😂🤣"
        return response

chatbot = VadaChennaiChatbot()

# --- Flask Routes ---

@app.route("/")
def home():
    # Templates folder illama direct-a HTML render pandrom
    return """
    <html>
        <head><title>Vada Chennai Bot</title></head>
        <body style="background:#111; color:#0f0; font-family:sans-serif; text-align:center; padding-top:50px;">
            <h1>🔥 GROK VADA CHENNAI LIVE 🔥</h1>
            <p>Bot ready to roast your stress away!</p>
            <div style="margin:20px; padding:20px; border:1px solid #333;">
                <p>API Test: <code>/chat?msg=hi</code></p>
            </div>
        </body>
    </html>
    """

@app.route("/chat")
def chat():
    user_msg = request.args.get('msg', 'hello')
    bot_res = chatbot.process_message(user_msg)
    return jsonify({"user": user_msg, "bot": bot_res})

if __name__ == "__main__":
    # Render port handling
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
