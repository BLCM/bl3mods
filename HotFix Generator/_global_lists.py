##Function i uses to get only what is needed if you are choosing a JSON file
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names

FuncNames = ["get_data", "find", "find_data", "glob", "glob_data", "get_export_idx",
             "get_exports", "get_parts_category_name", "get_extra_anoints"]  # stores function names

#this is used to remove any data when searching files. may add or remove depending on what I learn later
NonUsedInfo = ["_apoc_data_ver", "_jwp_export_idx", "_jwp_is_asset",
               "_jwp_object_name", "export_type", "_jwp_arr_idx"]