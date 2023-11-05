import replicate

def img_descriptiongen(image_path, prompt):
    output = replicate.run(
    "yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591",
    input={
        "image": open("path/to/file", "rb"),
        "prompt": f"You are an expert in crafting SEO-optimized product descriptions for ecommerce sales. Please create a compelling product description for this item. {prompt}",
        }
    )