
from IPython.display import HTML, display
import json

def display_story_table(story_data):
    """
    Create a nicely formatted HTML table to display story information.
    
    Parameters:
    -----------
    story_data : dict
        Dictionary containing story data with title, characters, and scenes
    """
    # CSS for styling the table
    css = """
    <style>
    .story-table {
        font-family: Arial, sans-serif !important;
        border-collapse: collapse !important;
        width: 100% !important;
        margin-bottom: 20px !important;
        color: black !important;
        text-align: left !important;
    }
    .story-table th, 
    .story-table td {
        border: 1px solid #ddd !important;
        padding: 12px !important;
        vertical-align: top !important;
        text-align: left !important;
    }
    .story-table th {
        background-color: #36454F !important;
        color: white !important;
        font-size: 16px !important;
        text-align: left !important;
    }
    .story-table tr:nth-child(even) {
        background-color: #f2f2f2 !important;
        text-align: left !important;
    }
    .story-table tr:hover {
        background-color: #ddd !important;
        text-align: left !important;
    }
    .title-section {
        font-size: 22px !important;
        font-weight: bold !important;
        margin: 15px 0 !important;
        color: #333 !important;
        text-align: left !important;
        background-color: #e6f2ff !important;
        padding: 10px !important;
        border-left: 5px solid #0066cc !important;
    }
    .section-title {
        font-size: 20px !important;
        font-weight: bold !important;
        margin: 15px 0 !important;
        color: #333 !important;
        text-align: left !important;
        border-bottom: 2px solid #36454F !important;
        padding-bottom: 5px !important;
    }
    .character-name {
        font-weight: bold !important;
        color: #0066cc !important;
        text-align: left !important;
    }
    .scene-id {
        font-weight: bold !important;
        color: #0066cc !important;
        text-align: left !important;
    }
    .name-column {
        width: 100px !important;  /* Reduced width for character name column */
    }
    /* Direct attribute to force text alignment */
    [data-align="left"] {
        text-align: left !important;
    }
    </style>
    """
    
    # Create the title section
    html_content = css
    html_content += f'<div class="title-section" data-align="left">Title: {story_data["title"]}</div>'
    
    # Create the characters section
    html_content += '<div class="section-title" data-align="left">Characters:</div>'
    html_content += '<table class="story-table">'
    html_content += '<tr><th class="name-column" data-align="left">Name</th><th data-align="left">Description</th></tr>'
    
    for character in story_data['characters']:
        html_content += f'<tr>'
        html_content += f'<td class="character-name name-column" data-align="left">{character["name"]}</td>'
        html_content += f'<td data-align="left">{character["description"]}</td>'
        html_content += '</tr>'
    
    html_content += '</table>'
    
    # Create the scenes section
    html_content += '<div class="section-title" data-align="left">Scenes:</div>'
    html_content += '<table class="story-table">'
    html_content += '<tr><th data-align="left">Scene</th><th data-align="left">Description</th><th data-align="left">Imagery</th><th data-align="left">Characters Present</th></tr>'
    
    for scene in story_data['scenes']:
        html_content += '<tr>'
        html_content += f'<td class="scene-id" data-align="left">Scene {scene["scene_id"] + 1}</td>'
        html_content += f'<td data-align="left">{scene["description"]}</td>'
        html_content += f'<td data-align="left">{scene["imagery"]}</td>'
        
        # Create a comma-separated list of character names
        character_names = [char["name"] for char in scene['characters']]
        characters_text = ", ".join(character_names)
        
        html_content += f'<td data-align="left">{characters_text}</td>'
        html_content += '</tr>'
    
    html_content += '</table>'
    
    # Display the HTML
    display(HTML(html_content))

