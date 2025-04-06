cwlVersion: v1.2
class: CommandLineTool
 
hints:
  DockerRequirement:
    dockerPull: "eforoutan/clip_shp:latest"
  NetworkAccess:
    networkAccess: true
 
inputs:
  input_shapefile:
    type:
      - File
      - Directory
    inputBinding:
      position: 1
 
  clip_shapefile:
    type:
      - File
      - Directory
    inputBinding:
      position: 2

outputs:

  clipped_GeoJSON:
    type: File  
    outputBinding:
      glob: "clipped_shapefile.geojson"
