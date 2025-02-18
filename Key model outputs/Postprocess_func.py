
import matplotlib.pyplot as plt 
import numpy as np
import pickle, os, sys
from scipy import stats


category1 = ['natgas', 'natgas_ccs', 'natgas_fixed', 'natgas_ccs_fixed', 'dac']
category2 = ['solar',       'wind',       'storage',       'conventional_nuclear',       'Resistant Heater',
             'solar_fixed', 'wind_fixed', 'storage_fixed', 'conventional_nuclear_fixed', 'Resistant Heater_fixed']
category3 = {'advanced_nuclear':['nuclear', 'nuclear_generator', 'heat_storage'],
             'advanced_nuclear_fixed':['nuclear_fixed', 'nuclear_generator_fixed', 'heat_storage_fixed']}
category4 = ['lost_load']
category5 = ['shift_load']
category6 = {'pgp':['to_PGP', 'PGP_storage', 'from_PGP']}

def initial_keys(info, keylist):
    for key in keylist:
        info[key] = []

def nonan(input):
    input[input==0] = np.nan
    return input

def Update_info(info, category, results_tech_dic, results_case_dic, results_time_dic, input_case_dic, cost):
    if category in category1:
        cost_var = cost[category + '_var']
        cost_fix = cost[category + '_fix']
        cost_co2 = cost[category + '_co2']
        co2_price_n = input_case_dic['co2_price']
        info[category+'_cap'].append(results_tech_dic[category+' capacity'])
        info[category+'_tot'].append(cost_fix * results_tech_dic[category+' capacity']+np.mean(cost_var * results_time_dic[category+' dispatch'])+np.mean(cost_co2 * results_time_dic[category+' dispatch'] * co2_price_n))
    if category in category2:
        cost_fix = cost[category+'_fix']
        info[category+'_cap'].append(results_tech_dic[category+' capacity'])
        info[category+'_fix'].append(cost_fix * results_tech_dic[category+' capacity'])
    if category in category3.keys():
        name_list = category3[category]
        nuclear_generator_eff = cost['nuclear_generator_eff']
        # Reactor
        REAcap = results_tech_dic[name_list[0]+' capacity'] * nuclear_generator_eff
        REAcos = results_tech_dic[name_list[0]+' capacity'] * cost[name_list[0]+'_fix']
        info[name_list[0]+'_cap'].append(REAcap)
        info[name_list[0]+'_fix'].append(REAcos)
        # TES
        TEScap = results_tech_dic[name_list[2]+' capacity'] * nuclear_generator_eff
        TEScos = results_tech_dic[name_list[2]+' capacity'] * cost[name_list[2]+'_fix']
        info[name_list[2]+'_cap'].append(TEScap)
        info[name_list[2]+'_fix'].append(TEScos)
        # Generator
        GENcap_REAmatch = REAcap
        GENcos_REAmatch = GENcap_REAmatch * cost[name_list[1]+'_fix']
        info[name_list[1]+'_REAmatch_cap'].append(GENcap_REAmatch)
        info[name_list[1]+'_REAmatch_fix'].append(GENcos_REAmatch)
        GENcap_TESmatch = results_tech_dic[name_list[1]+' capacity'] - GENcap_REAmatch
        GENcos_TESmatch = GENcap_TESmatch * cost[name_list[1]+'_fix']
        info[name_list[1]+'_TESmatch_cap'].append(GENcap_TESmatch)
        info[name_list[1]+'_TESmatch_fix'].append(GENcos_TESmatch)
    if category in category4:
        cost_var = cost[category+'_var']
        info[category+'_var'].append(np.mean(results_time_dic[category+' dispatch']*cost_var))
        info[category+'_mean'].append(np.mean(results_time_dic[category+' dispatch']))
    if category in category5:
        cost_var = cost[category+'_var']
        cost_fix = cost[category + '_fix']
        absolute_dispatch = np.abs(results_time_dic[category+' stored'])
        info[category+'_tot'].append(cost_fix * results_tech_dic[category+' capacity']+np.mean(cost_var * absolute_dispatch))
    if category == 'others':
        info['system_cost'].append(results_case_dic['system_cost'])
        info['co2_emissions'].append(results_case_dic['co2_emissions'])
    if category in category6:
        name_list = category6[category]
        # To_PGP
        to_pgp_eff = cost['to_PGP_eff']
        to_pgp_cap = results_tech_dic[name_list[0]+' capacity'] * to_pgp_eff
        to_pgp_cos = results_tech_dic[name_list[0]+' capacity'] * cost[name_list[0]+'_fix']
        info[name_list[0]+'_cap'].append(to_pgp_cap)
        info[name_list[0]+'_fix'].append(to_pgp_cos)
        # PGP_storage
        pgp_storage_cap = results_tech_dic[name_list[1]+' capacity']
        pgp_storage_cos = results_tech_dic[name_list[1]+' capacity'] * cost[name_list[1]+'_fix']
        info[name_list[1]+'_cap'].append(pgp_storage_cap)
        info[name_list[1]+'_fix'].append(pgp_storage_cos)
        # From_PGP
        from_pgp_eff = cost['from_PGP_eff']
        from_pgp_cap = results_tech_dic[name_list[2]+' capacity'] * from_pgp_eff
        from_pgp_cos = results_tech_dic[name_list[2]+' capacity'] * cost[name_list[2]+'_fix']
        info[name_list[2]+'_cap'].append(from_pgp_cap)
        info[name_list[2]+'_fix'].append(from_pgp_cos)


    
    # Now add emissions calculation:
    if category in ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'conventional_nuclear', 'advanced_nuclear']:
        emissions_list = {'natgas':490, 'natgas_ccs':170, 'solar':48, 'wind':11, 'conventional_nuclear':12, 'advanced_nuclear':12,
                          'storage':0.1}
        if category in ['natgas', 'natgas_ccs']: info[category+'_emis'].append( np.sum(emissions_list[category] * results_time_dic[category+' dispatch']) )
        if category in ['solar', 'wind']: info[category+'_emis'].append( emissions_list[category] * np.sum(results_time_dic[category + ' potential']) ) 
        if category in ['advanced_nuclear']: info[category+'_emis'].append( emissions_list[category] * results_tech_dic[category3[category][1]+' capacity'] * np.sum(results_time_dic['demand potential']) ) 
        if category in ['conventional_nuclear']: info[category+'_emis'].append( emissions_list[category] * results_tech_dic[category+' capacity'] * np.sum(results_time_dic['demand potential']) ) 
        if category in ['storage']: info[category+'_emis'].append( 0 )



