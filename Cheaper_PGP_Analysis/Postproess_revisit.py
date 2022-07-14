import numpy as np
import pickle, os
from Postprocess_func import Get_Table, get_case_dispatch
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == "__main__":

    data_find = '/Volumes/DataCenter/MacOS_data_archive/Accepted/Duan et al. 2021_advanced nuclear/Postprocess_codes/'
    Country_list = ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']
    tech_list_Full = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load', 'pgp']

    with open('Revisit_PGP_2019.pickle', 'rb') as handle:
        Table_year2019_CheaperPGP_EIA, Table_year2019_CheaperPGP_4kd = pickle.load(handle)
    
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 
                               68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 
                               38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 
                               8,  6,  4,  2,  1, 0.1, 0.01, 0])

    # Plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]

    def nonan(input):
        input[input==0] = np.nan
        return input

    # Costs
    def plot_cost(CurrentCase, default_case_name):
        ax = plt.subplot(111)
        y_lists = [np.array(CurrentCase['natgas_tot']), 
                   np.array(CurrentCase['natgas_ccs_tot']), 
                   np.array(CurrentCase['solar_fix']), 
                   np.array(CurrentCase['wind_fix']), 
                   np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                   np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                   np.array(CurrentCase['storage_fix']),
                   np.array(CurrentCase['to_PGP_fix']) + np.array(CurrentCase['PGP_storage_fix']) + np.array(CurrentCase['from_PGP_fix']),
                   np.array(CurrentCase['lost_load_var'])]
        y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'green', 'cadetblue']

        ax.stackplot(x_axis, y_lists, colors=y_color)
        ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
        ax.set_ylabel('System cost ($/kWh)', fontsize=14)
        ax.set_title('With TES case', fontsize=18, y=1.05)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8
        ax.set_xticks( xticks )
        ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
        ax.set_xlim(0, 1)
        # ax.set_ylim(0, 0.12)
        ax.set_ylim(0, 0.10)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        plt.clf()

    for cty_idx in range(len(Country_list)):
        plot_cost(Table_year2019_CheaperPGP_EIA[cty_idx], f'Cheaper_PGP_EIA_{Country_list[cty_idx]}')
        plot_cost(Table_year2019_CheaperPGP_4kd[cty_idx], f'Cheaper_PGP_4kd_{Country_list[cty_idx]}')
