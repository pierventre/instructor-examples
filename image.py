from instructor.multimodal import Image
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI
import os

class ImageDescription(BaseModel):
    objects: list[str] = Field(..., description="The objects in the image")
    scene: str = Field(..., description="The scene of the image")
    colors: list[str] = Field(..., description="The colors in the image")

localai_url = "http://localhost:8080/v1"

# Initialize with API key
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=localai_url,
)

client = instructor.from_openai(client)

url = "https://raw.githubusercontent.com/instructor-ai/instructor/main/tests/assets/image.jpg"
# Multiple ways to load an image:
response = client.chat.completions.create(
    model="gpt-4o",
    response_model=ImageDescription,
    messages=[
        {
            "role": "user",
            "content": [
                "What is in this image?",
                # Option 1: Direct URL with autodetection
                Image.from_url(url),
            ],
        },
    ],
)

print(response)
