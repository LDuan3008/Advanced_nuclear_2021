import matplotlib.pyplot as plt 
import numpy as np, cdms2 as cdms, MV2 as MV, regionmask
import matplotlib
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.colors as colors
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.path as mpath


# Public variable
find_idx_list = [82, 9, 137, 29, 3, 10, 139, 32, 163, 43, 121, 59, 98, 8, 107, 141, 155, 164, 148,
                 27, 162, 72, 136, 56, 156, 31, 113, 18, 158, 25, 96, 132, 14, 110, 91, 81, 124, 112, 143, 4, 40, 94]

TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR', 'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX', 'MA',
                  'MZ','NZ','NG','PY','PE','PL','RU','SA','ZA','KR','ES','SD','SE','TH','TN','TR','UA','GB','US', 'VE','VN']

def nonan(input):
    input[input==0] = np.nan
    return input

def Scenario1Fig1_autoMake(default_case_name, summary_table):

    NumOfCases = len(summary_table)

    xlist = np.array([100, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
                  80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
                  60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
                  38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
                  16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    # xticks = np.r_[[0, 0.25, 0.5, 0.75, 1.0], xticks_addition_cov]
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]


    def plot_cost(CurrentCase, ax, x_axis, title):
        y_lists = [np.array(CurrentCase['natgas_tot']), 
                   np.array(CurrentCase['natgas_ccs_tot']), 
                   np.array(CurrentCase['solar_fix']), 
                   np.array(CurrentCase['wind_fix']), 
                   np.array(CurrentCase['conventional_nuclear_fix']), 
                   np.array(CurrentCase['storage_fix']),
                   np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                   np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                   np.array(CurrentCase['lost_load_var'])]
        y_color = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'plum', 'tomato', 'indigo', 'cadetblue']
        ax.stackplot(x_axis, y_lists, colors=y_color)
        ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
        ax.set_ylabel('System cost ($/kWh)', fontsize=14)
        ax.set_title(title, fontsize=18, y=1.05)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8

    fig = plt.figure(figsize=(12,4))
    fig.subplots_adjust(top=0.85, bottom=0.2, left=0.1, right=0.95, hspace=0.7, wspace=0.4)
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
    plot_cost(summary_table[0], ax1, x_axis, 'Conventional Nuclear')
    plot_cost(summary_table[1], ax2, x_axis, 'Low-cost advanced')
    ax1.set_xticks( xticks )
    ax1.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 0.16)
    # plt.show()
    plt.savefig(default_case_name+'_Cost.png', dpi=1500)
    # plt.savefig(default_case_name+str(idx)+'_cost.ps')
    plt.clf()


    def plot_cap(CurrentCase, ax1, ax2, x_axis, title):
        ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_cap'])), color='black')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_ccs_cap'])), color='grey')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['solar_cap'])), color='wheat')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['wind_cap'])), color='skyblue')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['conventional_nuclear_cap'])), color='brown')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_cap'])), color='tomato')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_generator_REAmatch_cap'])) +
                         nonan(np.array(CurrentCase['nuclear_generator_TESmatch_cap'])), color='limegreen')
        ax2.plot(x_axis, nonan(np.array(CurrentCase['storage_cap'])), color='violet', linestyle='--')
        ax2.plot(x_axis, nonan(np.array(CurrentCase['heat_storage_cap'])), color='indigo', linestyle='--')
        ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax1.set_xlabel('Emissions reduction constration (%)', fontsize=14)
        ax1.set_ylabel('Generation capacity (kW)', fontsize=14)
        ax2.set_ylabel('Storage capacity (kWh)', fontsize=14)
        ax1.set_title(title, fontsize=18, y=1.05)
        ax1.xaxis.labelpad = 8
        ax1.yaxis.labelpad = 8

    fig = plt.figure(figsize=(12,4))
    fig.subplots_adjust(top=0.85, bottom=0.2, left=0.1, right=0.9, hspace=0.7, wspace=0.4)
    ax1_1 = plt.subplot(121)
    ax1_2 = ax1_1.twinx()
    ax2_1 = plt.subplot(122)
    ax2_2 = ax2_1.twinx()
    ax1_1.get_shared_x_axes().join(ax1_1, ax2_1)
    ax1_1.get_shared_y_axes().join(ax1_1, ax2_1)
    ax1_1.get_shared_y_axes().join(ax1_2, ax2_2)
    plot_cap(summary_table[0], ax1_1, ax1_2, x_axis, 'Conventional Nuclear')
    plot_cap(summary_table[1], ax2_1, ax2_2, x_axis, 'Low-cost advanced')
    ax1_1.set_xticks( xticks )
    ax1_1.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    ax2_1.set_xticks( xticks )
    ax2_1.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    ax1_1.set_xlim(0, 1)
    ax1_1.set_ylim(0, 4)
    ax1_2.set_ylim(0, 5.5)
    # plt.show()
    plt.savefig(default_case_name+'_Cap.png', dpi=1500)
    # plt.savefig(default_case_name+str(idx)+'_cost.ps')
    plt.clf()



def Scenario1Fig2_autoMake(default_case_name, summary_table):

    def ReshapeData(TS, choice):
        TS_reshape = TS.reshape(-1, 24)
        if choice == 0:
            return np.mean(TS_reshape, axis=0)
        if choice == 1:
            return np.mean(TS_reshape, axis=1)
        if choice == 2:
            return np.array(TS)
    
    choice_lengh = {0:24, 1:365, 2:8760}
    choice = 1
    xaxisn = choice_lengh[choice]
    FirstDayofMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    def plot_dispatch(CurrentCase, choice, ax, title):
        ax.stackplot( np.arange(xaxisn), 
                       ReshapeData(CurrentCase['conventional_nuclear_potential'], choice), 
                       ReshapeData(CurrentCase['advanced_nuclear_potential'], choice), 
                       ReshapeData(CurrentCase['heat_storage_dispatch'], choice), 
                       ReshapeData(CurrentCase['solar_potential'], choice), 
                       ReshapeData(CurrentCase['wind_potential'], choice), 
                       ReshapeData(CurrentCase['natgas_dispatch'], choice), 
                       ReshapeData(CurrentCase['natgas_ccs_dispatch'], choice), 
                       ReshapeData(CurrentCase['storage_dispatch'], choice),
                       ReshapeData(CurrentCase['lost_load_dispatch'], choice),
                       colors = ['brown', 'tomato', 'indigo', 'wheat', 'skyblue', 'black', 'grey', 'violet', 'cadetblue'] )
        ax.plot( np.arange(xaxisn), ReshapeData(CurrentCase['demand_potential'], choice), color='black' )
        ax.set_xlabel('Days', fontsize=14)
        ax.set_ylabel('Electricity dispatch (kWh)', fontsize=14)
        ax.set_title(title, fontsize=18, y=1.05)
        ax.xaxis.labelpad = 8
        ax.yaxis.labelpad = 8

    fig = plt.figure(figsize=(12,4))
    fig.subplots_adjust(top=0.85, bottom=0.2, left=0.1, right=0.9, hspace=0.7, wspace=0.4)
    
    ax1 = plt.subplot(121)
    plot_dispatch(summary_table[0], choice, ax1, 'Conventional Nuclear')
    ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
    plot_dispatch(summary_table[1], choice, ax2, 'Low-cost advanced')
    ax1.set_xlim(0, xaxisn-1)
    ax1.set_xticks( FirstDayofMonth )
    ax1.set_xticklabels( ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
    ax1.set_ylim(0, 3.5)
    # plt.show()
    plt.savefig(default_case_name+'_Dispatch_Daily.png', dpi=1500)
    plt.clf()
