from transformers import pipeline

# Load the text generation pipeline from Hugging Face Transformers
generator = pipeline("text-generation")

def generate_restaurant_name_and_items(cuisine):
    prompt = f"Generate a restaurant name and menu items for a {cuisine} cuisine restaurant."
    generated_text = generator(prompt, max_length=50)[0]['generated_text']
    
    # Split the generated text into restaurant name and menu items
    parts = generated_text.split(':', 1)
    if len(parts) > 1:
        restaurant_name, menu_items = parts
        return {
            'restaurant_name': restaurant_name.strip(),
            'menu_items': [item.strip() for item in menu_items.strip().split(",")]
        }
    else:
        return {
            'restaurant_name': "Failed to generate",
            'menu_items': ["Failed to generate"]
        }
