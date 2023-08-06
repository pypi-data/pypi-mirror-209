from bm_utilities import Address_finder as af
from bm_utilities import quality_gates as qg

import geopandas as gpd
import pandas as pd


def address_finder(geodf,address):
    construct = af.AddressFinder(geodf)
    address = construct.find_address(address)
    return address


def quality_gates_check(df,config):
    my_gate = qg.QualityGates()
    df=my_gate.run_Quality_Gates(df,config)
    return df





'''
geo_df = gpd.read_file(r"D:\\Task_2\\point of interst\\Reading shape files\\egy_admbnda_adm3_capmas_20170421.shp")
address = pd.read_csv(r"D:\\Task_2\\address_finder_application\\output\\Address_Finder\\Address Finder\\test_data.csv")
construct = AddressFinder(geo_df)
address = construct.find_address(address)
print(address)
'''


#for i in range(Branches_lat_long.shape[0]):
#    if((Branches_lat_long[['lat']].iloc[i,:]).isna()):
#        continue
#    latitude = Branches_lat_long[['lat','long']].iloc[i,:]
#    longitude = Branches_lat_long[['lat','long']].iloc[i,:]
#    print(latitude,longitude)