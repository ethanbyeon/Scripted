from PIL import Image

# ASCII characters used by level of intensity for the output text
ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', 
    '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 
    'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 
    'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't',
    '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']',
    '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', 
    ';', ':', ',', '"', '^', '`', '.']


# scale image based on the new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel through grayscale process
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    
    # access an image from user-input
    path = input("Please enter a valid path name to an image:\n")

    try:
        img = Image.open(path)
    except:
        print(path, "is not a valid path name to an image.")
        return
    
    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(img)))

    # format the image
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    # print(ascii_image)

    # save the image to a .txt file
    with open("ascci_image.txt", "w") as f:
        f.write(ascii_image)
    
main()