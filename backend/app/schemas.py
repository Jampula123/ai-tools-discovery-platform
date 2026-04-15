from pydantic import BaseModel, EmailStr


class AIToolSchema(BaseModel):
    id: int
    name: str
    description: str
    created_at: str
    updated_at: str


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str
    updated_at: str


class NewsSchema(BaseModel):
    id: int
    title: str
    content: str
    published_at: str


class NotificationSchema(BaseModel):
    id: int
    user_id: int
    message: str
    is_read: bool
    created_at: str