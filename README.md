# Ad_Craft_AI

Welcome to our Ad Generator Application! This tool allows users to create visually stunning ads and captions by leveraging state-of-the-art machine learning models, including Stable Diffusion and LLaMA 3.1. Simply input a prompt, upload a starting image, and let the application do the rest!

## Features

- **User-Friendly Interface**: Intuitive front-end where users can type prompts and upload starting images.
- **AI-Powered Back End**: Utilizes cutting-edge models like Stable Diffusion for image generation and LLaMA 3.1 for caption creation.
- **Customizable Ads**: Generate unique ads tailored to your input.

## Installation and Setup

Follow these steps to set up the application locally:

1. **Download the Project Files**:
   - Download the zip file containing the project from the repository.
   - Extract the contents to a folder on your local machine.

2. **Install Dependencies**:
   - Open a terminal and navigate to the project folder.
   - Run the following command to install all required Node.js modules:
     ```bash
     npm install
     ```

3. **Prepare the Model Files**:
   - Download the `pytorch_model.bin` file from the public Google Drive link provided.
   - Move the downloaded file into the `Fooocus expansion` folder within the project directory.

4. **Run the Application**:
   - Start the application by running:
     ```bash
     npm start
     ```

   That’s it! The application is now up and running on your local machine.

## Usage Instructions

1. Launch the application from your terminal using `npm start`.
2. Access the application in your web browser (it will display the URL upon starting).
3. Use the front-end interface to:
   - Type your desired prompt.
   - Upload a starting image.
   - Click the generate button to create an ad and caption.

## Technical Details

### Front-End:
- Built with modern web development tools for a seamless user experience.

### Back-End:
- Implements advanced AI models:
  - **Stable Diffusion** for high-quality image generation.
  - **LLaMA 3.1** for intelligent captioning.

### File Structure:
- `Fooocus expansion`: Contains required model files, including the `pytorch_model.bin`.
- Front-end and back-end files are structured for easy navigation and modification.

## Troubleshooting

If you encounter any issues:
- Ensure that `pytorch_model.bin` is in the correct folder (`Fooocus expansion`).
- Check that all dependencies are installed (`npm install`).
- Verify your Node.js and npm versions (recommended: Node.js >= 16.x).

---

Thank you for using the Ad Generator Application! We’re excited to see the creative ads you generate.
