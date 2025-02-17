from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_crop_mask = {"mask": [], "prob": [], "filtered": []}


# old style
style_crop_mask_magma = {
    "name": "magma",
    "title": "PROB",
    "abstract": "Prob band Magma",
    "needed_bands": ["prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "prob",
        },
    },
    "mpl_ramp": "magma",
    "range": [50, 100],
    "legend": {
        "begin": "50",
        "end": "100",
        "ticks_every": "10",
        "tick_labels": {
            "50": {"prefix": "<"},
        },
    },
}

style_crop_mask_prob = {
    "name": "prob",
    "title": "Crop probability",
    "abstract": "Crop probability",
    "needed_bands": ["prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "prob",
        },
    },
    "color_ramp": [
        {
            "value": 0,
            "color": "black",
            "alpha": 0.0,
        },
        {
            "value": 1,
            "color": "#010007",
        },
        {
            "value": 10,
            "color": "#170b3b",
        },
        {
            "value": 20,
            "color": "#410967",
        },
        {
            "value": 30,
            "color": "#6b176e",
        },
        {
            "value": 40,
            "color": "#952666",
        },
        {
            "value": 50,
            "color": "#bb3754",
        },
        {
            "value": 60,
            "color": "#dd5238",
        },
        {
            "value": 70,
            "color": "#f37719",
        },
        {
            "value": 80,
            "color": "#fba60b",
        },
        {
            "value": 90,
            "color": "#f5d948",
        },
        {
            "value": 100,
            "color": "#fcfea4",
        },
    ],
    "range": [0, 100],
    "legend": {
        "begin": "0",
        "end": "100",
        "ticks_every": "20",
    },
}

style_crop_mask_green = {
    "name": "green",
    "title": "Crop area",
    "abstract": "Classified as crop",
    "value_map": {
        "mask": [
            {
                "title": "Crop area",
                "color": "#00FF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_yellow = {
    "name": "yellow",
    "title": "Crop area",
    "abstract": "Classified as crop",
    "value_map": {
        "mask": [
            {
                "title": "Crop area",
                "color": "#FFFF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_filtered_green = {
    "name": "filtered_green",
    "title": "Crop area (object-filtered)",
    "abstract": "Classified as crop and filtered",
    "value_map": {
        "filtered": [
            {
                "title": "Crop area",
                "color": "#00FF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_filtered_yellow = {
    "name": "filtered_yellow",
    "title": "Crop area (object-filtered)",
    "abstract": "Classified as crop and filtered",
    "value_map": {
        "filtered": [
            {
                "title": "Crop area",
                "color": "#FFFF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_reversed = {
    "name": "reversed",
    "title": "Reversed",
    "abstract": "Classified as crop by the mask band",
    "value_map": {
        "mask": [
            {
                "title": "Crop area",
                "color": "#CCCCCC",  # (Or #FFFF00)
                "values": [1],
                "mask": True,  # transparent
            },
            {
                "title": "No Crop",
                "color": "#CCCCCC",  # (Or #FFFF00)
                "values": [0],
            },
        ]
    },
}

layer = {
    "title": "Cropland Extent Map for Eastern Africa",
    "name": "crop_mask_eastern",
    "abstract": """
Digital Earth Africa's cropland extent map for Eastern Africa shows the location of croplands in the countries of Tanzania, Kenya, Uganda, Ethiopia, Rwanda, and Burundi. Cropland is defined as: "a piece of land of minimum 0.04 ha (a single 10m x 10m pixel) that is sowed/planted and harvest-able at least once within the 12 months after the sowing/planting date." This definition will exclude non-planted grazing lands and perennial crops which can be difficult for satellite imagery to differentiate from natural vegetation.

This provisional cropland extent map has a resolution of 10m, and was built using Copernicus Sentinel-2 satellite images from 2019 and 2020. The cropland extent map was produced using extensive training data from Eastern Africa, coupled with a Random Forest machine learning model. For a detailed exploration of the methods used to produce the cropland extent map, read the jupyter notebooks in DE Africa’s crop-mask github repository.

An independent validation dataset suggests this product has an overall accuracy of 90.3 %. The algorithm tends to report more omission errors (labelling actual crops as non-crops) than commission errors (labelling non-crops as crops). Where commission errors occur they tend to be focussed around wetlands and seasonal grasslands (e.g. in the Serengeti) which spectrally resemble some kinds of cropping.

The product contains three bands:
- mask: This band displays cropped regions as a binary map. Values of 1 indicate the presence of crops, while a value of 0 indicates the absence of cropping. This band is a pixel-based cropland extent map, meaning the map displays the raw output of the pixel-based Random Forest classification.
- prob: This band displays the prediction probabilities for the 'crop' class. As this product used a random forest classifier, the prediction probabilities refer to the percentage of trees that voted for the random forest classification. For example, if the model had 200 decision trees in the random forest, and 150 of the trees voted 'crop', the prediction probability is 150 / 200 x 100 = 75 %. Thresholding this band at 50 % will produce a map identical to mask.
- filtered: This band displays cropped regions as a binary map. Values of 1 indicate the presence of crops, while a value of 0 indicates the absence of cropping. This band is an object-based cropland extent map where the mask band has filtered using an image segmentation algorithm. During this process, segments smaller than 1 Ha (100 10m x 10m pixels) are merged with neighbouring segments, resulting in a map where the smallest classified region is 1 Ha is size. The filtered dataset is provided as small commission errors are removed by this process, and the 'salt and pepper' effect typical of classifying pixels is diminished.

More techincal information about the GeoMAD product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Cropland_extent_specs.html)

Cropland extent maps are a foundational, baseline layer in high-order crop health and crop productivity products which necessarily rely on knowing where cropping occurs before further analysis can take place.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "crop_mask_eastern",
    "time_resolution": "year",
    "bands": bands_crop_mask,
    "resource_limits": reslim_alos_palsar,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "wcs": {
        "native_crs": "epsg:6933",
        "native_resolution": [10, -10],
        "default_bands": ["mask", "prob"],
    },
    "styling": {
        "default_style": "green",
        "styles": [
            style_crop_mask_green,
            style_crop_mask_filtered_yellow,
            style_crop_mask_prob,
        ],
    },
}
