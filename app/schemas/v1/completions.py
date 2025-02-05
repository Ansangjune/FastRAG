from enum import Enum
from pydantic import BaseModel


class MessageRole(str, Enum):
    client = "client"
    assistant = "assistant"

class CompletionTokenDetails(BaseModel):
    reasoningTokens: int
    acceptedPredictionTokens: int
    rejectedPredictionTokens: int

class ChatUsage(BaseModel):
    promptTokens: int
    completionTokens: int
    totalTotal: int
    completionTokensDetails: CompletionTokenDetails

class Message(BaseModel):
    role: MessageRole
    content: str

class Choice(BaseModel):
    message: Message
    logprobs: int
    finish_reason: str
    index: int

class Responses:
    class ChatCompletions(BaseModel):
        id: str
        object: str
        created: int
        model: str
        usage: ChatUsage
        choices: list[Choice]

class Requests:
    class ChatCompletions(BaseModel):
        model: str
        messages: list[Message]
        temperature: float
