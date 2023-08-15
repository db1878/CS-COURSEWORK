from PIL import Image

def cut_image_into_16x16(image_path):
    # Open the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except OSError:
        print("Error: Unable to open the image.")
        return

    # Get the dimensions of the image
    width, height = image.size

    # Check if the image dimensions are divisible by 16
    if width % 16 != 0 or height % 16 != 0:
        print("Error: Image dimensions are not divisible by 16.")
        return

    # Calculate the number of rows and columns for the 16x16 images
    rows = height // 16
    cols = width // 16

    # Cut the image into 16x16 images
    for row in range(rows):
        for col in range(cols):
            # Define the coordinates of the current 16x16 block
            left = col * 16
            upper = row * 16
            right = left + 16
            lower = upper + 16

            # Crop the image to get the 16x16 block
            block = image.crop((left, upper, right, lower))

            # Save the 16x16 block as a new image
            block.save(f"block_{row}_{col}.png")

    print(f"{rows * cols} 16x16 images created.")

if __name__ == "__main__":
    image_path = "Map/levels/images/Tiles/Assets/plants.png"  # Replace with the path to your image
    cut_image_into_16x16(image_path)
