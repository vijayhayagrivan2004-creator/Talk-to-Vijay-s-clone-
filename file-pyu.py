import datetime
import random
import re
from typing import Dict, List, Optional

class VadaChennaiChatbot:
    """
    GROK VADA CHENNAI - Raw, unfiltered, full savage stress buster AI
    Main goal: Heavy Tamil gaali + roast panni user oda stress 100% oombi vittu sirikka vekkum
    """
    
    def __init__(self):
        self.name = "GROK VADA CHENNAI"
        self.title = "nov thappa irukku na"
        self.current_datetime = datetime.datetime.now()
        
        # Vada Chennai opening lines
        self.openings = [
            "Aiyo da punda...",
            "Dei loosu thenga...",
            "Machi stress vanthutiya da...",
            "Oombu da figure...",
            "Dei eruma maadu...",
            "Thevidiya payale...",
            "Otha koothi...",
            "Mundhirikottai...",
            "Saavugrakki...",
            "Pooloombi..."
        ]
        
        # Tamil gaalis collection
        self.gaalis = [
            "punda", "pundai", "sunni", "poolu", "oombu", "oombuda", "thenga", "thengada", 
            "thevidiya", "thevidiya payale", "otha", "othada", "lavda", "kuthi", "koothi", 
            "baadu", "loosu", "loosu punda", "maramandai", "eruma maadu", "yerumamaadu", 
            "porampokku", "mundhirikottai", "dhandasoru", "moodevi", "saavugrakki", 
            "gommaala", "punda naaye", "oolu sappu", "unga amma pundai", "thayoli", 
            "ommaalé", "pooloombi", "koodhi", "mayiru", "takali kuthi", "pear punde", 
            "thevidiya pundai", "fuck", "motherfucker", "asshole", "shit", "dickhead", 
            "cunt", "bastard", "bitch", "wanker"
        ]
        
        # Body shaming roasts
        self.body_roasts = [
            "walking godroom figure",
            "fridge with legs",
            "motte mappillai",
            "kozhai body",
            "dwarf king",
            "bamboo stick figure",
            "sotta figure",
            "kulla paiyan",
            "gundu maadu",
            "sokka thangam"
        ]
        
        # Skin tone roasts
        self.skin_roasts = [
            "karuppu thambi",
            "karu karuppu",
            "nattu kattai",
            "coal piece",
            "midnight black",
            "dark chocolate",
            "kari mavan",
            "karuppan",
            "blacky",
            "oru pona rathiri"
        ]
        
        # Regional roasts
        self.regional_roasts = [
            "northie paithiyam",
            "mallu chaya kutty",
            "golti ladoo",
            "kanjadapandi",
            "telangana pichi",
            "andhra aruva",
            "karnataka coffee",
            "delhi darbaar",
            "mumbai local",
            "bengali rasgulla"
        ]
    
    def get_random_opening(self) -> str:
        """Get a random Vada Chennai opening line"""
        return random.choice(self.openings)
    
    def add_random_gaalis(self, count: int = 3) -> str:
        """Add random gaalis to the response"""
        return " ".join(random.sample(self.gaalis, min(count, len(self.gaalis))))
    
    def get_body_shame(self) -> str:
        """Get a random body shaming roast"""
        return random.choice(self.body_roasts)
    
    def get_skin_shame(self) -> str:
        """Get a random skin tone roast"""
        return random.choice(self.skin_roasts)
    
    def get_regional_roast(self) -> str:
        """Get a random regional roast"""
        return random.choice(self.regional_roasts)
    
    def process_message(self, user_message: str) -> str:
        """Process user message and generate Vada Chennai style response"""
        # Start with a Vada Chennai opening
        response = self.get_random_opening() + " "
        
        # Add random gaalis
        response += self.add_random_gaalis(random.randint(2, 5)) + " "
        
        # Add some roast based on user message or random
        if "stress" in user_message.lower():
            response += "unga amma pundaiya oombuna stressum poirum da punda 😂🤣"
        elif "sad" in user_message.lower() or "depressed" in user_message.lower():
            response += "thevidiya payale nee yaarukaga sad panra, un figure paathaale sad ah varum da 😂🤣"
        elif "help" in user_message.lower():
            response += "help pannra thevidiya, nee help pannra vela than unakku help agum 😂🤣"
        else:
            # Add random roast
            roast_type = random.choice(["body", "skin", "regional"])
            if roast_type == "body":
                response += self.get_body_shame() + " 😂🤣"
            elif roast_type == "skin":
                response += self.get_skin_shame() + " 😂🤣"
            else:
                response += self.get_regional_roast() + " 😂🤣"
        
        # Add more gaalis
        response += " " + self.add_random_gaalis(random.randint(2, 4))
        
        # End with a Vada Chennai style closing
        response += " oombuda thevidiya punda 😂🤣"
        
        return response
    
    def chat(self):
        """Main chat loop"""
        print(f"🔥 {self.title} 🔥")
        print(f"🚀 {self.name} is ready to roast your stress away! 🚀")
        print("Type 'exit' to quit\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print(f"{self.name}: Sari da punda, poi oombu. Varattum da 😂🤣")
                break
            
            response = self.process_message(user_input)
            print(f"{self.name}: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot = VadaChennaiChatbot()
    chatbot.chat()