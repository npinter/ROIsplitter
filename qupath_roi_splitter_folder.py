import geojson
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
import pandas as pd
import argparse


def draw_poly(input_df, input_img, col=(0, 0, 0), fill=False):
    s = np.array(input_df)
    if fill:
        output_img = cv2.fillPoly(input_img, pts=np.int32([s]), color=col)
    else:
        output_img = cv2.polylines(input_img, np.int32([s]), True, color=col, thickness=1)
    return output_img


def draw_roi(input_roi, input_img, fill):
    if len(input_roi["geometry"]["coordinates"]) == 1:
        # Polygon w/o holes
        input_img = draw_poly(input_roi["geometry"]["coordinates"][0], input_img, fill=fill)
    else:
        first_roi = True
        for sub_roi in input_roi["geometry"]["coordinates"]:
            # Polygon with holes
            if not isinstance(sub_roi[0][0], list):
                if first_roi:
                    first_roi = False
                    col = (0, 0, 0)
                else:
                    # holes in ROI
                    col = (255, 255, 255) if not fill else (0, 0, 0)
                input_img = draw_poly(sub_roi, input_img, col=col, fill=fill)
            else:
                # MultiPolygon with holes
                for sub_coord in sub_roi:
                    if first_roi:
                        first_roi = False
                        col = (0, 0, 0)
                    else:
                        # holes in ROI
                        col = (255, 255, 255) if not fill else (0, 0, 0)
                    input_img = draw_poly(sub_coord, input_img, col=col, fill=fill)

    return input_img


def split_qupath_roi_folder(roi_folder):
    geojson_files = [f for f in listdir(roi_folder) if isfile(join(roi_folder, f)) and f.endswith(".geojson")]

    for gj_f in geojson_files:
        with open(join(roi_folder, gj_f)) as file:
            geo_json = geojson.load(file)

        # HE dimensions
        dim_plt = [geo_json["dim"]["width"], geo_json["dim"]["height"]]

        tma_name = geo_json["name"]
        cell_types = [ct.rsplit(" - ", 1)[-1] for ct in geo_json["featureNames"]]

        for cell_type in cell_types:
            # Create numpy array with white background
            img = np.zeros((dim_plt[1], dim_plt[0], 3), dtype="uint8")
            img.fill(255)

            for i, roi in enumerate(geo_json["features"]):
                if not args.all:
                    if "classification" not in roi["properties"]:
                        continue
                    if roi["properties"]["classification"]["name"] == cell_type:
                        img = draw_roi(roi, img, args.fill)
                else:
                    img = draw_roi(roi, img, args.fill)

            # get all black pixel
            coords_arr = np.column_stack(np.where(img == (0, 0, 0)))

            # remove duplicated rows
            coords_arr_xy = coords_arr[coords_arr[:, 2] == 0]

            # remove last column
            coords_arr_xy = np.delete(coords_arr_xy, 2, axis=1)

            # to pandas and rename columns to x and y
            coords_df = pd.DataFrame(coords_arr_xy, columns=['y', 'x'])

            # reorder columns
            coords_df = coords_df[['x', 'y']]

            # drop duplicates
            coords_df = coords_df.drop_duplicates(
                subset=['x', 'y'],
                keep='last').reset_index(drop=True)

            coords_df.to_csv(join(roi_folder, "{}_{}.txt".format(tma_name, cell_type)), sep='\t', index=False)

            if args.img:
                cv2.imwrite(join(roi_folder, "{}_{}.png".format(tma_name, cell_type)), img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split ROI coordinates of QuPath TMA annotation by cell type (classfication) [FOLDER]")
    parser.add_argument("qupath_roi_folder", default=False, help="Input QuPath annotation folder (GeoJSON files)")
    parser.add_argument("--fill", action="store_true", required=False, help="Fill holes in ROI")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
    parser.add_argument("--all", action="store_true", required=False, help="Extracts all ROIs")
    parser.add_argument("--img", action="store_true", required=False, help="Generates image of ROIs")
    args = parser.parse_args()

    if args.qupath_roi_folder:
        split_qupath_roi_folder(args.qupath_roi_folder)
