# app.py
import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

# Load the model (Hugging Face will cache this after first run)
model_id = "runwayml/stable-diffusion-v1-5"
# Increase the etag_timeout to allow more time for the initial connection to Hugging Face
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    safety_checker=None,  # Disable if you get NSFW filter errors
    etag_timeout=30 # Increase timeout to 30 seconds (default is 10)
).to("cuda")

def generate_image(prompt, negative_prompt="", steps=25, guidance=7.5, seed=None):
    # Set random seed if provided
    if seed is not None:
        torch.manual_seed(seed)

    # Generate the image
    # Removed torch.autocast("cuda") as it's generally not needed
    # with torch.autocast("cuda"):
    image = pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=int(steps),
        guidance_scale=guidance
    ).images[0]

    return image

# Create Gradio interface
with gr.Blocks(title="Stable Diffusion Image Generator") as demo:
    gr.Markdown("""# 🎨 Text-to-Image Generation
    Generate images using Stable Diffusion v1.5""")

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="Prompt", placeholder="A beautiful sunset over mountains...", lines=3)
            negative_prompt = gr.Textbox(label="Negative Prompt", placeholder="blurry, distorted, low quality...", lines=2)
            generate_btn = gr.Button("Generate", variant="primary")

            with gr.Accordion("Advanced Options", open=False):
                steps = gr.Slider(10, 50, value=25, step=1, label="Inference Steps")
                guidance = gr.Slider(1, 20, value=7.5, step=0.5, label="Guidance Scale")
                seed = gr.Number(label="Seed (leave blank for random)", precision=0)

        with gr.Column():
            output_image = gr.Image(label="Generated Image")

    # Example prompts
    gr.Examples(
        examples=[
            ["A cute corgi wearing a crown, 4k photo"],
            ["Cyberpunk cityscape at night, neon lights, rain-wet streets"],
            ["Watercolor painting of autumn forest"]
        ],
        inputs=prompt
    )

    generate_btn.click(
        fn=generate_image,
        inputs=[prompt, negative_prompt, steps, guidance, seed],
        outputs=output_image
    )

demo.launch()