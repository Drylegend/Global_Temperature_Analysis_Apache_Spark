import os
import json

input_folder = "gadm_states"
output_file = "world_states_merged.geojson"

merged = {
    "type": "FeatureCollection",
    "features": []
}

for file in os.listdir(input_folder):
    if file.endswith(".json"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            data = json.load(f)
            # Add all features from the file
            merged["features"].extend(data["features"])

print(f"Merged {len(merged['features'])} features.")

# Save merged file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(merged, f)

print(f"Saved merged file as: {output_file}")
