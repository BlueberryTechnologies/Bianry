from PIL import Image #for image processing
import sys #for cli

#converts binary strings into readable text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

#converts text to binary 
def text_to_binary(text):    
    #takes each char in the message and turns it into its 8 bit binary counterpart
    return ''.join(format(ord(char), '08b') for char in text)

# Function hides a message inside of an image using steganography
def encrypt_image(input_image, output_path, text, interval=5):        
    img = Image.open(input_image).convert("RGB") #make sure the image is in RGB mode
    pixels = img.load()
    
    bin_text = text_to_binary(text) + '1111111111111110' #1111111111111110 is an end of message marker, so we can make decrypting simple
    data_index = 0
    
    #Loop through the image pixels row by row, modifying every interval'th pixel
    #match this interval to the interval in the decrypt function
    for y in range(img.height):
        for x in range(0, img.width, interval):
            #message is done being processed
            if data_index >= len(bin_text):
                break
            
            #rgb values of current pixel
            r, g, b = pixels[x, y]
            
            #embeds the next bti of the message into the LSB of the blue channel. 
            if data_index < len(bin_text):
                b =  (b & ~1) | int(bin_text[data_index])
                data_index += 1

            #updates the pixel with the new blue value    
            pixels[x,y] = (r, g, b)

    #save the image to the output path        
    img.save(output_path, "BMP")
    print(f"Text hidden in {output_path} successfully...\n")


#function extracts the hidden text from an image        
def decrypt_text(input_image, interval=5):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()
    
    bin_text = ""

    #loop through the image pixels row by row, reading every interval'th pixel
    #this interval MUST be the same as the interval in the encrypt function
    for y in range(img.height):
        for x in range(0, img.width, interval):
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
    #checks if the user gave us enough args
    if len(sys.argv) < 2:
        #instructions here
        print("Usage:\n")
        print("\tembed_message <input image> <output path> <message>\n")
        print("\textract_message <input image>")
        sys.exit(1)

    #determines which command we are using from the first arg    
    command = sys.argv[1]
    
    if command == "embed_message":
        #embedding needs 4 args
        if len(sys.argv) != 5:
            print("Usage: embed_message <input image> <output path> <message>")
            sys.exit(1)

        if (sys.argv[2][-4:] == ".bmp"): #if its a bmp image then we can continue to check the message size
            if len(sys.argv[4]) <= 256: #if the messaeg size is correct then we can continue to encrypt the image. 
                encrypt_image(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                print("Error: Message is too long, maximum message length is 256 characters...")
        else:
            print("Error: Please use a bmp image...")

    elif command == "extract_message":
        #extracting needs 2 args
        if len(sys.argv) != 3:
            print("Usage: extract_message: <input image>")
            sys.exit(1)
            
        if (sys.argv[2][-4:] == ".bmp"):
            decrypted_message = decrypt_text(sys.argv[2])
            print("Extracted text: ", decrypted_message)
        
    else:
        #user entered an unkown command
        print("Unkown command... Use 'embed_message' or 'extract_message'.")
        sys.exit(1)
        
if __name__ == "__main__":
    main()