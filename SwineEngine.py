import os
import json
import random
from PIL import Image
from options import collection_name, description, layer_configurations, layers_paths, images_per_configuration, conflicts, resize_image_to, trait_size 

class SwineArtEngine:
    def __init__(self, layers_paths, build_path):
        self.layers_paths = layers_paths
        self.build_path = build_path

    def get_elements(self, layer):
        return [f for f in os.listdir(layer) if not f.startswith('.')]

    def get_layers_order(self, layer):
        return [f for f in os.listdir(layer) if os.path.isdir(os.path.join(layer, f))]

    def has_conflict(self, dna, layers_order):
        for index, trait_value in enumerate(dna):
            trait_conflicts = conflicts.get(trait_value, [])
            if any(conflict in dna for conflict in trait_conflicts):
                return True
        return False

    def generate_dna(self, layers_order, layer_path):
        retries = 50  # Number of retries if conflicts are found.
            
        while retries > 0:
            dna = []
            for layer in layers_order:
                element = random.choice(self.get_elements(os.path.join(layer_path, layer)))
                dna.append(element)
                
            if not self.has_conflict(dna, layers_order):
                return dna
            
            retries -= 1
            print(f"Retrying DNA generation. {retries} retries left.")
            
        print("Exceeded maximum retries for DNA generation due to conflicts.")
        return []

    def construct_image(self, dna, layers_order, layer_path):
        composite_image = Image.new("RGBA", trait_size)
        for index, layer_name in enumerate(layers_order):
            element_image = Image.open(os.path.join(layer_path, layer_name, dna[index]))
            composite_image = Image.alpha_composite(composite_image, element_image)
    
    # Resize the composite image
        composite_image = composite_image.resize(resize_image_to, Image.LANCZOS)     
        return composite_image

    def construct_metadata(self, dna, layers_order, edition):
        attributes = [{"trait_type": layers_order[i], "value": dna[i].replace('.PNG', '').split('#')[0]} for i in range(len(dna))]
        metadata = {
            "name": f"{collection_name} #{edition}",
            "description": description,
            "image": f"ipfs://NewUriToReplace/{edition}.png",
            "edition": edition,
            "attributes": attributes,
            "compiler": "CulturedSwine"
        }
        return metadata
    
    def save_metadata(self, metadata, edition):
        metadata_path = os.path.join(self.build_path, 'metadata', f"metadata_{edition}.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=4)

    def generate_art(self, configurations):
        total_images = sum(configurations.values())
        if total_images == configurations[layers_paths[0]]:
            edition_order = list(range(1, total_images + 1))
        else:
            edition_order = random.sample(range(1, total_images + 1), total_images)
        current_edition = 1

        for config, image_count in configurations.items():
            for _ in range(image_count):
                self.generate_single_image(config, edition_order[current_edition-1])
                current_edition += 1

    def generate_single_image(self, layer_path, edition):
        layer_order = self.get_layers_order(layer_path)
        dna = []
        for layer in layer_order:
            elements = self.get_elements(os.path.join(layer_path, layer))
            dna.append(random.choice(elements))
        composite_image = self.construct_image(dna, layer_order, layer_path)
        composite_image_path = os.path.join(self.build_path, 'images', f"{edition}.png")
        composite_image.save(composite_image_path)
        metadata = self.construct_metadata(dna, layer_order, edition)
        self.save_metadata(metadata, edition)

def compile_metadata(build_path):
    metadata_dir = os.path.join(build_path, 'metadata')
    compiled_data = []

    for file in os.listdir(metadata_dir):
        if file.endswith(".json") and file != "compiled_metadata.json":
            with open(os.path.join(metadata_dir, file), 'r') as f:
                data = json.load(f)
                compiled_data.append(data)

    with open(os.path.join(metadata_dir, "compiled_metadata.json"), 'w') as f:
        json.dump(compiled_data, f, indent=4)       

if __name__ == "__main__":
    BUILD_PATH = 'Build'
    
    # Ensure the images and metadata directories exist
    for sub_dir in ['images', 'metadata']:
        path = os.path.join(BUILD_PATH, sub_dir)
        if not os.path.exists(path):
            os.makedirs(path)
    
        # Clear out the contents of the subdirectories
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            os.unlink(file_path)

    configurations = {layer_path: images_count for layer_path, images_count in zip(layers_paths, images_per_configuration)}
    engine = SwineArtEngine(layers_paths, BUILD_PATH)
    engine.generate_art(configurations)
    compile_metadata(BUILD_PATH)
    
