from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (800, 500), "#87ceeb")
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 60)
except:
    font = ImageFont.load_default()

draw.text((300, 300), "Hello Adi ", fill="black", font=font)

img.save("final_pillow_image.png")

print("Image created successfully!")