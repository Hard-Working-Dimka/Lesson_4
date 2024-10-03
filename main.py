from PIL import Image

image = Image.open('image.jpg')
image.convert('RGB')
image_red, image_green, image_blue = image.split()

image_red_crop_left = image_red.crop((100, 0, image_red.width, image_red.height))
image_red_crop_middle = image_red.crop((50, 0, image_red.width - 50, image_red.height))
image_red_crop_result = Image.blend(image_red_crop_left, image_red_crop_middle, 0.3)

image_blue_crop_right = image_blue.crop((0, 0, image_blue.width - 100, image_blue.height))
image_blue_crop_middle = image_blue.crop((50, 0, image_blue.width - 50, image_blue.height))
image_blue_crop_result = Image.blend(image_blue_crop_right, image_blue_crop_middle, 0.3)

image_green_crop_result = image_green.crop((50, 0, image_green.width - 50, image_green.height))

image_merge_result = Image.merge('RGB', (image_red_crop_result, image_green_crop_result, image_blue_crop_result))
image_merge_result.thumbnail((80, 80))
image_merge_result.save('profile_photo.jpg')
