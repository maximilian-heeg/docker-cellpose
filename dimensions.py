#! /usr/bin/env/ python
import tifffile

tif = tifffile.TiffFile('data/morphology_mip.ome.tif')
page = tif.pages[0]  # get shape and dtype of image in first page
pixel = page.shape[0] * page.shape[1]
bytes = pixel * 16
tif.close()