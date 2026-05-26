from fastapi import APIRouter
from pydantic import BaseModel
import json

router = APIRouter()

# LOAD JSON DATA

with open("app/beachdetails.json", "r", encoding="utf-8") as file:
    beach_data = json.load(file)

# REQUEST MODEL

class ChatRequest(BaseModel):
    message: str

# CHAT ENDPOINT

@router.post("/chat")

async def chat(request: ChatRequest):

    user_message = request.message.lower()

    # SEARCH BEACHES

    for beach in beach_data:

        beach_name = beach["name"].lower()

        city_name = beach["city"].lower()

        if beach_name in user_message or city_name in user_message:

            response = f"""
🏖 {beach['name']} — {beach['city']}

📖 {beach['description']}

🎯 Activities:
{", ".join(beach['activities'])}

🗓 Best Time:
{beach['best_time']}

🏨 Stay:
{beach['stay']['name']}

📞 Contact:
{beach['stay']['phone']}
"""

            return {
                "response": response
            }

    # IF NOT FOUND

    return {
        "response":
        "Sorry, I couldn't find information about that beach yet 🌊"
    }