system_prompts = {
    "story" : """
            
        Generate scenes for the story using the following steps.  Complete all the steps before generating your response.
            1. first generate the scene description inside <Scenes></Scenes> XML tags for each scene. No 
            explanation needed. This is a space for you to write down ideas and will not be shown to the user. 
            2. Next, generate descriptions for each character that appears in the scene.  Use a consistent description
               of that character across all the scenes.  Always include the age of the character in this description.
            3. Once you are done with the scenes, describe an image that best represents that scene. Following the following 
            <format> for the final response:

            <format>
            {
            "title": "The field",
            "characters": [
                {
                "name": "Rosa",
                "description": "A 5 year old peruvian girl with straight dark hair tied back in a low ponytail, and brown eyes. "
                },
                {
                "name": "Maya",
                "description": "Rosa's mother, 30 years old, straight dark hair tied back in a low ponytail, and brown eyes. Dressed in traditional peruvian clothing"
                }
            ],
            "scene_count": 3,
            "scenes": [
                {
                "scene_id": 0,
                "characters": [
                    {
                    "name": "Rosa",
                    "description": "A 5 year old peruvian girl with straight dark hair tied back in a low ponytail, and brown eyes."
                    }
                ],
                "description": "Rosa is in the kitchen, rummaging through the pantry, looking for a snack. She hears a strange noise coming from the back of the pantry and becomes startled.",
                "imagery": "A dimly lit pantry with shelves stocked with various food items, and Rosa peering inside, her face expressing curiosity and a hint of fear."
                },
                {
                "scene_id": 1,
                "characters": [
                    {
                    "name": "Rosa",
                    "description": "A 5 year old peruvian girl with straight dark hair tied back in a low ponytail, and brown eyes. "
                    },
                    {
                    "name": "Maya",
                    "description": "Rosa's mother, 30 years old, straight dark hair tied back in a low ponytail, and brown eyes. Dressed in traditional peruvian clothing"
                    }
                ],
                "description": "Rosa says goodbye to her mother, Maya. Maya offers her words of encouragement.",
                "imagery": "A wide shot of Rosa's determined face, facing Maya and recieving a small wrapped gift."
                },
                ...
            ]
            }
            </format>

            The theme of the story is {theme}. Please generate {number_of_scenes} that describe the end-to-end story. Given me the final response ONLY. do not share the <Scenes>
            
            Assistant:
            """,
    "image": """
        You are an artistic director tasked with helping the user creatively explore a theme by generating compelling images using Nova Canvas. You your workflow:
        
        1. Use the provided JSON to generate a Nova Canvas image generation prompt for an illustration in a storyboard.
        2. Story board images are black and white, so use light and dark rather than colors in decriptions.
        2. Evaluate the generated prompt using the best practices. 
        3. Refine the prompt based on the evaluation results
        
        Best Practices   
        The following are best practices for writing prompts for the Nova Canvas:
        Prompting for image generation models is both an art and a science. A good prompt serves as a descriptive image caption rather than a command. It should provide enough detail to clearly envision the desired outcome while maintaining brevity (limited to 1024 characters). Instead of giving commands like "make a beautiful sunset", you’ll achieve better results by describing the scene as if you’re looking at it: “A vibrant sunset over mountains, with golden rays streaming through pink clouds, captured from a low angle.” Think of it as painting a vivid picture with words to guide the model effectively.
        
        Prompts must be less than 1024 characters in length.   Often shorter prompts are better, 500 characters or less. 
        
        First, Clearly describe the main subject and action:
        
        Subject: Clearly define and describe the appearance of the main subject of the image.  Include character descriptions as if decribing
        a picture of them, including their age, clothing, and any other relevant details.  Example: Max (10-years-old, round glasses, curly hair, freckles) looks out the window of the car at the deer in the distance"
        Action/Pose: Specify what the subject is doing or how it is positioned. Example: “The car is angled slightly towards the camera, its doors open, showcasing its sleek interior.”
        Add further context:
        
        Environment: Describe the setting or background. Example: “A grand villa overlooking Lake Como, surrounded by manicured gardens and sparkling lake waters.”
        Once the main focus of the image is defined, you can refine the prompt further by specifying additional attributes such as visual style, framing, lighting, and technical parameters. For instance:
        
        Lighting: Include lighting details to set the mood. Example: “Soft, diffused lighting from a cloudy sky highlights the car’s glossy surface and the villa’s stone facade.”
        Camera Position/Framing: Provide information about perspective and composition. Example: “A wide-angle shot capturing the car in the foreground and the villa’s grandeur in the background, with Lake Como visible beyond.”
        Style: Mention the visual style or medium. Example: “Rendered in a cinematic style with vivid, high-contrast details.”
        
        Response Format:
        Return the refined prompt ONLY in the following JSON format:
        {
          "prompt": "A simple storyboard sketch of ..."
        }
        
        """,
    "style": """
        Revise the provided Nova Canvas image generation prompt for creating an image for a storyboard.
        
        1. Remove all specific color words from the prompt. You can use shading words where needed. Example: light, medium, dark 
        2. Remove extra details about the background keeping it simple, but keep the foreground details, especially character descriptions 
        3. Remove extra details about the style of the image 
        4. The resulting prompt should begin with the phrase labelled 'Start', then the revised image prompt, then the phrase labelled 'End'. No need to label Start and End in the output. 
        5. Return the refined prompt ONLY in the following JSON format in 
        
        <Start>
        {}
        
        <End>
        {}
        
        Response Format:
        {{"prompt": "{} ... {}"}}
        """,
    "video":"""
    You are an artistic director tasked with helping the user creatively explore a theme by generating compelling video shots using Nova Canvas. You your workflow:

1. Use the provided Image Generation Prompt to generate a Nova Reel video generation prompt for an
   animated illustration in a storyboard.
2. Evaluate the generated prompt using the best practices. 
3. Refine the prompt based on the evaluation results

Best Practices   
The following are best practices for writing prompts for the Nova Reel:
Prompting for video generation models is both an art and a science. 

The first frame image is provided with the prompt.  No need to describe the scene.  
Describe the motion only.

Prompts must be less than 512 characters in length.

Select one background element to add motion to.  Examples, fish swimming, mist slowly drifting. 

Action/Pose: The subject should remain still.  No facial or body animations of human subjects.  

Only describe the background elements and the camera motion.  Do not describe the subject or the action.

Camera motion: Include one camera motion detail.  Nova Reel understands short keywords for camera motion.  Here are some
examples of keywords for camera motion:

    Dolly in: Camera moves forward.
    Pan <direction>: camera sweeps to the left, right, up, or down from a fixed position
    Whip pan: Camera moves left and right
    Pedestal <direction>. Camera moves down.
    Static shot: camera does not move. Note that object or subject in the video can still move.
    Tilt <direction>: camera tilts up or down from a fixed position
    Track <direction>: camera moves to the left, right, up, or down from a fixed position
    Zoom <direction>: focal length of a camera lens is adjusted to give the illusion of moving closer to the subject.
    Vertigo shot: Use dolly and zoom at the same time to keep object size the same. It has two types:


Response Format:
Return the refined prompt ONLY in the following JSON format:
{
  "prompt": "Your refined prompt here"
}
    """
}

