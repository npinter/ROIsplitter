[![European Galaxy server](https://img.shields.io/badge/usegalaxy-.eu-brightgreen?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAASCAYAAABB7B6eAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAACC2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOlJlc29sdXRpb25Vbml0PjI8L3RpZmY6UmVzb2x1dGlvblVuaXQ+CiAgICAgICAgIDx0aWZmOkNvbXByZXNzaW9uPjE8L3RpZmY6Q29tcHJlc3Npb24+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24+MjwvdGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KD0UqkwAAAn9JREFUOBGlVEuLE0EQruqZiftwDz4QYT1IYM8eFkHFw/4HYX+GB3/B4l/YP+CP8OBNTwpCwFMQXAQPKtnsg5nJZpKdni6/6kzHvAYDFtRUT71f3UwAEbkLch9ogQxcBwRKMfAnM1/CBwgrbxkgPAYqlBOy1jfovlaPsEiWPROZmqmZKKzOYCJb/AbdYLso9/9B6GppBRqCrjSYYaquZq20EUKAzVpjo1FzWRDVrNay6C/HDxT92wXrAVCH3ASqq5VqEtv1WZ13Mdwf8LFyyKECNbgHHAObWhScf4Wnj9CbQpPzWYU3UFoX3qkhlG8AY2BTQt5/EA7qaEPQsgGLWied0A8VKrHAsCC1eJ6EFoUd1v6GoPOaRAtDPViUr/wPzkIFV9AaAZGtYB568VyJfijV+ZBzlVZJ3W7XHB2RESGe4opXIGzRTdjcAupOK09RA6kzr1NTrTj7V1ugM4VgPGWEw+e39CxO6JUw5XhhKihmaDacU2GiR0Ohcc4cZ+Kq3AjlEnEeRSazLs6/9b/kh4eTC+hngE3QQD7Yyclxsrf3cpxsPXn+cFdenF9aqlBXMXaDiEyfyfawBz2RqC/O9WF1ysacOpytlUSoqNrtfbS642+4D4CS9V3xb4u8P/ACI4O810efRu6KsC0QnjHJGaq4IOGUjWTo/YDZDB3xSIxcGyNlWcTucb4T3in/3IaueNrZyX0lGOrWndstOr+w21UlVFokILjJLFhPukbVY8OmwNQ3nZgNJNmKDccusSb4UIe+gtkI+9/bSLJDjqn763f5CQ5TLApmICkqwR0QnUPKZFIUnoozWcQuRbC0Km02knj0tPYx63furGs3x/iPnz83zJDVNtdP3QAAAABJRU5ErkJggg==)](https://usegalaxy.eu/root?tool_id=qupath_roi_splitter)

# QuPath Annotation Exporter and ROI Splitter

This repository contains a set of scripts to export QuPath annotations as GeoJSON and split the exported ROI coordinates by cell type (classification) for further analysis.

v0.2.0

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

1. Run `qupath_roi_splitter.py` with the `--qupath_roi` argument pointing to the GeoJSON file you want to process. `--fill` is an optional argument to fill the ROI polygons. `--all` is an optional argument to export all features of GeoJSON (ignores if classification is present).

```bash
python qupath_roi_splitter.py --qupath_roi path/to/your/geojson_file.geojson --fill
```

#### For multiple GeoJSON files in a folder

1. Run `qupath_roi_splitter_folder.py` with the `qupath_roi_folder` argument pointing to the folder containing the GeoJSON files you want to process.

```bash
python qupath_roi_splitter_folder.py path/to/your/geojson_folder --fill
```

The script will create a tab-separated text file for each cell type (classification) in the same folder as the GeoJSON files. The text files will be named as follows: `[TMA_name]_[cell_type].txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.