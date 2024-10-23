import requests

class LLMClient:
    def __init__(self, api_url, model_name):
        self.api_url = api_url
        self.model_name = model_name
        self.history = []

    def send_message(self, message, options=None):
        user_message = {
            "role": "user",
            "content": message
        }

        self.history.append(user_message)

        payload = {
            "model": self.model_name,
            "messages": self.history,
            "stream": False
        }

        if options:
            payload["options"] = options

        response = requests.post(f"{self.api_url}/chat", json=payload)
        response_data = response.json()


        if (not response.ok):
            return {"error": response.status_code, "msg": response.text}

        assistant_message = {
            "role": "assistant",
            "content": response_data.get("message", {}).get("content", "")
        }
        self.history.append(assistant_message) 
        
        return assistant_message["content"]
    