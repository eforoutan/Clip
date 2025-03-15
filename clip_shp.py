import sys
import os
import json
import geopandas as gpd

def clip_shp(input_shapefile, clip_shapefile):
    try:
        # Read the input shapefile and clip shapefile
        gdf_input = gpd.read_file(input_shapefile)
        gdf_clip = gpd.read_file(clip_shapefile)

        # Perform the clip operation
        gdf_clipped = gpd.overlay(gdf_input, gdf_clip, how='intersection')

        # Construct output file names in the current directory
        output_shapefile = os.path.join(os.getcwd(), "clipped_shapefile.shp")
        output_geojson = os.path.join(os.getcwd(), "clipped_shapefile.geojson")

        # Save the clipped shapefile
        gdf_clipped.to_file(output_shapefile)

        # Save the clipped GeoJSON
        gdf_clipped.to_file(output_geojson, driver='GeoJSON')

        return output_shapefile, output_geojson  # Return the paths to the output files

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None  # Indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clip_shapefile.py <input_shapefile> <clip_shapefile>")
        sys.exit(1)

    input_shapefile = sys.argv[1]
    clip_shapefile = sys.argv[2]

    output_shapefile, output_geojson = clip_shp(input_shapefile, clip_shapefile)


    if output_shapefile and output_geojson:
        print(f"Shapefile successfully clipped and saved as {output_shapefile}.")
        print(f"GeoJSON successfully clipped and saved as {output_geojson}.")
    else:
        print(json.dumps({"error": "Clipping failed"}))
