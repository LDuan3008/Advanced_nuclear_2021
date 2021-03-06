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
    if name == 'demand': demand_idx = idx
    if name == 'solar': solar_idx = idx 
    if name == 'wind': wind_idx = idx
    if name == 'lost_load': lost_load_idx = idx

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
case_name_default = 'LostLoad'
case_dic['co2_constraint'] = 0

### Set cycle values
unmet_demand_cost = [10**(-3), 10**(-2.8), 10**(-2.6), 10**(-2.4), 10**(-2.2),
                     10**(-2), 10**(-1.8), 10**(-1.6), 10**(-1.4), 10**(-1.2),
                     10**(-1), 10**(-0.8), 10**(-0.6), 10**(-0.4), 10**(-0.2),
                     10**0,    10**0.2,    10**0.4,    10**0.6,    10**0.8,
                     10**1]

for idx in range(len(unmet_demand_cost)):
    tech_list[lost_load_idx]['var_cost'] = unmet_demand_cost[idx]
    case_dic['case_name'] = case_name_default + '_Year' + str(year) + '_' + str(region) + '_LostLoad' + str(unmet_demand_cost[idx])
    run_model_main_fun(case_dic, tech_list) 