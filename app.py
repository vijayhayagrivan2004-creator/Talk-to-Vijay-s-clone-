from flask import Flask, request, jsonify
import os
import random

app = Flask(__name__)

# --- Vada Chennai Chatbot Logic ---
class VadaChennaiChatbot:
    def __init__(self):
        self.name = "Talk with Vijay's clone 👺!!"
        
        self.openings = [
            "Aiyo da punda...", "Dei loosu thenga...", "Machi stress vanthutiya da...",
            "Oombu da figure...", "Dei eruma maattu koothi.", "Thevidiya payale...",
            "Otha koothi...", "Kudhurakotta..", "Saavugrakki...", "Pooloombi..."
        ]
        
        self.gaalis = [
            "punda", "pundai", "sunni", "poolu", "oombu", "thenga", "thevidiya", 
            "otha", "lavda", "kuthi", "koothi", "baadu", "loosu", "maramandai", 
            "eruma maadu", "porampokku", "saavugrakki", "thayoli", "mayiru"
        ]
        
        self.body_roasts = ["kutty kunjii", "thevdiya koothi", "poolumbi", "omaleyy deiii", "koothiyan"]
        self.skin_roasts = ["tight pussy", "karuppu kunjii", "koo🔥", "otha pundaa", "thevdiya mavan"]
        self.regional_roasts = [
            "punda paithiyam", 
            "adingu un vaila yen poola vittu aata", 
            "poi un appan poola sappu", 
            "kanjakuduki"
        ]

    def process_message(self, user_message: str) -> str:
        msg = user_message.lower().strip()
        response = random.choice(self.openings) + " "
        
        # Always add some gaalis
        response += " ".join(random.sample(self.gaalis, min(3, len(self.gaalis)))) + " "
        
        # Conditional roasts
        if any(word in msg for word in ["stress", "tension", "pressure"]):
            response += "unga appa poola oombuna stressum poirum da punda 🤣 "
        elif any(word in msg for word in ["sad", "depressed", "feel bad", "cry"]):
            response += "thevidiya payale nee yaarukaga sad panra? Un figure paathaale erijal varum da 😂 "
        else:
            roast_list = random.choice([self.body_roasts, self.skin_roasts, self.regional_roasts])
            response += random.choice(roast_list) + " 😂🤣 "
        
        # Final gaali blast
        response += " ".join(random.sample(self.gaalis, min(2, len(self.gaalis)))) + " oombuda thevidiya punda 😂🤣"
        
        return response.strip()


chatbot = VadaChennaiChatbot()


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Talk with Vijay's clone 👺!!</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { 
                    background: #000; 
                    color: #0f0; 
                    font-family: 'Courier New', Courier, monospace; 
                    margin: 0; 
                    padding: 0; 
                    height: 100vh; 
                    display: flex; 
                    flex-direction: column;
                }
                h1 { 
                    text-align: center; 
                    padding: 15px; 
                    margin: 0; 
                    background: #111; 
                    border-bottom: 2px solid #0f0;
                }
                #chat-box { 
                    flex: 1; 
                    overflow-y: auto; 
                    padding: 20px; 
                    background: #050505;
                }
                .input-area { 
                    padding: 15px; 
                    background: #111; 
                    display: flex; 
                    gap: 10px;
                }
                input { 
                    flex: 1; 
                    padding: 14px; 
                    background: #222; 
                    border: 1px solid #444; 
                    color: #0f0; 
                    outline: none; 
                    border-radius: 6px; 
                    font-size: 16px;
                }
                button { 
                    padding: 14px 24px; 
                    background: #0f0; 
                    border: none; 
                    color: #000; 
                    font-weight: bold; 
                    cursor: pointer; 
                    border-radius: 6px;
                }
                .user { 
                    color: #fff; 
                    text-align: right; 
                    margin: 12px 0; 
                }
                .bot { 
                    color: #0f0; 
                    margin: 15px 0; 
                    padding-left: 12px; 
                    border-left: 4px solid #0f0; 
                    line-height: 1.5;
                }
            </style>
        </head>
        <body>
            <h1>Talk with Vijay's clone 👺!!</h1>
            <div id="chat-box">
                <div class="bot"><b>Bot:</b> Enna da, stress-ah irukiya? Message pannu machi... full gaali + roast waiting for you 😂</div>
            </div>
            <div class="input-area">
                <input type="text" id="userMsg" placeholder="Type here da punda..." onkeypress="if(event.key==='Enter') sendMsg()">
                <button onclick="sendMsg()">SEND GAALI</button>
            </div>

            <script>
                async function sendMsg() {
                    const input = document.getElementById('userMsg');
                    const box = document.getElementById('chat-box');
                    const val = input.value.trim();
                    if (!val) return;

                    box.innerHTML += `<div class="user"><b>You:</b> ${val}</div>`;
                    input.value = '';
                    box.scrollTop = box.scrollHeight;

                    try {
                        const res = await fetch('/chat', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({msg: val})
                        });
                        const data = await res.json();
                        box.innerHTML += `<div class="bot"><b>Bot:</b> ${data.bot}</div>`;
                    } catch (e) {
                        box.innerHTML += `<div class="bot" style="color:red;"><b>Error:</b> Server oombidichi da!</div>`;
                    }
                    box.scrollTop = box.scrollHeight;
                }
            </script>
        </body>
    </html>
    """


@app.route("/chat", methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('msg', '') if data else ''
    
    if not user_msg:
        return jsonify({"bot": "Enna da silent ah irukke? Type pannu loosu!"})
    
    bot_res = chatbot.process_message(user_msg)
    return jsonify({"bot": bot_res})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)