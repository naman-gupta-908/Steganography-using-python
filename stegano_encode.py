from stegano import lsb
image=input("Enter Input Image name: ")
image+=".png"
new_img=input("Enter new Image name : ")
new_img+=".png"
msg=input("Enter message to be decoded : ")

#hiding the message
lsb.hide(image,message=msg).save(new_img)
