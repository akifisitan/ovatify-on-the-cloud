import functions_framework
from flask import make_response, jsonify
import os
from google.cloud import vision
from PIL import Image
import io
from google.cloud.vision_v1 import types
import base64

@functions_framework.http
def compress_and_check_image(request):
    # Ensure correct method
    if request.method != 'POST':
        return jsonify({"error": "Only POST method is accepted"}), 405

    # Ensure there is a file in the request
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    if not file.filename.lower().split('.')[-1] in allowed_extensions:
        return jsonify({"error": "File format not supported. Only JPG, JPEG, PNG, and GIF are allowed"}), 400

    try:
        # Process the image
        image = Image.open(file.stream)
        max_size = (500, 500)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG', quality=20)
        img_byte_arr.seek(0)
        
        # Perform safe search detection
        safe_search_result = detect_safe_search(img_byte_arr.getvalue())
        if safe_search_result["flagged"]:
            return 'Image contains inappropriate content.', 400

        base64_encoded_image = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
        # Return JSON response
        return jsonify({"image": base64_encoded_image}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def detect_safe_search(content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.safe_search_detection(image=image)
    safesearch = response.safe_search_annotation

    if response.error.message:
        raise Exception(response.error.message)

    # Define flagged conditions
    if (safesearch.violence.name in ['POSSIBLE', 'LIKELY', 'VERY_LIKELY'] or
        safesearch.racy.name in ['POSSIBLE', 'LIKELY', 'VERY_LIKELY'] or
        safesearch.adult.name in ['POSSIBLE', 'LIKELY', 'VERY_LIKELY']):
        return {"flagged": True}
    
    return {"flagged": False}