from stegano import lsb

new_img=input("Enter Image name : ")
new_img+=".png"

#revealing the encoded message
clear_message=lsb.reveal(new_img)
print(clear_message)