def Get_Table(default_case_name, **kwargs):

    if 'data_path' in kwargs:
        data_path = kwargs['data_path']
    else:
        data_path = './'
    
    if 'repeat_list' in kwargs:
        repeat_list = kwargs['repeat_list']
    else:
        repeat_list = ['']
    
    if 'dividing_name_point' in kwargs:
        dividing_name_point = kwargs['dividing_name_point']
    else:
        dividing_name_point = -1
    
    if 'tech_name_list' in kwargs:
        tech_name_list = kwargs['tech_name_list']
    else:
        tech_name_list = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'conventional_nuclear', 'advanced_nuclear', 'lost_load']

    info = {}
    initial_keys(info, ['system_cost', 'co2_emissions'])
    for tech_idx in tech_name_list:
        if tech_idx in category1:
            initial_keys(info, [tech_idx+'_cap', tech_idx+'_tot', tech_idx+'_emis'])
        if tech_idx in category2:
            initial_keys(info, [tech_idx+'_cap', tech_idx+'_fix', tech_idx+'_emis'])
        if tech_idx in category3.keys():
            name_list = category3[tech_idx]
            initial_keys(info, [name_list[0]+'_cap', name_list[0]+'_fix'])
            initial_keys(info, [name_list[2]+'_cap', name_list[2]+'_fix'])
            initial_keys(info, [name_list[1]+'_REAmatch_cap', name_list[1]+'_REAmatch_fix'])
            initial_keys(info, [name_list[1]+'_TESmatch_cap', name_list[1]+'_TESmatch_fix'])
            initial_keys(info, [tech_idx+'_emis'])
        if tech_idx in category4:
            initial_keys(info, [tech_idx+'_var'])
            initial_keys(info, [tech_idx+'_mean'])
        if tech_idx in category5:
            initial_keys(info, [tech_idx+'_tot'])
        if tech_idx in category6:
            name_list = category6[tech_idx]
            initial_keys(info, [name_list[0]+'_cap', name_list[0]+'_fix'])
            initial_keys(info, [name_list[1]+'_cap', name_list[1]+'_fix'])
            initial_keys(info, [name_list[2]+'_cap', name_list[2]+'_fix'])
            initial_keys(info, [tech_idx+'_emis'])


    def get_individual_case_result(case_name):

        file_list = os.listdir(data_path+case_name)
        for file in file_list:
            if file[-6:] == "pickle": 
                case_name_open = file
                break
        with open(data_path+case_name+case_name_open, 'rb') as handle:
            [[input_case_dic,  input_tech_list,  input_time_dic],
             [results_case_dic,  results_tech_dic,  results_time_dic]] = pickle.load(handle)

        if 'demand series' not in info.keys():
            info['demand series'] = input_time_dic['demand series']
            info['wind series'] = input_time_dic['wind series']
            info['solar series'] = input_time_dic['solar series']

        cost = {}
        for tech_idx in range(len(input_tech_list)):
            current_tech_list = input_tech_list[tech_idx]
            tech_name = current_tech_list['tech_name'] #.lower()
            if 'var_cost' in current_tech_list.keys():
                cost[tech_name+'_var'] = current_tech_list['var_cost']
            if 'fixed_cost' in current_tech_list.keys():
                cost[tech_name+'_fix'] = current_tech_list['fixed_cost'] 
            if 'var_co2' in current_tech_list.keys():
                cost[tech_name+'_co2'] = current_tech_list['var_co2']
            if 'efficiency' in current_tech_list.keys():
                cost[tech_name+'_eff'] = current_tech_list['efficiency'] 
        
        for tech_name_idx in tech_name_list:
            Update_info(info, tech_name_idx, results_tech_dic, results_case_dic, results_time_dic, input_case_dic, cost)
        Update_info(info, 'others', results_tech_dic, results_case_dic, results_time_dic, input_case_dic, cost)

    if repeat_list != ['']:
        for repeat_n in repeat_list:
            # print (repeat_n)
            if dividing_name_point > -1:
                case_name = default_case_name[:dividing_name_point] + str(repeat_n) + default_case_name[dividing_name_point:] + '/'
                get_individual_case_result(case_name)
            else:
                case_name = default_case_name + str(repeat_n) + '/'
                # print (case_name)
                get_individual_case_result(case_name)
    else:
        case_name = default_case_name + '/'
        get_individual_case_result(case_name)
    
    return info















