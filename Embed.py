from PIL import Image #for image processing

#converts binary strings into readable text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

#converts text to binary 
def text_to_binary(text):    
    #takes each char in the message and turns it into its 8 bit binary counterpart
    return ''.join(format(ord(char), '08b') for char in text)

# Function hides a message inside of an image using stenography
def encrypt_image(input_image, output_path, text, key=5):        
    img = Image.open(input_image).convert("RGB") #make sure the image is in RGB mode
    pixels = img.load()
    
    bin_text = text_to_binary(text) + '1111111111111110' #1111111111111110 is an end of message marker, so we can make decrypting simple
    data_index = 0
    
    #Loop through the image pixels row by row, modifying every key'th pixel
    #match this key to the key in the decrypt function
    for y in range(img.height):
        for x in range(0, img.width, key):
            #message is done being processed
            if data_index >= len(bin_text):
                break
            
            #rgb values of current pixel
            r, g, b = pixels[x, y]
            
            #embeds the next bit of the message into the LSB of the blue channel. 
            if data_index < len(bin_text):
                b =  (b & ~1) | int(bin_text[data_index])
                data_index += 1

            #updates the pixel with the new blue value    
            pixels[x,y] = (r, g, b)

    #save the image to the output path        
    img.save(output_path, "BMP")
    print(f"Text hidden in {output_path} successfully...\n")


#function extracts the hidden text from an image        
def decrypt_text(input_image, key=5):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()
    
    bin_text = ""

    #loop through the image pixels row by row, reading every key'th pixel
    #this key MUST be the same as the key in the encrypt function
    for y in range(img.height):
        for x in range(0, img.width, key):
            #rgb values of current pixel
            r, g, b = pixels[x,y]
            #extracts the LSB of the blue channel
            bin_text += str(b & 1)
            
            #checking for the message ending marker
            if bin_text[-16:] == "1111111111111110":
                #exclude the marker and convert the binary to text
                return binary_to_text(bin_text[:-16])
    
    return "Error: Expected message in image was not found."

#main function handles cli args
def main():
   #encrypt_image("monkey.png", "output.png", "this is a monkey text")
   print(decrypt_text("output.png"))
        
if __name__ == "__main__":
    main()