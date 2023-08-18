# CulturedSwineArtEngine
A very compact Art Engine to create NFTs
The engine will begin generating unique images based on the configurations provided. It will retry generating images if they contain any conflicting elements.
Generated images and their metadata will be saved in the Build directory.
Configuration (options.py)
collection_name: The name of your art collection.
description: A default description for the generated images.
layers_paths: Paths to directories containing different layer configurations.
build_path: Path to the output directory.
layer_configurations: Order of layers for each configuration.
images_per_configuration: Number of images to generate for each configuration.
resize_image_to: Desired output size for the generated images.
conflicts: A dictionary of elements that should not appear together in the generated images.
Notes
Ensure that image components for each layer are of the same size.
If any conflicts are detected during image generation, the engine will retry until a valid combination is found or until it exceeds the maximum number of retries.
