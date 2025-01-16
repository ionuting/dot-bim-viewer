# Import required Flask modules and utilities
from flask import Flask, render_template, send_from_directory, jsonify
import os

# Initialize Flask application
app = Flask(__name__)

# Configure models folder setup
# This folder will store all JSON model files
MODELS_FOLDER = os.path.join(app.static_folder, 'models')
if not os.path.exists(MODELS_FOLDER):
    os.makedirs(MODELS_FOLDER)

@app.route('/')
def index():
    """
    Main route handler for the application.
    Lists all JSON model files from the models folder and renders the viewer template.
    
    Returns:
        rendered template: viewer.html with list of available models
    """
    # Get all JSON files from the models directory
    models = [f for f in os.listdir(MODELS_FOLDER) if f.endswith('.json')]
    return render_template('viewer.html', models=models)

@app.route('/models/<path:filename>')
def serve_model(filename):
    """
    Route handler for serving model files.
    Provides secure access to model files stored in the models folder.
    
    Args:
        filename (str): Name of the model file to serve
        
    Returns:
        file: The requested model file
    """
    return send_from_directory(MODELS_FOLDER, filename)

@app.route('/csv-viewer')
def csv_viewer():
    """
    Route handler for the CSV viewer page.
    Renders a simplified CSV viewer template.
    
    Returns:
        rendered template: csv-viewer-simple.html
    """
    return render_template('csv-viewer-simple.html')

# Run the application in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)