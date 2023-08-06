import requests

def process_image(ngrok_url, img_url, output_filename):
    api_url = ngrok_url + "/process_image"
    payload = {"url": img_url, "output_filename": output_filename}

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        with open(output_filename + ".png", "wb") as f:
            f.write(response.content)
        print("Image processed successfully. Saved as", output_filename + ".png")
    else:
        print("Error processing image:", response.json().get("error"))
