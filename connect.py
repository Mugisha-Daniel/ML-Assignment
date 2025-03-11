import gradio as gr
import requests

def predict_price(num_rooms, area):
    url = "http://127.0.0.1:5000/predict"
    data = {"num_rooms": num_rooms, "area": area}
    response = requests.post(url, json=data)
    return response.json().get("predicted_price", "Error in prediction")

with gr.Blocks() as demo:
    gr.Markdown("# 🏠 House Price Prediction")
    num_rooms = gr.Dropdown(choices=list(range(1, 10)), value=1, label="Select Number of Rooms")
    area = gr.Number(label="Enter Area (in square meters)")
    predict_button = gr.Button("Predict")
    output = gr.Textbox(label="Predicted Price")
    predict_button.click(predict_price, inputs=[num_rooms, area], outputs=output)

demo.launch()
