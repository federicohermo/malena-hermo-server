from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from email_service import send_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:9000",  # Your local frontend
        "https://malenahermo.netlify.app/",  # Production frontend
    ], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the email request
class EmailRequest(BaseModel):
    sender: str
    subject: str
    message: str

# Route for sending email
@app.post("/send-email/")
async def send_email_route(email_request: EmailRequest):
    try:
        # Call the send_email function
        send_email(
            sender=email_request.sender,
            subject=email_request.subject,
            message=email_request.message
        )
        return {"message": "Email sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))