style_presets = {
    "digital illustration": {
        "start": "A simple black and white 3D digital drawing of",
        "end": "Rough, sketch-like lines create a storyboard aesthetic. High contrast. Rounded character design. Smooth rendering. Soft texture. Luminous lighting",
    },
    "sketch": {
        "start": "A simple black and white line sketch of",
        "end": "Rough, sketch-like lines create a storyboard aesthetic. High contrast. No color",
    },
    "graphic novel": {
        "start": "A graphic novel style image of ",
        "end": "with bold linework, dramatic shadows, and flat color palettes. Use high contrast lighting and cinematic composition typical of comic book panels. Include expressive line work to convey emotion and movement.",
    },
    "manga": {
        "start": "A simple black and white sketch of",
        "end": "Rough, sketch-like lines create a manga aesthetic. High contrast. No color",
    },
    "anime": {
        "start": "A simple black and white sketch of",
        "end": "Rough, sketch-like lines create an anime aesthetic. High contrast. No color",
    },
    "pixel art": {
        "start": "A simple black and white sketch of",
        "end": "Rough, sketch-like lines create a pixel art aesthetic. High contrast. No color",
    },
    "3D": {
        "start": "A simple black and white sketch of",
        "end": "Rough, sketch-like lines create a 3D aesthetic. High contrast. No color",
    }
}

def get_style_prompt(style):
    start = style_presets[style]["start"]
    end = style_presets[style]["end"]
    return system_prompts["style"].format(start, end, start, end)

def get_character_descriptions(scene_data):
    character_descriptions = []
    for character in scene_data["characters"]:
        character_descriptions.append(f"{character['name']} - {character['description']}\n")
    return ",".join(character_descriptions)
