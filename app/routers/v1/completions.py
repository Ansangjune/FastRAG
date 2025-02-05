from fastapi import APIRouter
from app.schemas.v1.completions import Responses, Requests
from app.services.v1.completions import ChatService

router = APIRouter(tags=["Chat Completions"])


@router.post("", response_model=Responses.ChatCompletions, summary="답변 생성")
def chatCompletions(
        body:Requests.ChatCompletions):
    return ChatService.completions(body.model_dump())
