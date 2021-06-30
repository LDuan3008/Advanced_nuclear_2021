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
    region = sys.argv[2]
    year = sys.argv[3]


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
case_dic['year_start'] = 2018
case_dic['year_end'] = 2018
tech_list[demand_idx]['series_file'] = DemandName;   update_series(case_dic, tech_list[demand_idx])
case_dic['year_start'] = 2019
case_dic['year_end'] = 2019
tech_list[solar_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_idx])
tech_list[wind_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_idx])
num_time_periods = update_timenum(case_dic)
case_name_default = case_dic['case_name']

### Set cycle values
co2_constraints_percentage = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 
                              38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])

upper_co2_emissions = num_time_periods * 1 * co2_emis_natgas
co2_constraints_list = upper_co2_emissions * co2_constraints_percentage / 100
case_dic['dispatch_constraint'] = -1

### Run models
for idx in range(len(co2_constraints_list)):
    case_dic['co2_constraint'] = co2_constraints_list[idx]
    case_dic['case_name'] = case_name_default + '_Year' + str(year) + '_' + str(region) + '_Co2Cons' + str(co2_constraints_percentage[idx])
    run_model_main_fun(case_dic, tech_list) 