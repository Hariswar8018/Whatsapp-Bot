from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}