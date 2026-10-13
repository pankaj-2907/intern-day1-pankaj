from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory database
users_db = []
current_id = 1

# Request model
class UserCreate(BaseModel):
    name: str
    email: str

# Response model
class UserResponse(BaseModel):
    id: int
    name: str
    email: str


# 1. POST /users - Create a user
@app.post("/users", response_model=UserResponse, status_code = status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global current_id

    # Validate duplicate email
    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    new_user = {
        "id": current_id,
        "name": user.name,
        "email": user.email
    }
    users_db.append(new_user)
    current_id += 1
    return new_user


# 2. GET /users - Return all users
@app.get("/users", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users():
    return users_db


# 3. GET /users/{id} - Return a specific user
@app.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )


# 4. DELETE /users/{id} - Delete a user
@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    global users_db
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            deleted_user = users_db.pop(index)
            return {"message": f"User '{deleted_user['name']}' deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )