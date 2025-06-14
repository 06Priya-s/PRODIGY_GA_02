# PRODIGY_GA_02
# Stable Diffusion Image Generator
    
  <p>A Gradio web interface for generating images using Stable Diffusion v1.5 model from Hugging Face.</p>
    
  <h2>✨ Features</h2>
    <ul>
        <li>Text-to-image generation with Stable Diffusion v1.5</li>
        <li>Customizable parameters (steps, guidance scale, seed)</li>
        <li>Negative prompt support to exclude unwanted elements</li>
        <li>Example prompts for quick testing</li>
        <li>Responsive web interface</li>
    </ul>
    
   <h2>🚀 Getting Started</h2>
    
  <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7+</li>
        <li>NVIDIA GPU with CUDA support (recommended)</li>
        <li>PyTorch with CUDA</li>
    </ul>
    
  <h3>Installation</h3>
    <ol>
        <li>Clone this repository</li>
        <li>Install the required packages:</li>
    </ol>
    <pre><code>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install diffusers transformers gradio</code></pre>
    
  <h3>Running the Application</h3>
    <p> Please copy the above code in a google colab notebook to run </p>
    
  <h2>⚙️ Configuration</h2>
    <p>The application uses the following default settings:</p>
    <ul>
        <li><strong>Model:</strong> runwayml/stable-diffusion-v1-5</li>
        <li><strong>Inference Steps:</strong> 25</li>
        <li><strong>Guidance Scale:</strong> 7.5</li>
        <li><strong>Image Size:</strong> 512x512 (default for Stable Diffusion)</li>
    </ul>
    
   <p>
        <strong>Note:</strong> The first run will download the Stable Diffusion model (several GB) from Hugging Face. 
        Subsequent runs will use the cached version.
    </p>
    
  <h2>🖌️ Usage</h2>
    <ol>
        <li>Enter your prompt in the text box</li>
        <li>(Optional) Add negative prompts to exclude unwanted elements</li>
        <li>(Optional) Adjust advanced parameters:
            <ul>
                <li><strong>Inference Steps:</strong> Higher values may improve quality but take longer (10-50)</li>
                <li><strong>Guidance Scale:</strong> Controls how closely the image follows the prompt (1-20)</li>
                <li><strong>Seed:</strong> For reproducible results (leave blank for random)</li>
            </ul>
        </li>
        <li>Click "Generate"</li>
    </ol>
    
    
  <h2>📚 Example Prompts</h2>
    <ul>
        <li>"A cute corgi wearing a crown, 4k photo"</li>
        <li>"Cyberpunk cityscape at night, neon lights, rain-wet streets"</li>
        <li>"Watercolor painting of autumn forest"</li>
    </ul>
    
   <h2>⚠️ Limitations</h2>
    <ul>
        <li>Requires significant GPU memory (at least 8GB recommended)</li>
        <li>Image generation may take 10-30 seconds depending on hardware</li>
        <li>NSFW filter is disabled by default in this implementation</li>
    </ul>

 