def display_prompt_table(story_data, image_prompts):
    """
    Create a nicely formatted HTML table to display story information.
    
    Parameters:
    -----------
    story_data : dict
        Dictionary containing story data with title, characters, and scenes
    """
    # CSS for styling the table
    css = """
    <style>
    .story-table {
        font-family: Arial, sans-serif !important;
        border-collapse: collapse !important;
        width: 100% !important;
        margin-bottom: 20px !important;
        color: black !important;
        text-align: left !important;
    }
    .story-table th, 
    .story-table td {
        border: 1px solid #ddd !important;
        padding: 12px !important;
        vertical-align: top !important;
        text-align: left !important;
    }
    .story-table th {
        background-color: #36454F !important;
        color: white !important;
        font-size: 16px !important;
        text-align: left !important;
    }
    .story-table tr:nth-child(even) {
        background-color: #f2f2f2 !important;
        text-align: left !important;
    }
    .story-table tr:hover {
        background-color: #ddd !important;
        text-align: left !important;
    }
    .title-section {
        font-size: 22px !important;
        font-weight: bold !important;
        margin: 15px 0 !important;
        color: #333 !important;
        text-align: left !important;
        background-color: #e6f2ff !important;
        padding: 10px !important;
        border-left: 5px solid #0066cc !important;
    }
    .section-title {
        font-size: 20px !important;
        font-weight: bold !important;
        margin: 15px 0 !important;
        color: #333 !important;
        text-align: left !important;
        border-bottom: 2px solid #36454F !important;
        padding-bottom: 5px !important;
    }
    .character-name {
        font-weight: bold !important;
        color: #0066cc !important;
        text-align: left !important;
    }
    .scene-id {
        font-weight: bold !important;
        color: #0066cc !important;
        text-align: left !important;
    }
    .name-column {
        width: 100px !important;  /* Reduced width for character name column */
    }
    /* Direct attribute to force text alignment */
    [data-align="left"] {
        text-align: left !important;
    }
    </style>
    """
    
    # Create the title section
    html_content = css
    
    # Create the characters section
    html_content += '<table class="story-table">'
    html_content += '<tr><th data-align="left">Scene Imagery From Script</th><th data-align="left">Image Prompt</th></tr>'
    
    for scene in story_data['scenes']:
        html_content += f'<tr>'
        html_content += f'<td data-align="left">{scene["imagery"]}</td>'
        html_content += f'<td data-align="left">{image_prompts[scene["scene_id"]]}</td>'
        html_content += '</tr>'
    
    html_content += '</table>'
    
    
    # Display the HTML
    display(HTML(html_content))

def display_images_in_row(image_data, caption=None, width=300):
    """
    Display a list of images in a single row with an optional description column.
    
    Parameters:
    -----------
    image_bytes_list : list
        List of image byte arrays (already decoded from base64)
    caption : str, optional
        Long description to display in the last column
    width : int, optional
        Width of the displayed images in pixels
    """
    # Start building HTML table with CSS for the wider description column
    html = """
    <style>
    .image-table td.description {
        width: 300px;
        max-width: 300px;
        word-wrap: break-word;
        padding: 10px;
        vertical-align: top;
        text-align: left;
    }
    .image-table td.image {
        padding: 5px;
        text-align: center;
        vertical-align: middle;
    }
    </style>
    <table class="image-table">
    <tr>
    """
    
    # Add each image cell
    for b64_str in image_data:
        # b64_str = base64.b64encode(img_bytes).decode('utf-8')
        
        # # Detect image type (assuming JPEG or PNG)
        # if img_bytes.startswith(b'\xff\xd8'):
        #     mime = 'image/jpeg'
        # else:
        mime = 'image/png'  # Default to PNG
        
        # Create HTML img tag
        img_html = f'<img src="data:{mime};base64,{b64_str}" width="{width}px"/>'
        
        # Add cell to row
        html += f'<td class="image">{img_html}</td>'
    
    # Add the description column (last column)
    if caption:
        html += f'<td class="description">{caption}</td>'
    
    # Close the row and table
    html += "</tr></table>"
    
    # Display the HTML
    display(HTML(html))

def display_storyboard(image_data, story):
    for scene in story.get("scenes"):
        scene_id = scene["scene_id"]
        display_images_in_row(image_data[scene_id], caption=story["scenes"][scene_id]["description"])