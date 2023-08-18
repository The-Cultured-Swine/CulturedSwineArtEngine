
# Be sure to replace this with your own
collection_name = "MyArtCollection"

# Default description for the generated images
description = "Remember to replace this description"

layers_paths = ['layers', 'layers2']  # Paths to layer folders, you can add more as needed.
build_path = "build"
layer_configurations = [
    ["Background", "Body", "Clothing", "Eyes", "Head", "Mouth", "Weapon"],  # Layers order for first configuration
    ["Background", "Body", "Clothing", "Eyes", "Head", "Mouth", "Weapon"]   # Layers order for second configuration
    # Change these to match your projects layer folder names
]

#check you layers and ensure they are all the same size and enter the width and height here.
trait_size = (2701, 2701)

#If you'd like the generated art to be a different size than the original trait size
resize_image_to = (1512, 1512)

#these are the width and height in px, if you want to change the generated size from the 

# Number of images to generate for each layer configuration
images_per_configuration = [
    55,  # For the first configuration
    1,  # For the second configuration
    # Add counts for more configurations if required

#update IPFS

]
conflicts = {
    "Red Blindfold": ["Army Beanie", "Peace Love Nutz"],
    "Rubber Chicken": ["Branch"],
    "Battle Band": ["Goggles", "Digital Goggles"],
    "Gold Vipers": ["Storm Helmet", "Desert Helmet", "Battle Band", "Gold Viking Helmet", "Viking Helmet", "Black Cowboy Hat", "Cowboy Hat"],
    "Blindfold": ["Army Beanie", "Peace Love Nutz"],
    "Vipers": ["Storm Helmet", "Desert Helmet", "Battle Band", "Gold Viking Helmet", "Viking Helmet", "Black Cowboy Hat", "Cowboy Hat"],
    "VR": ["Jungle Helmet", "Storm Helmet", "Desert Helmet", "Army Beanie", "Peace Love Nutz", "Battle Band", "Black Cowboy Hat", "Cowboy Hat", "Battle Band"],
    "Lazers": ["Cigar", "Blue Lightsaber", "Lightsaber"]
}
