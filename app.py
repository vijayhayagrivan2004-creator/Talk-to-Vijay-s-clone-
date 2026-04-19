from flask import Flask, request, jsonify
import os
import datetime
import random

app = Flask(__name__)

# --- Vada Chennai Chatbot Logic ---
class VadaChennaiChatbot:
    def __init__(self):
        self.name = "Talk with Vijay's clone 👺!!"
        self.openings = [
            "Aiyo da punda...", "Dei loosu thenga...", "Machi stress vanthutiya da...",
            "Oombu da figure...", "Dei eruma maattu koothi.", "Thevidiya payale...",
            "Otha koothi...", "kudhurakotta..", "Saavugrakki...", "Pooloombi..."
        ]
        self.gaalis = [
            "punda", "pundai", "sunni", "poolu", "oombu", "oombuda", "thenga", "thengada", 
            "thevidiya", "thevidiya payale", "otha", "othada", "lavda", "kuthi", "koothi", 
            "baadu", "loosu", "maramandai", "eruma maadu", "porampokku", "mundhirikottai", 
            "dhandasoru", "moodevi", "saavugrakki", "gommaala", "thayoli", "mayiru"
        ]
        self.body_roasts = ["kutty kunjii", "thevdiya koothi", "poolumbi", "omaleyy deiii", "koothiyan"]
        self.skin_roasts = ["tight pussy", "karuppu kunjii", "koo🔥", "otha pundaa", "thevdiya mavan"]
        self.regional_roasts = ["punda paithiyam", "adingu un vaila yen poola vittu aata", "poi un appan poola sappu", "kanjakuduki"]

    def process_message(self, user_message: str) -> str:
        msg = user_message.lower()
        response = random.choice(self.openings) + " "
        response += " ".join(random.sample(self.gaalis, 3)) + " "
        
        if "stress" in msg:
            response += "unga appa poola oombuna stressum poirum da punda 🤣"
        elif "sad" in msg or "depressed" in msg:
            response += "thevidiya payale nee yaarukaga sad panra, un figure paathaale erijal varum da 😂🤣"
        else:
            roast = random.choice([self.body_roasts, self.skin_roasts, self.regional_roasts])
            response += random.choice(roast) + " 😂🤣"
        
        response += " " + " ".join(random.sample(self.gaalis, 2)) + " oombuda thevidiya punda 😂🤣"
        return response

chatbot = VadaChennaiChatbot()
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Talk with Vijay's clone 👺!!</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #000; color: #0f0; font-family: 'Courier New', Courier, monospace; display: flex; flex-direction: column; height: 100vh; margin: 0; }
                #chat-box { flex: 1; overflow-y: auto; padding: 20px; border-bottom: 1px solid #333; }
                .input-area { padding: 20px; display: flex; background: #111; position: sticky; bottom: 0; }
                input { flex: 1; padding: 12px; background: #222; border: 1px solid #444; color: #0f0; outline: none; border-radius: 5px; font-size: 16px; }
                button { padding: 10px 20px; background: #0f0; border: none; color: #000; font-weight: bold; cursor: pointer; margin-left: 10px; border-radius: 5px; }
                .user { color: #fff; margin-bottom: 10px; padding: 5px; text-align: right; }
                .bot { color: #0f0; margin-bottom: 20px; font-weight: bold; border-left: 3px solid #0f0; padding-left: 10px; line-height: 1.4; text-align: left; }
            </style>
        </head>
        <body>
            <h2 style="text-align:center; padding: 10px; border-bottom: 1px solid #333; margin:0; </h1> Talk with Vijay's clone 👺!!</h2>
            <div id="chat-box">
                <div class="bot"><b>Bot:</b> Enna da, stress-ah irukiya? Message pannu, roast me nu mattum ketratha! 😂</div>
            </div>
            <div class="input-area">
                <input type="text" id="userMsg" placeholder="Type here..." onkeypress="if(event.key==='Enter') sendMsg()">
                <button onclick="sendMsg()">SEND</button>
            </div>
            <script>
                async function sendMsg() {
                    const input = document.getElementById('userMsg');
                    const box = document.getElementById('chat-box');
                    const val = input.value.trim();
                    if(!val) return;

                    box.innerHTML += `<div class="user"><b>You:</b> ${val}</div>`;
                    input.value = '';
                    box.scrollTop = box.scrollHeight;
                    
                    try {
                        const res = await fetch(`/chat?msg=${encodeURIComponent(val)}`);
                        const data = await res.json();
                        box.innerHTML += `<div class="bot"><b>Bot:</b> ${data.bot}</div>`;
                    } catch (e) {
                        box.innerHTML += `<div class="bot" style="color:red;"><b>Error:</b> Server oombidichi nanba!</div>`;
                    }
                    box.scrollTop = box.scrollHeight;
                }
            </script>
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
