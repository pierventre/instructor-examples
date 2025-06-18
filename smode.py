# SPDX-FileCopyrightText: (C) 2025 pierventre
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import List
import os
from openai import OpenAI
import instructor

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    addresses: List[Address]

localai_url = "http://localhost:8080/v1"

# Initialize with API key
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=localai_url,
)

# Enable instructor patches for OpenAI client
client = instructor.from_openai(client)

user = client.chat.completions.create_partial(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Create a user profile for Jason, age 25. He lives at 123 Main St, New York, USA"},
    ],
    response_model=User,
)

for user_partial in user:
    print(user_partial)
    for address in user_partial.addresses:
        print(address)

print("#######################################\n")

users = client.chat.completions.create_iterable(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": """
            Extract users:
            1. Jason is 25 years old, He lives at 123 Main St, New York, USA.
            2. Sarah is 30 years old, She lives at 456 Elm St, Los Angeles, USA.
            3. Mike is 28 years old, He lives at 789 Oak St, Chicago, US.
        """},
    ],
    response_model=User,
)

for user in users:
    print(user)
    for address in user.addresses:
        print(address)