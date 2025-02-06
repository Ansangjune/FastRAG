from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from app.schemas.v1.completions import Responses
from app.llm.chain import ragChain


class ChatService:
    @staticmethod
    def completions(data: dict) -> Responses.ChatCompletions:
        try:
            lastUserQuery = next((msg["content"] for msg in reversed(data["messages"]) if msg["role"] == "client"), None)
            # Make completion.
            content = ragChain.invoke(lastUserQuery)

            response_data = {
                "id": "chatcmpl-123",
                "object": "chat.completion",
                "created": int(datetime.now(timezone(timedelta(hours=9))).timestamp()),
                "model": data.get("model"),
                "usage": {
                    "promptTokens": 0,
                    "completionTokens": 0,
                    "totalTotal": 0,
                    "completionTokensDetails": {
                        "reasoningTokens": 0,
                        "acceptedPredictionTokens": 0,
                        "rejectedPredictionTokens": 0
                    }
                },
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": content
                        },
                        "logprobs": 0,
                        "finish_reason": "stop",
                        "index": 0
                    }
                ]
            }

            return response_data
        except Exception as E:
            print(E)
            raise HTTPException(500, str(E))
