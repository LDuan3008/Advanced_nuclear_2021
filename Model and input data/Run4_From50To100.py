from Preprocess_Input import preprocess_input
from Run_Core_Model import run_model_main_fun
from FindRegion import GetCFsName, update_series, update_timenum
import sys, numpy as np, os, pickle

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
    if name == 'solar_fixed': solar_fixed_idx = idx 
    if name == 'wind_fixed': wind_fixed_idx = idx 

### Set basic information
case_dic['output_path'] = '/data/carnegie/leiduan/cesm_archive/MEM_AdvNuc' 
DemandName, SolarCFsName, WindCFsName = GetCFsName(region) 

if year == 2019:
    case_dic['year_start'] = 2018
    case_dic['year_end'] = 2018
    tech_list[demand_idx]['series_file'] = DemandName;   update_series(case_dic, tech_list[demand_idx])
    case_dic['year_start'] = 2019
    case_dic['year_end'] = 2019
    tech_list[solar_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_idx])
    tech_list[wind_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_idx])
    tech_list[solar_fixed_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_fixed_idx])
    tech_list[wind_fixed_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_fixed_idx])
else:
    case_dic['year_start'] = year
    case_dic['year_end'] = year
    tech_list[demand_idx]['series_file'] = DemandName;   update_series(case_dic, tech_list[demand_idx])
    tech_list[solar_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_idx])
    tech_list[wind_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_idx])
    tech_list[solar_fixed_idx]['series_file']  = SolarCFsName; update_series(case_dic, tech_list[solar_fixed_idx])
    tech_list[wind_fixed_idx]['series_file']   = WindCFsName;  update_series(case_dic, tech_list[wind_fixed_idx])
num_time_periods = update_timenum(case_dic)
case_dic['num_time_periods'] = num_time_periods
case_dic['dispatch_constraint'] = -1

### Getting base case
case_name =  case_dic['case_name'] + '_Year' + str(year) + '_' + str(region) + '_Co2Cons50'
output_folder = case_dic['output_path'] + '/' + case_name + '/'
file_list = os.listdir(output_folder)

for file in file_list:
    if file[-6:] == "pickle": 
        case_name_open = file
        break

# print ()
# print ()
# print (case_name)
# print (output_folder)
# print (case_name_open)
# print ()
# print ()
# print (DemandName)
# print (tech_list[demand_idx]['series'])
# print ()
# print ()
# print ()
# stop 
# sys.exit()

with open(output_folder+case_name_open, 'rb') as handle:
    [[input_case_dic,  input_tech_list,  input_time_dic],
    [results_case_dic,  results_tech_dic,  results_time_dic]] = pickle.load(handle)
### Set fixed capacities
for tech_idx in range(len(tech_list)):
    if tech_list[tech_idx]['tech_name'] == 'natgas_fixed':
        tech_list[tech_idx]['capacity'] = 0 
    if tech_list[tech_idx]['tech_name'] == 'natgas_ccs_fixed':
        tech_list[tech_idx]['capacity'] = 0 
    if tech_list[tech_idx]['tech_name'] == 'solar_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['solar capacity']
    if tech_list[tech_idx]['tech_name'] == 'wind_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['wind capacity']
    if tech_list[tech_idx]['tech_name'] == 'storage_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['storage capacity'] 
    if tech_list[tech_idx]['tech_name'] == 'nuclear_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['nuclear capacity'] 
    if tech_list[tech_idx]['tech_name'] == 'heat_storage_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['heat_storage capacity'] 
    if tech_list[tech_idx]['tech_name'] == 'nuclear_generator_fixed':
        tech_list[tech_idx]['capacity'] = results_tech_dic['nuclear_generator capacity'] 

co2_constraints_percentage = 1.0
case_dic['co2_constraint'] = num_time_periods * 1 * co2_emis_natgas * co2_constraints_percentage / 100.0
case_dic['case_name'] = 'zzzto99_' + case_name

print () 
print ('start running models')
print ()
print ()
print (DemandName)
print (tech_list[demand_idx]['series'])
print ()
print ()
print (case_dic)
print (tech_list)
run_model_main_fun(case_dic, tech_list) 
print ('end running models')
print () 