from Preprocess_Input import preprocess_input
from Run_Core_Model import run_model_main_fun
from FindRegion import GetCFsName, update_series, update_timenum
import sys, numpy as np


### Read input data
if len(sys.argv) < 4:
    print ('give parameter ;;code input region year;;') 
    stop
else:
    case_input_path_filename = sys.argv[1]
    region = str(sys.argv[2])
    year = int(sys.argv[3])


### Pre-processing
print ('Macro_Energy_Model: Pre-processing input')
case_dic,tech_list = preprocess_input(case_input_path_filename)


### Find values
for idx in range(len(tech_list)):
    name = tech_list[idx]['tech_name']
    if name == 'natgas': co2_emis_natgas = tech_list[idx]['var_co2']
    if name == 'demand': demand_idx = idx
    if name == 'solar': solar_idx = idx 
    if name == 'wind': wind_idx = idx


### Set basic information
case_dic['output_path'] = '/data/carnegie/leiduan/cesm_archive/MEM_AdvNuc'
DemandName, SolarCFsName, WindCFsName = GetCFsName(region)
case_dic['year_start'] = year
case_dic['year_end'] = year
tech_list[demand_idx]['series_file'] = DemandName;   update_series(case_dic, tech_list[demand_idx])
tech_list[solar_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_idx])
tech_list[wind_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_idx])
num_time_periods = update_timenum(case_dic)
case_dic['num_time_periods'] = num_time_periods
case_name_default = case_dic['case_name']


### Set cycle values
co2_constraints_percentage = np.array([1e24, 50, 0])
upper_co2_emissions = num_time_periods * 1 * co2_emis_natgas
co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100


### Run models
for idx in range(len(co2_constraints_list)):
    case_dic['co2_constraint'] = co2_constraints_list[idx]
    case_dic['case_name'] = case_name_default + '_Year' + str(year) + '_' + str(region) + '_Co2Cons' + str(co2_constraints_percentage[idx])
    run_model_main_fun(case_dic, tech_list) 