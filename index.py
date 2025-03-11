import gradio as gr
from joblib import load
import numpy as np

model = load("house_model.pkl")

def predict_price(num_rooms, area):
    features = np.array([[area, num_rooms]])  
    prediction = model.predict(features)[0][0] * 1_000_000 
    return f"Predicted Price: {prediction:,.0f} Rwf"

with gr.Blocks(css="""
    body { background-color: #001f00; color: #00ff00; text-align: center; }
    .gradio-container { font-family: Arial, sans-serif; }
    .gr-button { background-color: #004d00; color: cyan; border-radius: 10px; }
    .gr-button:hover { background-color: #008000; }
    .gr-textbox, .gr-dropdown, .gr-number { border: 2px solid #00ff00; }
""") as demo:
    with gr.Column():
        gr.Markdown("# 🏠 House Price Prediction", elem_id="title")
        num_rooms = gr.Dropdown(choices=list(range(1, 10)), value=1, label="Select Number of Rooms")
        area = gr.Number(label="Enter Area (in square meters)")
        predict_button = gr.Button("Predict")
        output = gr.Textbox(label="Predicted Price")
        
        predict_button.click(predict_price, inputs=[num_rooms, area], outputs=output)

demo.launch()
