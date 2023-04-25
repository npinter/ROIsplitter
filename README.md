# QuPath Annotation Exporter and ROI Splitter

This repository contains a set of scripts to export QuPath annotations as GeoJSON and split the exported ROI coordinates by cell type (classification) for further analysis.

## Scripts

1. `ExAnnoClassifications.groovy`: A Groovy script for QuPath to extract cell detection-based annotations (classifications) from QuPath TMA projects and save them as GeoJSON files.
2. `qupath_roi_splitter.py`: A Python script to split the ROI coordinates of QuPath TMA annotations by cell type (classification) and save them as tab-separated text files.
3. `qupath_roi_splitter_folder.py`: A folder version of the `qupath_roi_splitter.py` script that processes all GeoJSON files in a specified folder.

## Requirements

- QuPath (for `ExAnnoClassifications.groovy`)
- Python 3.6 or later
- OpenCV (cv2)
- GeoJSON
- Pandas
- NumPy

## Usage

### 1. Export annotations from QuPath

1. Open QuPath and load your TMA project.
2. In QuPath, go to `Automate > Show script editor`.
3. Copy the content of the `ExAnnoClassifications.groovy` script into the script editor.
4. Run the script. It will save the exported annotations as GeoJSON files in a folder named `annotations_export_[TMA_name]` within your QuPath project directory.

### 2. Split ROI coordinates by cell type (classification)

#### For single GeoJSON file

1. Run `qupath_roi_splitter.py` with the `--qupath_roi` argument pointing to the GeoJSON file you want to process.

```bash
python qupath_roi_splitter.py --qupath_roi path/to/your/geojson_file.geojson
```

#### For multiple GeoJSON files in a folder

1. Run `qupath_roi_splitter_folder.py` with the `qupath_roi_folder` argument pointing to the folder containing the GeoJSON files you want to process.

```bash
python qupath_roi_splitter_folder.py path/to/your/geojson_folder
```

The script will create a tab-separated text file for each cell type (classification) in the same folder as the GeoJSON files. The text files will be named as follows: `[TMA_name]_[cell_type].txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.