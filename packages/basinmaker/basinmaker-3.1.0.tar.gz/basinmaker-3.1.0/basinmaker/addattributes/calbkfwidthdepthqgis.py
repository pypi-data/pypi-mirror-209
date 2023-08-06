from basinmaker.func.grassgis import *
from basinmaker.func.qgis import *
from basinmaker.func.pdtable import *
from basinmaker.func.rarray import *
from basinmaker.utilities.utilities import *
import sqlite3
from scipy.optimize import curve_fit
from basinmaker.preprocessing.reprojectandclipvectorbyplyqgis import (
    reproject_clip_vectors_by_polygon,
)


def calculate_bankfull_width_depth_from_polyline(
    grassdb,
    grass_location,
    qgis_prefix_path,
    path_bkfwidthdepth,
    path_k_c_zone_polygon,
    bkfwd_attributes,
    catinfo,
    input_geo_names,
    k_in=-1,
    c_in=-1,
    return_k_c_only=False,
):
    mask = input_geo_names["mask"]
    cat_ply_info = input_geo_names["cat_ply_info"]

    default_slope = min_riv_slope
    min_manning_n = 0.025
    max_manning_n = 0.15
    default_bkf_width = 1.2345
    default_bkf_depth = 1.2345
    default_bkf_q = 1.2345
    k = -1
    c = -1
    if path_bkfwidthdepth != "#":
        reproject_clip_vectors_by_polygon(
            grassdb=grassdb,
            grass_location=grass_location,
            qgis_prefix_path=qgis_prefix_path,
            mask=os.path.join(grassdb, mask + ".shp"),
            path_polygon=path_bkfwidthdepth,
            ply_name="bkf_width_depth",
        )
    if path_k_c_zone_polygon != '#':
        reproject_clip_vectors_by_polygon(
            grassdb=grassdb,
            grass_location=grass_location,
            qgis_prefix_path=qgis_prefix_path,
            mask=os.path.join(grassdb, mask + ".shp"),
            path_polygon=path_k_c_zone_polygon,
            ply_name="kc_zone",
        )

    import grass.script as grass
    import grass.script.setup as gsetup
    from grass.pygrass.modules import Module
    from grass.pygrass.modules.shortcuts import general as g
    from grass.pygrass.modules.shortcuts import raster as r
    from grass.script import array as garray
    from grass.script import core as gcore
    from grass_session import Session

    os.environ.update(
        dict(GRASS_COMPRESS_NULLS="1", GRASS_COMPRESSOR="ZSTD", GRASS_VERBOSE="1")
    )
    PERMANENT = Session()
    PERMANENT.open(gisdb=grassdb, location=grass_location, create_opts="")

    con = sqlite3.connect(
        os.path.join(grassdb, grass_location, "PERMANENT", "sqlite", "sqlite.db")
    )

    if path_bkfwidthdepth != "#":
        grass.run_command(
            "v.import",
            input=os.path.join(grassdb, "bkf_width_depth" + ".shp"),
            output="bk_full_wid_depth",
            overwrite=True,
        )

    if path_k_c_zone_polygon != "#":
        grass.run_command(
            "v.import",
            input=os.path.join(grassdb, "kc_zone_clip" + ".shp"),
            output="kc_zone",
            overwrite=True,
        )

        grass.run_command(
            "v.overlay",
            ainput="kc_zone",
            alayer=1,
            atype="area",
            binput=cat_ply_info,
            operator="and",
            output=cat_ply_info + "kc",
            overwrite=True,
        )
        grass.run_command(
            "v.to.db",
            map=cat_ply_info + "kc",
            option="area",
            columns="Area_kc",
            units="meters",
            overwrite=True,
        )


    if k_in < 0 and c_in < 0:
        ### read catchment
        if path_bkfwidthdepth != '#':
            sqlstat = "SELECT %s,%s,%s,%s FROM %s" % (
                bkfwd_attributes[3],
                bkfwd_attributes[2],
                bkfwd_attributes[1],
                bkfwd_attributes[0],
                "bk_full_wid_depth",
            )
            bkf_width_depth = pd.read_sql_query(sqlstat, con)
            bkf_width_depth = bkf_width_depth.fillna(-9999)

            da_q = bkf_width_depth[[bkfwd_attributes[3], bkfwd_attributes[2]]].values

            if len(da_q) > 3:
                k, c = return_k_and_c_in_q_da_relationship(da_q)
            elif len(da_q) > 0 and len(da_q) <= 3:
                k = -1
                c = -1
                default_bkf_width = np.average(bkf_width_depth[bkfwd_attributes[0]])
                default_bkf_depth = np.average(bkf_width_depth[bkfwd_attributes[1]])
                default_bkf_q = np.average(bkf_width_depth[bkfwd_attributes[3]])
            else:
                k = -1
                c = -1

        if path_k_c_zone_polygon != '#':
            k = -1
            c = -1
            sqlstat = "SELECT a_k, a_c,b_Gridcode, Area_kc FROM %s" % (cat_ply_info + "kc")
            k_c_sub = pd.read_sql_query(sqlstat, con)
            k_c_sub = k_c_sub.fillna(-9999)
            k_c_sub = k_c_sub.sort_values(by='Area_kc', ascending=False)
            k_c_sub = k_c_sub.drop_duplicates(subset=['b_Gridcode'])

    else:
        k = k_in
        c = c_in

    if return_k_c_only:
        return k, c


    if 'k_c_sub' not in locals() and k == -1:
        return

    idx = catinfo.index
    for i in range(0, len(idx)):
        idx_i = idx[i]
        da = catinfo.loc[idx_i, "DrainArea"] / 1000 / 1000  # m2 to km2
        catid = catinfo.loc[idx_i, "SubId"]
        if k > 0:
            q = func_Q_DA(da, k, c)
            catinfo.loc[idx_i, "BkfWidth"] =  max(7.2 * q ** 0.5,min_bkf_width)
            catinfo.loc[idx_i, "BkfDepth"] =  max(0.27 * q ** 0.3,min_bkf_depth)
            catinfo.loc[idx_i, "Q_Mean"] = q
            catinfo.loc[idx_i, "k"] = k
            catinfo.loc[idx_i, "c"] = c

        elif 'k_c_sub' in locals():
            if len(k_c_sub.loc[k_c_sub["b_Gridcode"] == catid]) < 1:
                k_sub =  0.00450718
                c_sub =  0.98579699
                print("k_sub not found .....")
            else:
                k_sub = k_c_sub.loc[k_c_sub["b_Gridcode"] == catid]["a_k"].values[0]
                c_sub = k_c_sub.loc[k_c_sub["b_Gridcode"] == catid]["a_c"].values[0]
                if k_sub < 0:
                    k_sub =  0.00450718
                    c_sub =  0.98579699

            q = func_Q_DA(da, k_sub, c_sub)
            catinfo.loc[idx_i, "BkfWidth"] =  max(7.2 * q ** 0.5,min_bkf_width)
            catinfo.loc[idx_i, "BkfDepth"] =  max(0.27 * q ** 0.3,min_bkf_depth)
            catinfo.loc[idx_i, "Q_Mean"] = q
            catinfo.loc[idx_i, "k"] = k_sub
            catinfo.loc[idx_i, "c"] = c_sub

        else:
            catinfo.loc[idx_i, "BkfWidth"] = default_bkf_width
            catinfo.loc[idx_i, "BkfDepth"] = default_bkf_depth
            catinfo.loc[idx_i, "Q_Mean"] = default_bkf_q

        if catinfo.loc[idx_i, "Lake_Cat"] < 2:
            if catinfo.loc[idx_i, "Max_DEM"] < 0:
                catinfo.loc[idx_i, "Max_DEM"] = catinfo.loc[idx_i, "MeanElev"]
                catinfo.loc[idx_i, "Min_DEM"] = catinfo.loc[idx_i, "MeanElev"]

    # adjust channel parameters

    #remove ncl and headwater subbasins
    catinfo_riv = catinfo.loc[(catinfo["Lake_Cat"] < 2) & (catinfo["RivLength"] != -1.2345)].copy(deep=True)

    Seg_IDS = catinfo_riv["Seg_ID"].values
    Seg_IDS = np.unique(Seg_IDS)

    for iseg in range(0, len(Seg_IDS)):
        i_seg_id = Seg_IDS[iseg]
        i_seg_info = catinfo_riv[catinfo_riv["Seg_ID"] == i_seg_id]
        if len(i_seg_info["RivLength"].values[i_seg_info["RivLength"].values > 0]) > 0:
            length_seg = np.sum(i_seg_info["RivLength"].values[i_seg_info["RivLength"].values > 0])
        else:
            length_seg = 1
        qmean_seg = np.average(i_seg_info["Q_Mean"].values[i_seg_info["Q_Mean"].values > 0])
        width_seg = np.average(i_seg_info["BkfWidth"].values[i_seg_info["BkfWidth"].values > 0])
        depth_Seg = np.average(i_seg_info["BkfDepth"].values[i_seg_info["BkfDepth"].values > 0])
        floodn_Seg = np.average(i_seg_info["FloodP_n"].values[i_seg_info["FloodP_n"].values > 0])
        basslp_Seg = np.average(i_seg_info["BasSlope"].values[i_seg_info["BasSlope"].values > 0])
        basasp_Seg = np.average(i_seg_info["BasAspect"].values[i_seg_info["BasAspect"].values > 0])
        baselv_Seg = np.average(i_seg_info["MeanElev"].values[i_seg_info["MeanElev"].values > 0])

        if len(i_seg_info["Max_DEM"].values[i_seg_info["Max_DEM"].values > -999999999999999999]) > 0:
            max_elve_seg = np.max(i_seg_info["Max_DEM"].values[i_seg_info["Max_DEM"].values > -9999999999999999])
            min_elve_seg = np.min(i_seg_info["Min_DEM"].values[i_seg_info["Min_DEM"].values > -9999999999999999])
        else:
            max_elve_seg = baselv_Seg
            min_elve_seg = baselv_Seg

        slope_seg = (max_elve_seg - min_elve_seg) / length_seg
        if slope_seg < 0.000000001:
            slope_seg = min_riv_slope  #### Needs to update later

        n_seg = calculateChannaln(width_seg, depth_Seg, qmean_seg, slope_seg)

        for i in range(0, len(i_seg_info)):
            subid = i_seg_info["SubId"].values[i]
            max_elve_rch = i_seg_info["Max_DEM"].values[i]
            min_elve_rch = i_seg_info["Min_DEM"].values[i]
            length_rch = max(i_seg_info["RivLength"].values[i],min_riv_lenth)
            qmean_rch = i_seg_info["Q_Mean"].values[i]
            width_rch = i_seg_info["BkfWidth"].values[i]
            depth_rch = i_seg_info["BkfDepth"].values[i]
            floodn_rch = i_seg_info["FloodP_n"].values[i]

            if min_elve_rch < -2000:
                if i_seg_info["MeanElev"].values[i] > -2000:
                    min_elve_rch = i_seg_info["MeanElev"].values[i]
                else:
                    min_elve_rch = baselv_Seg

            if max_elve_rch < -2000:
                if i_seg_info["MeanElev"].values[i] > -2000:
                    max_elve_rch = i_seg_info["MeanElev"].values[i]
                else:
                    max_elve_rch = baselv_Seg

            slope_rch = (max_elve_rch - min_elve_rch) / length_rch


            if slope_rch < min_riv_slope or slope_rch > max_riv_slope:
                if slope_seg >= min_riv_slope and slope_seg <= max_riv_slope:
                    slope_rch = slope_seg

            slope_rch = max(slope_rch,min_riv_slope)
            slope_rch = min(slope_rch,max_riv_slope)

            n_rch = calculateChannaln(width_rch, depth_rch, qmean_rch, slope_rch)

            if n_rch < min_manning_n or n_rch > max_manning_n:
                if n_seg >= min_manning_n and n_seg <= max_manning_n:
                    n_rch = n_seg

            n_rch = max(n_rch,min_manning_n)
            n_rch = min(n_rch,max_manning_n)

            catinfo.loc[catinfo["SubId"] == subid, "RivSlope"] = slope_rch
            catinfo.loc[catinfo["SubId"] == subid, "Ch_n"] = n_rch
            catinfo.loc[catinfo["SubId"] == subid, "RivLength"] = length_rch


            # if subid == 504:
            #     print(floodn_rch)


            if floodn_rch < 0:
                if floodn_Seg > 0:
                    floodn_rch = floodn_Seg
                else:
                    floodn_rch = DEFALUT_FLOOD_N

            floodn_rch = max(floodn_rch,n_rch)
            catinfo.loc[catinfo["SubId"] == subid, "FloodP_n"] = floodn_rch
            catinfo.loc[catinfo["SubId"] == subid, "Max_DEM"] = max_elve_rch
            catinfo.loc[catinfo["SubId"] == subid, "Min_DEM"] = min_elve_rch

            # if subid == 504:
            #     print(floodn_rch)
            #     asdf

            if i_seg_info["BasSlope"].values[i] <= 0:
                if basslp_Seg > 0:
                    catinfo.loc[catinfo["SubId"] == subid, "BasSlope"] = basslp_Seg
                else:
                    catinfo.loc[catinfo["SubId"] == subid, "BasSlope"] = 0

            if i_seg_info["BasAspect"].values[i] <= 0:
                if basasp_Seg > 0:
                    catinfo.loc[catinfo["SubId"] == subid, "BasAspect"] = basasp_Seg
                else:
                    catinfo.loc[catinfo["SubId"] == subid, "BasAspect"] = 0

            if i_seg_info["MeanElev"].values[i] < 0:
                if baselv_Seg > 0:
                    catinfo.loc[catinfo["SubId"] == subid, "MeanElev"] = baselv_Seg
                else:
                    catelv = catinfo['MeanElev'].values
                    catelv = catelv[catelv > 0]
                    catinfo.loc[catinfo["SubId"] == subid, "MeanElev"] =np.average(catelv)
    PERMANENT.close()
    return catinfo
