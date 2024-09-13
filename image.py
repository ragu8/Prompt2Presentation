import requests
from PIL import Image
from io import BytesIO
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# Download the image
image_response = requests.get(image_url)

# Open the image using Pillow
image = Image.open(BytesIO(image_response.content))

# Save the image as a PNG
image.save("cude.png", "PNG")

print("Image saved as white_siamese_cat.png")