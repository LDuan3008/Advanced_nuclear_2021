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
    if name == 'dac': dac_idx = idx
    if name == 'to_PGP': to_pgp_idx = idx
    if name == 'from_PGP': from_pgp_idx = idx

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
case_name_default = 'PGP'
case_dic['co2_constraint'] = 0
case_dic['dispatch_constraint'] = -1

### Set cycle values
dac_vari_costs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] # $/kgCO2
ptp_cost_ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

to_pgp_org = tech_list[to_pgp_idx]['fixed_cost']
from_pgp_org = tech_list[from_pgp_idx]['fixed_cost']
for pgp_ratio_idx in range(len(ptp_cost_ratio)):
    tech_list[to_pgp_idx]['fixed_cost'] = to_pgp_org * ptp_cost_ratio[pgp_ratio_idx]
    tech_list[from_pgp_idx]['fixed_cost'] = from_pgp_org * ptp_cost_ratio[pgp_ratio_idx]
    case_dic['case_name'] = case_name_default + '_Year' + str(year) + '_' + str(region) + '_pgp' + str(ptp_cost_ratio[pgp_ratio_idx])
    run_model_main_fun(case_dic, tech_list) 