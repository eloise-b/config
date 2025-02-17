ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {  # GDA-94, Australian Albers. Not sure why, but it's required!
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
            "EPSG:6933": {  # Cylindrical equal area
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "ESRI:102022": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
            "https://ows-us.digitalearth.africa",
            "https://ows-us-latest.digitalearth.africa",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Africa - OGC Web Services",
        "abstract": """Digital Earth Africa OGC Web Services""",
        "info_url": "digitalearthafrica.org/",
        "keywords": [
            "landsat",
            "africa",
            "WOfS",
            "fractional-cover",
            "time-series",
        ],
        "contact_info": {
            "person": "Digital Earth Africa",
            "organisation": "Geoscience Australia",
            "position": "",
            "address": {
                "type": "postal",
                "address": "GPO Box 378",
                "city": "Canberra",
                "state": "ACT",
                "postcode": "2609",
                "country": "Australia",
            },
            "telephone": "+61 2 6249 9111",
            "fax": "",
            "email": "info@digitalearthafrica.org",
        },
        "fees": "",
        "access_constraints": "© Commonwealth of Australia (Geoscience Australia) 2018. "
        "This product is released under the Creative Commons Attribution 4.0 International Licence. "
        "http://creativecommons.org/licenses/by/4.0/legalcode",
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_url": "https://data.digitalearth.africa",
        "s3_bucket": "deafrica-data",
        "s3_aws_zone": "ap-southeast-2",
        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                # "renderer": "datacube_ows.wcs_utils.get_tiff",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False,
            },
            "netCDF": {
                # "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Digital Earth Africa - OGC Web Services",
            "abstract": "Digital Earth Africa OGC Web Services",
            "layers": [
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
                {
                    "title": "Satellite images",
                    "abstract": """Satellite images""",
                    "layers": [
                        {
                            "title": "Surface reflectance",
                            "abstract": """Surface reflectance""",
                            "layers": [
                                {
                                    "include": "ows_refactored.surface_reflectance.ows_sr_cfg.layers",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.surface_reflectance.ows_s2_cfg.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.surface_reflectance.ows_geomedian_cfg.layers",
                                    "type": "python",
                                },
                            ]
                        },
                        {
                            "title": "Radar backscatter",
                            "abstract": """Radar backscatter""",
                            "layers": [
                                {
                                    "include": "ows_refactored.radar_backscatter.ows_alos_cfg.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.radar_backscatter.ows_us_jers_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                    ]
                },
                {
                    "title": "Surface water",
                    "abstract": """Surface water""",
                    "layers": [
                        {
                            "include": "ows_refactored.wofs.ows_wofs_cfg.layers",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.wofs.ows_wofsc2_cfg.layers",
                            "type": "python",
                        },
                    ]
                },
                {
                    "title": "Vegetation",
                    "abstract": """Vegetation""",
                    "layers": [
                        {
                            "include": "ows_refactored.vegetation.ows_us_fc_cfg.layer",
                            "type": "python",
                        },
                    ]
                },
                {
                    "title": "Elevation",
                    "abstract": """Digital elevation model from NASA's SRTM<""",
                    "layers": [
                        {
                            "include": "ows_refactored.elevation.ows_us_srtm_cfg.layer",
                            "type": "python",
                        },
                    ],
                },
            ],
        }
    ],
}
