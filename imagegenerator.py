import openai
import requests

# Set up your API key
openai.api_key = "YOUR API KEY"

# Function to generate an image
def generate_image(prompt, size="1024x1024"):
    try:
        # Call the OpenAI API for image generation
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size=size  # Image resolution
        )
        # Get the URL of the generated image
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to download and save the image locally
def save_image(image_url, filename):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image successfully saved as {filename}")
        else:
            print("Failed to download the image.")
    except Exception as e:
        print(f"Error: {e}")

# Get the image prompt from the user
image_prompt = input("Enter a description for the image: ")

# Generate the image
image_url = generate_image(image_prompt)

if image_url:
    print(f"Generated Image URL: {image_url}")
    # Save the image locally
    save_image(image_url, "generated_image.png")
