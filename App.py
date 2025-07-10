import gradio as gr

def greet(name):
    return f"خوش آمدید، {name}!"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="MalikAI Urdu Video Generator"
)

demo.launch()
