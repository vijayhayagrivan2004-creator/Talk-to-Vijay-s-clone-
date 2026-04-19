from flask import Flask, request, jsonify
import os
import random

app = Flask(__name__)

class VadaChennaiChatbot:
    def __init__(self):
        self.name = "Talk with Vijay's clone 👺!!"
        
        self.openings = [
            "Aiyo da loosu kuthi...", "Dei maramandai payale...", "Machi enna da ivlo thenga irukke...",
            "Oombu da figure oombi...", "Dei eruma maadu koothi...", "Thevidiya mavan da nee...",
            "Otha pundaiya... enna da varra...", "Kudhirakotta baadu...", "Saavugrakki thayoli...",
            "Pooloombi mundhirikottai...", "Gotha punda naaye...", "Adhigaprasangi moodevi..."
        ]
        
        self.gaalis = [
            "punda", "pundai", "sunni", "poolu", "oombu", "thenga", "thevidiya", "otha", 
            "lavda", "kuthi", "koothi", "baadu", "loosu", "maramandai", "eruma maadu", 
            "porampokku", "saavugrakki", "thayoli", "mayiru", "gommaala", "dhandasoru", 
            "mundhirikottai", "moodevi", "adhigaprasangi", "arivuketta mundam", "vesi mavane",
            "punda naaye", "koothi kalutha", "oolu sappu", "badu", "thayozhi"
        ]
        
        self.body_roasts = [
            "kutty kunji poolumbi", "thevdiya koothi figure", "omaleyy deiii soothu", 
            "koothiyan nakki", "pundaiya virichu kaatu", "sunni thooki aadu da"
        ]
        
        self.skin_roasts = [
            "karuppu kunji pundai", "tight pussy oombi", "koo🔥 karuppu figure", 
            "otha pundaa black beauty", "thevdiya mavan dark mode", "mayiru full karupu"
        ]
        
        self.family_roasts = [
            "un amma poola oombu", "poi un appan soothula poola vachu aadu", 
            "un thaatha pundaiya nakku", "un amma thevidiya payale", "unga veetla ellarum oombi"
        ]
        
        self.regional_roasts = [
            "punda paithiyam full form", "adingu un vaila yen poola vittu aata da", 
            "poi un appan poola sappu da", "kanjakuduki loosu", "arivu illa pundai",
            "vesi mavane full charge", "puramboku baadu"
        ]

    def process_message(self, user_message: str) -> str:
        msg = user_message.lower().strip()
        
        # Start with strong opening
        response = random.choice(self.openings) + " "
        
        # Mix 4-5 unique gaalis (no repetition in one response)
        selected_gaalis = random.sample(self.gaalis, min(5, len(self.gaalis)))
        response += " ".join(selected_gaalis) + " "
        
        # Conditional savage replies
        if any(word in msg for word in ["stress", "tension", "pressure", "work", "job"]):
            response += "unga amma poola oombuna stress full ah poidum da thayoli 🤣 "
        elif any(word in msg for word in ["sad", "depressed", "cry", "feel bad", "lonely", "heartbreak"]):
            response += "thevidiya payale nee enna da sad panra? Un figure paathaale en poolu thookum da 😂 "
        elif any(word in msg for word in ["love", "girlfriend", "figure", "crush"]):
            response += "un figure ah en sunni ku oombu vachu tharuva da pundai... love varum nu nenaikura 🤣 "
        else:
            # Random roast category
            roast_list = random.choice([self.body_roasts, self.skin_roasts, self.family_roasts, self.regional_roasts])
            response += random.choice(roast_list) + " 😂🤣 "
        
        # Final blast with 3 more unique gaalis
        remaining_gaalis = [g for g in self.gaalis if g not in selected_gaalis]
        if remaining_gaalis:
            final_gaalis = random.sample(remaining_gaalis, min(3, len(remaining_gaalis)))
            response += " ".join(final_gaalis) + " "
        
        response += "oombuda thevidiya punda full ah erinjidu da 🔥🤣"
        
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
                body { background: #000; color: #0f0; font-family: 'Courier New', Courier, monospace; margin: 0; padding: 0; height: 100vh; display: flex; flex-direction: column; }
                h1 { text-align: center; padding: 15px; margin: 0; background: #111; border-bottom: 3px solid #f00; color: #f00; }
                #chat-box { flex: 1; overflow-y: auto; padding: 20px; background: #050505; }
                .input-area { padding: 15px; background: #111; display: flex; gap: 10px; }
                input { flex: 1; padding: 14px; background: #222; border: 2px solid #f00; color: #0f0; outline: none; border-radius: 6px; font-size: 16px; }
                button { padding: 14px 28px; background: #f00; border: none; color: #000; font-weight: bold; cursor: pointer; border-radius: 6px; }
                .user { color: #fff; text-align: right; margin: 15px 0; }
                .bot { color: #0f0; margin: 18px 0; padding-left: 15px; border-left: 5px solid #f00; line-height: 1.6; }
            </style>
        </head>
        <body>
            <h1>Talk with Vijay's clone 👺!! (Wild Mode 🔥)</h1>
            <div id="chat-box">
                <div class="bot"><b>Bot:</b> Enna da punda... innum wild ah venuma? Full gaali + family roast waiting... message pannu thayoli! 😂🤣</div>
            </div>
            <div class="input-area">
                <input type="text" id="userMsg" placeholder="Type pannu da... enna venumna ketkalaam" onkeypress="if(event.key==='Enter') sendMsg()">
                <button onclick="sendMsg()">SEND GAALI 🔥</button>
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
                        box.innerHTML += `<div class="bot" style="color:red;"><b>Error:</b> Server oombidichi da punda!</div>`;
                    }
                    box.scrollTop = box.scrollHeight;
                }
            </script>
        </body>
    </html>
    """


@app.route("/chat", methods=['POST'])
def chat():
    data = request.get_json(silent=True)
    user_msg = data.get('msg', '') if data else ''
    
    if not user_msg or len(user_msg.strip()) < 1:
        return jsonify({"bot": "Enna da silent ah irukke? Gaali thooku da loosu! 🔥"})
    
    bot_res = chatbot.process_message(user_msg)
    return jsonify({"bot": bot_res})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)