def get_case_dispatch(case_name, data_find, which_nuclear):

    file_list = os.listdir(data_find+case_name)
    for file in file_list:
        if file[-6:] == "pickle": 
            case_name_open = file
            break
    with open(data_find + case_name + '/' + case_name_open, 'rb') as handle:
        [[input_case_dic,  input_tech_list,  input_time_dic],
         [results_case_dic,  results_tech_dic,  results_time_dic]] = pickle.load(handle)

    info = {}
    info['demand_potential'] = results_time_dic['demand potential']
    # Above the zero line
    info['lost_load_dispatch'] = results_time_dic['lost_load dispatch']
    info['natgas_dispatch'] = results_time_dic['natgas dispatch']
    info['natgas_ccs_dispatch'] = results_time_dic['natgas_ccs dispatch']
    info['solar_potential']  = results_time_dic['solar potential']
    info['wind_potential']   = results_time_dic['wind potential']
    info['storage_dispatch'] = results_time_dic['storage dispatch']
    info['storage_in_dispatch'] = results_time_dic['storage in dispatch']
    info['storage_stored'] = results_time_dic['storage stored']
    info['main_node_curtailment'] = results_time_dic['main_node_curtailment dispatch']

    if which_nuclear == 0:
        info['nuclear_potential'] = results_time_dic['demand potential'] * 0 + results_tech_dic['nuclear capacity'] * 0.370800284
        diff2 = (results_time_dic['heat_storage dispatch'] - results_time_dic['heat_storage in dispatch']) * 0.370800284
        diff2[diff2<=0] = 0
        info['heat_storage_dispatch'] = diff2
        diff1 = (results_time_dic['heat_storage in dispatch'] - results_time_dic['heat_storage dispatch']) * 0.370800284
        diff1[diff1<=0] = 0
        info['heat_storage_in_dispatch'] = diff1
        info['heat_storage_stored'] = results_time_dic['heat_storage stored'] * 0.370800284

    if which_nuclear == 1:
        info['nuclear_potential'] = results_time_dic['demand potential'] * 0 + results_tech_dic['conventional_nuclear capacity']
        info['heat_storage_dispatch'] = results_time_dic['demand potential'] * 0 + 0
        info['heat_storage_in_dispatch'] = results_time_dic['demand potential'] * 0 + 0
        info['heat_storage_stored'] = results_time_dic['demand potential'] * 0 + 0

    if which_nuclear == -1:
        info['nuclear_potential'] = results_time_dic['demand potential'] * 0
        info['heat_storage_dispatch'] = results_time_dic['demand potential'] * 0 + 0
        info['heat_storage_in_dispatch'] = results_time_dic['demand potential'] * 0 + 0
        info['heat_storage_stored'] = results_time_dic['demand potential'] * 0 + 0


    # Fix Storage dispatch
    total_dispatch = info['natgas_dispatch'] + \
                     info['natgas_ccs_dispatch'] + \
                     info['solar_potential'] + \
                     info['wind_potential'] + \
                     info['nuclear_potential']
    Diff3 = info['demand_potential'] - total_dispatch
    Diff3[Diff3<=0] = 0
    Diff3[Diff3> 0] = 1
    info['storage_dispatch'] = info['storage_dispatch'] * Diff3
    Diff4 = info['demand_potential'] - total_dispatch
    Diff4[Diff4<=0] = 0
    Diff5 = info['storage_dispatch'] - Diff4
    Diff5[Diff5<0] = 0
    info['storage_dispatch'] = info['storage_dispatch'] - Diff5

    if which_nuclear == 0:
        # Fix heat storage dispatch
        total_dispatch = info['natgas_dispatch'] + \
                         info['natgas_ccs_dispatch'] + \
                         info['solar_potential'] + \
                         info['wind_potential'] + \
                         info['storage_dispatch'] + \
                         info['nuclear_potential']
    
        Diff3 = info['demand_potential'] - total_dispatch
        Diff3[Diff3<=0] = 0
        Diff3[Diff3> 0] = 1
        info['heat_storage_dispatch'] = info['heat_storage_dispatch'] * Diff3

        Diff4 = info['demand_potential'] - total_dispatch
        Diff4[Diff4<=0] = 0
        Diff5 = info['heat_storage_dispatch'] - Diff4
        Diff5[Diff5<0] = 0
        info['heat_storage_dispatch'] = info['heat_storage_dispatch'] - Diff5

    # Nuclear contributions
    if which_nuclear == 0: 
        nuclear_dispatch = info['nuclear_potential'] + info['heat_storage_dispatch']
        diff = nuclear_dispatch - results_time_dic['demand potential']
        nuclear_dispatch[diff>0] = nuclear_dispatch[diff>0] - diff[diff>0]
        total_generator_dispatch = np.sum(nuclear_dispatch)
        total_demand = np.sum(results_time_dic['demand potential'])
        info['percentage'] = total_generator_dispatch / total_demand * 100
    else:
        print ('Now only consider cases with TES')
        info['percentage'] = -999
    return info




def get_data_2(case_name, data_find, which_nuclear):

    file_list = os.listdir(data_find+case_name)
    for file in file_list:
        if file[-6:] == "pickle": 
            case_name_open = file
            break
    with open(data_find + case_name + '/' + case_name_open, 'rb') as handle:
        [[input_case_dic,  input_tech_list,  input_time_dic],
         [results_case_dic,  results_tech_dic,  results_time_dic]] = pickle.load(handle)

    system_cost = results_case_dic['system_cost']
    main_node_curtailment = np.mean(results_time_dic['main_node_curtailment dispatch'])

    return system_cost, main_node_curtailment