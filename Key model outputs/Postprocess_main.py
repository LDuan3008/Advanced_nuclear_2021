

if __name__ == "__main__":


    # %%
    """
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    table_AdvaNuclear_EIA,  table_ConvNuclear_EIA  = [], []
    table_AdvaNuclear_4000, table_ConvNuclear_4000 = [], []
    table_AdvaNuclear_2000, table_ConvNuclear_2000 = [], []
    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
                      'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
                      'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
                      'VE','VN']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 
                           80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 
                           40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    # new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load']
    # old_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'conventional_nuclear', 'lost_load']
    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name1 = f'U_AdvaNuclear_Year2019_{cty_idx}_Co2Cons';     table_AdvaNuclear_EIA  += [Get_Table(case_name1, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name2 = f'U_ConvNuclear_Year2019_{cty_idx}_Co2Cons';     table_ConvNuclear_EIA  += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=old_tech_lists)]
    #     case_name3 = f'U_AdvaNuclear4000_Year2019_{cty_idx}_Co2Cons'; table_AdvaNuclear_4000 += [Get_Table(case_name3, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name4 = f'U_ConvNuclear4000_Year2019_{cty_idx}_Co2Cons'; table_ConvNuclear_4000 += [Get_Table(case_name4, repeat_list = co2_cons, data_path = data_find, tech_name_list=old_tech_lists)]
    #     case_name5 = f'U_AdvaNuclear2000_Year2019_{cty_idx}_Co2Cons'; table_AdvaNuclear_2000 += [Get_Table(case_name5, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name6 = f'U_ConvNuclear2000_Year2019_{cty_idx}_Co2Cons'; table_ConvNuclear_2000 += [Get_Table(case_name6, repeat_list = co2_cons, data_path = data_find, tech_name_list=old_tech_lists)]
    # with open('Scenario1_210508.pickle', 'wb') as handle:
    #     pickle.dump([table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000], handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('Scenario1_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)
    # with open('test.pickle', 'wb') as handle:
    #     pickle.dump([table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000], handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('test.pickle', 'rb') as handle:
        # table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)

    # -------------------------------
    # --- Text in Results section ---
    # # DE and BR emission reduction level when nuclear appears;
    # def find_nonZero(var):
    #     for i in range(len(var)):
    #         if var[i] > 0:
    #             print (i, 100-co2_cons[i], var[i])
    #             break
    # for cty_idx in range(len(TwoLettersCode)):
    #     if TwoLettersCode[cty_idx] in ['DE','BR']:
    #         current_examine1 = np.array(table_AdvaNuclear_EIA[cty_idx]['nuclear_cap']).astype(float)
    #         current_examine2 = np.array(table_AdvaNuclear_4000[cty_idx]['nuclear_cap']).astype(float)
    #         print (TwoLettersCode[cty_idx])
    #         find_nonZero(current_examine1)
    #         find_nonZero(current_examine2)
    #         print ()  
    #         print () 
    
    # # System cost difference
    # SClist = []
    # for cty_idx in range(len(TwoLettersCode)):
    #     system_cost1 = table_AdvaNuclear_EIA[cty_idx]['system_cost'][-1]
    #     system_cost2 = table_AdvaNuclear_4000[cty_idx]['system_cost'][-1]
    #     diff = (system_cost2-system_cost1)/system_cost1 * 100
    #     SClist.append(diff)
    # print (min(SClist))
    # print (max(SClist))

    # # TES plus extra generator cost portion:
    # list1, list2 = [], []
    # for cty_idx in range(len(TwoLettersCode)):
    #     if TwoLettersCode[cty_idx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
    #         system_cost1 = np.array(table_AdvaNuclear_EIA[cty_idx]['system_cost']).astype(float)
    #         TES_cost1 = np.array(table_AdvaNuclear_EIA[cty_idx]['nuclear_generator_TESmatch_fix']).astype(float)
    #         GEN_cost1 = np.array(table_AdvaNuclear_EIA[cty_idx]['nuclear_generator_REAmatch_fix']).astype(float)
    #         list1.append( max( (TES_cost1/system_cost1)*100 ) )
    #         system_cost2 = np.array(table_AdvaNuclear_4000[cty_idx]['system_cost']).astype(float)
    #         TES_cost2 = np.array(table_AdvaNuclear_4000[cty_idx]['nuclear_generator_TESmatch_fix']).astype(float)
    #         GEN_cost2 = np.array(table_AdvaNuclear_4000[cty_idx]['nuclear_generator_REAmatch_fix']).astype(float)
    #         list2.append( max( (TES_cost2/system_cost2)*100 ) )
    # print ( max(list1) )
    # print ( max(list2) )
    # print ()

    # # Contribute of TES costs
    # first_flag = True
    # for cty_idx in range(len(TwoLettersCode)):
    #     # CurrentCase = table_AdvaNuclear_EIA[cty_idx]
    #     CurrentCase = table_AdvaNuclear_4000[cty_idx]
    #     system_cost = np.array(CurrentCase['system_cost'])
    #     TES_cost = np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix'])
    #     percentage_TES = TES_cost / system_cost * 100
    #     if first_flag == True:
    #         TES_percentage_list = percentage_TES / (len(TwoLettersCode))
    #         first_flag = False
    #     else:
    #         TES_percentage_list = TES_percentage_list + percentage_TES / (len(TwoLettersCode))
    # print (TES_percentage_list.max())

    # stop 
    # --- Text in Results section, end here
    # -------------------------------


    # Plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]

    def nonan(input):
        input[input==0] = np.nan
        return input

    # # Costs
    # def plot_cost(CurrentCase, default_case_name):
    #     ax = plt.subplot(111)
    #     try:
    #         y_lists = [np.array(CurrentCase['natgas_tot']), 
    #                np.array(CurrentCase['natgas_ccs_tot']), 
    #                np.array(CurrentCase['solar_fix']), 
    #                np.array(CurrentCase['wind_fix']), 
    #                np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
    #                np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
    #                np.array(CurrentCase['storage_fix']),
    #                np.array(CurrentCase['lost_load_var'])]
    #         y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']
    #     except:
    #         y_lists = [np.array(CurrentCase['natgas_tot']), 
    #                np.array(CurrentCase['natgas_ccs_tot']), 
    #                np.array(CurrentCase['solar_fix']), 
    #                np.array(CurrentCase['wind_fix']), 
    #                np.array(CurrentCase['conventional_nuclear_fix']),
    #                np.array(CurrentCase['storage_fix']),
    #                np.array(CurrentCase['lost_load_var'])]
    #         y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'plum', 'cadetblue']

    #     ax.stackplot(x_axis, y_lists, colors=y_color)
    #     ax.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
    #     ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
    #     ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
    #     ax.set_ylabel('System cost ($/kWh)', fontsize=14)
    #     ax.set_title('With TES case', fontsize=18, y=1.05)
    #     ax.xaxis.labelpad = 8
    #     ax.yaxis.labelpad = 8
    #     ax.set_xticks( xticks )
    #     ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 0.12)
    #     # plt.show()
    #     plt.savefig(default_case_name+'.ps')
    #     plt.clf()
    # for cty_idx in range(len(TwoLettersCode)):
        # if TwoLettersCode[cty_idx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
            # plot_cost(table_AdvaNuclear_EIA[cty_idx], f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')
            # plot_cost(table_AdvaNuclear_4000[cty_idx], f'Nuclear_with_TES_4000_{TwoLettersCode[cty_idx]}')
            # plot_cost(table_AdvaNuclear_2000[cty_idx], f'Nuclear_with_TES_2000_{TwoLettersCode[cty_idx]}')
            # plot_cost(table_ConvNuclear_EIA[cty_idx], f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')
            # plot_cost(table_ConvNuclear_4000[cty_idx], f'Nuclear_with_TES_4000_{TwoLettersCode[cty_idx]}')

    # # Capacity
    # def plot_capacity(CurrentCase, default_case_name):
    #     ax = plt.subplot(111)
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['natgas_cap'])), color='black')
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['natgas_ccs_cap'])), color='grey')
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['solar_cap'])), color='wheat')
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['wind_cap'])), color='skyblue')
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['nuclear_cap'])), color='tomato')
    #     ax.plot(x_axis, nonan(np.array(CurrentCase['nuclear_generator_REAmatch_cap'])) +
    #                     nonan(np.array(CurrentCase['nuclear_generator_TESmatch_cap'])), color='limegreen')
    #     ax_twin = ax.twinx()
    #     ax_twin.plot(x_axis, nonan(np.array(CurrentCase['storage_cap'])), color='violet', linestyle='--')
    #     ax_twin.plot(x_axis, nonan(np.array(CurrentCase['heat_storage_cap'])), color='indigo', linestyle='--')
    #     ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
    #     ax.set_xticks( xticks )
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 2.5)
    #     ax_twin.set_ylim(0, 8)
    #     # plt.show()
    #     plt.savefig(default_case_name+'_cap.ps')
    #     plt.clf()
    # for cty_idx in range(len(TwoLettersCode)):
    #     if TwoLettersCode[cty_idx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
    #         plot_capacity(table_AdvaNuclear_EIA[cty_idx], f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')
    #         plot_capacity(table_AdvaNuclear_4000[cty_idx], f'Nuclear_with_TES_4000_{TwoLettersCode[cty_idx]}')

    # # Emissions
    # def plot_emissions(CurrentCase, default_case_name):
    #     ax = plt.subplot(111)
    #     y_lists = [np.array(CurrentCase['natgas_emis'])/1e6, 
    #                np.array(CurrentCase['natgas_ccs_emis'])/1e6, 
    #                np.array(CurrentCase['solar_emis'])/1e6, 
    #                np.array(CurrentCase['wind_emis'])/1e6, 
    #                np.array(CurrentCase['advanced_nuclear_emis'])/1e6,
    #                np.array(CurrentCase['storage_emis'])/1e6]
    #     y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']
    #     ax.stackplot(x_axis, y_lists, colors=y_color)
    #     ax.plot(x_axis, np.zeros(len(x_axis)), color='black')
    #     ax.set_xlabel('Emissions reduction constration (%)', fontsize=14)
    #     ax.set_ylabel('Emissions (gCO2eq/kWh)', fontsize=14)
    #     ax.set_title('With TES case', fontsize=18, y=1.05)
    #     ax.xaxis.labelpad = 8
    #     ax.yaxis.labelpad = 8
    #     ax.set_xticks( xticks )
    #     ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 4.5)
    #     # plt.show()
    #     plt.savefig(default_case_name+'.ps')
    #     plt.clf()
    # for cty_idx in range(len(TwoLettersCode)):
    #     if TwoLettersCode[cty_idx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
    #         plot_emissions(table_AdvaNuclear_EIA[cty_idx], f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')

    # # Emissions all countries
    # def plot_emissions_42cty(tableIn, default_case_name):
    #     all_emissions = np.zeros([len(TwoLettersCode), len(co2_cons)])
    #     all_percentag = np.zeros(len(TwoLettersCode))
    #     for cty_idx in range(len(TwoLettersCode)):
    #         total_emissions = np.array(tableIn[cty_idx]['natgas_emis'])/1e6 + \
    #                           np.array(tableIn[cty_idx]['natgas_ccs_emis'])/1e6 + \
    #                           np.array(tableIn[cty_idx]['solar_emis'])/1e6 + \
    #                           np.array(tableIn[cty_idx]['wind_emis'])/1e6 + \
    #                           np.array(tableIn[cty_idx]['advanced_nuclear_emis'])/1e6 + \
    #                           np.array(tableIn[cty_idx]['storage_emis'])/1e6
    #         all_emissions[cty_idx] = total_emissions
    #         all_percentag[cty_idx] = total_emissions[-1]/total_emissions[0]*100

    #     print (np.max(all_percentag), np.min(all_percentag))

    #     min_emissions = np.min(all_emissions, axis=0)
    #     max_emissions = np.max(all_emissions, axis=0)
    #     ax = plt.subplot(111)
    #     ax.fill_between(x_axis, min_emissions, max_emissions, facecolor='grey')
    #     ax.set_xticks( xticks )
    #     ax.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 5)
    #     # plt.show()
    #     plt.savefig(default_case_name+'.ps')
    #     plt.clf()
    # plot_emissions_42cty(table_AdvaNuclear_EIA, 'EIA')
    # plot_emissions_42cty(table_AdvaNuclear_4000, 'c4k')

    # # Relative capacity of TES to nuclear reactor
    # def Scenario1Fig3(table_in, MaxVal):
    #     NumOfCty = len(TwoLettersCode)
    #     NumOfCas = len(co2_cons)
    #     ToDrawArray = np.zeros([NumOfCty, NumOfCas])
    #     for idx in range(NumOfCty):
    #         a1 = nonan(np.array(table_in[idx]['heat_storage_cap']))
    #         a3 = nonan(np.array(table_in[idx]['nuclear_cap']))
    #         ratio = a1/a3
    #         ToDrawArray[idx, :] = ratio
    #     Xarray, Yarray = [], []
    #     for idx in range(ToDrawArray.shape[0]):
    #         TakeCty = ToDrawArray[idx]
    #         WhereIsNan = np.isnan(TakeCty)
    #         TakeCty[WhereIsNan] = 0.0
    #         idx_max = np.argmax(ToDrawArray[idx])
    #         Xarray.append(idx+0.5)
    #         Yarray.append(idx_max+0.5)
    #     ToDrawArray = np.ma.masked_equal(ToDrawArray, 0)
    #     ax1 = plt.subplot(111)
    #     mp = ax1.pcolormesh(ToDrawArray, cmap='Reds', edgecolors='grey', linewidths='0.1', vmin=0, vmax=MaxVal)
    #     ax1.scatter(Yarray, Xarray, s=10, marker=(5, 1), edgecolors='black', linewidths='0.1')
    #     start=30; end=55
    #     ax1.set_xlim(start, end)
    #     ax1.set_xticks( np.arange(end-start)+start+0.5 )
    #     ax1.set_yticks( np.arange(ToDrawArray.shape[0])+0.5 )
    #     plt.colorbar(mp, ax=ax1, extend='max', shrink=0.8, orientation='vertical')
    #     plt.show() 
    #     # plt.savefig('test.ps') 
    #     plt.clf()
    # Scenario1Fig3(table_AdvaNuclear_EIA, 8)
    # Scenario1Fig3(table_AdvaNuclear_4000, 4)
    stop 
    # """


    """
    # --- Auto-plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
    def auto_plot_cost(table1, table2, default_case_name):
        def plot_cost(CurrentCase, ax, x_axis, type, title):
            if type == 1:
                y_lists = [np.array(CurrentCase['natgas_tot']), 
                    np.array(CurrentCase['natgas_ccs_tot']), 
                    np.array(CurrentCase['solar_fix']), 
                    np.array(CurrentCase['wind_fix']), 
                    np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                    np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                    np.array(CurrentCase['storage_fix']),
                    np.array(CurrentCase['lost_load_var'])]
                y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']
            elif type == 2:
                y_lists = [np.array(CurrentCase['natgas_tot']), 
                    np.array(CurrentCase['natgas_ccs_tot']), 
                    np.array(CurrentCase['solar_fix']), 
                    np.array(CurrentCase['wind_fix']), 
                    np.array(CurrentCase['conventional_nuclear_fix']),
                    np.array(CurrentCase['storage_fix']),
                    np.array(CurrentCase['lost_load_var'])]
                y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'plum', 'cadetblue']
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
        plot_cost(table1, ax1, x_axis, 1, 'Nuclear with TES')
        plot_cost(table2, ax2, x_axis, 2, 'Nuclear without TES')
        ax1.set_xticks( xticks )
        ax1.set_xticklabels( ['0', '80', '96', '100', '50', '90', '99'] )
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 0.16)
        # plt.show()
        plt.savefig(default_case_name+'_Cost.png', dpi=1500)
        # plt.savefig(default_case_name+str(idx)+'_cost.ps')
        plt.clf()
    for cty_idx in range(len(TwoLettersCode)):
        auto_plot_cost(table_AdvaNuclear_EIA[cty_idx],  table_ConvNuclear_EIA[cty_idx],  f'EIA_Dis{str(TwoLettersCode[cty_idx])}')
        auto_plot_cost(table_AdvaNuclear_4000[cty_idx], table_ConvNuclear_4000[cty_idx], f'C4000_Dis{str(TwoLettersCode[cty_idx])}')
        auto_plot_cost(table_AdvaNuclear_2000[cty_idx], table_ConvNuclear_2000[cty_idx], f'C2000_Dis{str(TwoLettersCode[cty_idx])}')
    """


    # %%
    """
    # Dispatch
    import numpy as np, pickle, os, matplotlib.pyplot as plt
    from Postprocess_func import get_case_dispatch
    from scipy import stats
    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    input_list1 = ['U_AdvaNuclear_Year2019_US_Co2Cons0.0', 'U_AdvaNuclear_Year2019_CN_Co2Cons0.0', 'U_AdvaNuclear_Year2019_DE_Co2Cons0.0', 
                   'U_AdvaNuclear_Year2019_ZA_Co2Cons0.0', 'U_AdvaNuclear_Year2019_AU_Co2Cons0.0', 'U_AdvaNuclear_Year2019_BR_Co2Cons0.0']
    input_list2 = ['U_ConvNuclear_Year2019_US_Co2Cons0.0', 'U_ConvNuclear_Year2019_CN_Co2Cons0.0', 'U_ConvNuclear_Year2019_DE_Co2Cons0.0', 
                   'U_ConvNuclear_Year2019_ZA_Co2Cons0.0', 'U_ConvNuclear_Year2019_AU_Co2Cons0.0', 'U_ConvNuclear_Year2019_BR_Co2Cons0.0']
    input_list3 = ['U_AdvaNuclear4000_Year2019_US_Co2Cons0.0', 'U_AdvaNuclear4000_Year2019_CN_Co2Cons0.0', 'U_AdvaNuclear4000_Year2019_DE_Co2Cons0.0', 
                   'U_AdvaNuclear4000_Year2019_ZA_Co2Cons0.0', 'U_AdvaNuclear4000_Year2019_AU_Co2Cons0.0', 'U_AdvaNuclear4000_Year2019_BR_Co2Cons0.0']
    table_withTES, table_noTES = [], []
    table4000_withTES = []
    for case_idx in range(len(input_list1)):
        table_withTES += [get_case_dispatch(input_list1[case_idx], data_find, 0)]
        table_noTES   += [get_case_dispatch(input_list2[case_idx], data_find, 1)]
        table4000_withTES   += [get_case_dispatch(input_list3[case_idx], data_find, 0)]
    # Plot
    def dispatch_plot(DicNew, default_case_name):
        def ReshapeData(TS, choice):
            TS_reshape = TS.reshape(-1, 24)
            if choice == 0: return np.mean(TS_reshape, axis=0)
            if choice == 1: return np.mean(TS_reshape, axis=1)
            if choice == 2: return np.array(TS)
        choice = 2
        choice_lengh = {0:24, 1:365, 2:8760}
        xaxisn = choice_lengh[choice]
        FirstDayofMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        for idx in range(len(DicNew)):
            plt.stackplot( np.arange(xaxisn), 
                ReshapeData(DicNew[idx]['nuclear_potential'], choice), 
                ReshapeData(DicNew[idx]['heat_storage_dispatch'], choice), 
                ReshapeData(DicNew[idx]['solar_potential'], choice), 
                ReshapeData(DicNew[idx]['wind_potential'], choice), 
                ReshapeData(DicNew[idx]['natgas_dispatch'], choice), 
                ReshapeData(DicNew[idx]['natgas_ccs_dispatch'], choice), 
                ReshapeData(DicNew[idx]['storage_dispatch'], choice),
                ReshapeData(DicNew[idx]['lost_load_dispatch'], choice),
                colors = ['tomato', 'indigo', 'wheat', 'skyblue', 'black', 'grey', 'violet', 'cadetblue'] )
            plt.plot( np.arange(xaxisn), ReshapeData(DicNew[idx]['demand_potential'], choice), color='black' )

            # plt.xlim(0, xaxisn-1)
            # plt.xticks(FirstDayofMonth)
            # plt.xlim(15*24, 20*24)
            # plt.xticks([15*24, 16*24, 17*24, 18*24, 19*24, 20*24])
            plt.xlim((181+15)*24, (181+20)*24)
            plt.xticks([4704, 4728, 4752, 4776, 4800, 4824])

            plt.ylim(0, 3.5)
            plt.yticks([0, 0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5])
            # plt.show() 
            plt.savefig(f'{default_case_name}_Dispatch'+str(idx)+'.ps')
            plt.clf()
    dispatch_plot(table_withTES, 'EIA_WithTES')
    # dispatch_plot(table_noTES, 'EIA_NoTES')
    dispatch_plot(table4000_withTES, 'C4000_WithTES')
    # """


    # %%
    """
    # Table S2
    import numpy as np, regionmask, cdms2 as cdms, MV2 as MV
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt
    #------------------------------------ Table S2
    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR','DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA','KR','ES','SD','SE','TH','TN','TR','UA','GB','US','VE','VN']

    def showTableS2(dict, DicNew):

        xlist = np.array([100, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0, 80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
                         60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0, 38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
                         16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0])
        ylist = 100 - xlist

        f_axis = cdms.open('SWGDN.nc')
        v=f_axis('SWGDN')
        lat, lon=v.getAxis(1), v.getAxis(2)
        bounds_lat = lat.getBounds() 
        bounds_lon = lon.getBounds() 
        f_axis.close()
        world_countries_array = regionmask.defined_regions.natural_earth.countries_110
        mask = np.array(world_countries_array.mask(lon, lat, wrap_lon=False))
        name = world_countries_array.names
        f_land_mask = cdms.open('land_sea_mask_merra.nc4')
        ocean_mask = f_land_mask('FROCEAN',squeeze=1)
        ocean_mask[ocean_mask>=0.5] = 1.
        ocean_mask[ocean_mask<0.5]  = 0.
        f_land_mask.close()

        R_earth = 6.371*10**6
        cell_areas = np.zeros((len(lat),len(lon)))
        for ii in range(len(lat)):
            for jj in range(len(lon)):
                cell_areas[ii,jj] = 2*np.pi*R_earth**2*np.absolute(np.sin(bounds_lat[ii,1]*np.pi/180)-np.sin(bounds_lat[ii,0]*np.pi/180))*np.absolute(bounds_lon[jj,1]-bounds_lon[jj,0])/360
        tot_area_list = []
        for idx_idx in range(len(find_idx_list)):
            new_mask = np.copy(mask)
            mask_new = MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
            total_area = np.sum(mask_new*cell_areas)
            tot_area_list.append(total_area)

        tot_cty = len(dict)
        new_array_outputs = np.zeros([42, 13])
        for cty_idx in range(tot_cty):
            current_info = dict[cty_idx]
            tota_a = tot_area_list[cty_idx] / 1e6
            mean_s = np.mean(current_info['solar series'])
            std_s  = np.std(current_info['solar series'])
            mean_w = np.mean(current_info['wind series'])
            std_w  = np.std(current_info['wind series'])
            # When start using Nuclear;
            for sub_idx in range(len(ylist)):
                if current_info['nuclear_cap'][sub_idx] > 0:
                    find_n = current_info['nuclear_cap'][sub_idx]
                    find_c = ylist[sub_idx]
                    break
            find_05x = -1
            for sub_idx in range(len(ylist)):
                if current_info['nuclear_cap'][sub_idx] > 0.5:
                    find_05x = ylist[sub_idx]
                    break
            find_99x = -1
            for sub_idx in range(len(ylist)):
                if current_info['nuclear_cap'][sub_idx] > 0.99:
                    find_99x = ylist[sub_idx]
                    break
            new_array_outputs[cty_idx, 0] = tota_a
            new_array_outputs[cty_idx, 1] = mean_s
            new_array_outputs[cty_idx, 2] = std_s
            new_array_outputs[cty_idx, 3] = mean_w
            new_array_outputs[cty_idx, 4] = std_w
            new_array_outputs[cty_idx, 5] = find_n
            new_array_outputs[cty_idx, 6] = find_c
            new_array_outputs[cty_idx, 7] = find_05x
            new_array_outputs[cty_idx, 8] = find_99x
        # TableS2_showTableS2_1_210508: EIA cost
        # TableS2_showTableS2_2_210508: $4000/kW cost
        import pickle
        with open('TableS2_showTableS2_1_210508.pickle', 'wb') as handle:
            pickle.dump(new_array_outputs, handle, protocol=pickle.HIGHEST_PROTOCOL)



    # # Dispatch percentage
    # DicNew = [] 
    # for idx1 in range(len(TwoLettersCode)):
    #     cty_name = TwoLettersCode[idx1]
    #     print (cty_name)
    #     DicCty = []
    #     for idx2 in range(len(co2_cons)):
    #         co2_name = co2_cons[idx2]
    #         case_name = 'U_AdvaNuclear_Year2019_' + cty_name + '_Co2Cons' + str(co2_name) + '/'
    #         DicCty.append(get_case_dispatch(case_name, data_find, 0)['percentage'])
    #     DicNew += [DicCty]
    # with open('TableS2_210508.pickle', 'wb') as handle:
    #     pickle.dump(DicNew, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    # with open('Scenario1_210508.pickle', 'rb') as handle:
    #     table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)
    # with open('TableS2_210508.pickle', 'rb') as handle:
    #     DicNew = pickle.load(handle)
    # from Postprocess_fig import showTableS2 # Remember to change the pickle file name
    # showTableS2(table_AdvaNuclear_EIA, DicNew)
    # # showTableS2(table_AdvaNuclear_4000, DicNew)
    # stop 
    
    with open('TableS2_showTableS2_1_210508.pickle', 'rb') as handle:
        arr1 = pickle.load(handle)
    with open('TableS2_showTableS2_2_210508.pickle', 'rb') as handle:
        arr2 = pickle.load(handle)

    np.savetxt("TableS2_1.csv", arr1, fmt='%.5f', delimiter=",")
    np.savetxt("TableS2_2.csv", arr2, fmt='%.5f', delimiter=",")

    

    # # Only wind and base data
    # size = arr1[:, 0]
    # ax1=plt.subplot(111)
    # ax1.scatter(arr1[:, 6], arr1[:, 3], c='firebrick', s=size/1e4, edgecolors='black', linewidths=0.1, alpha=0.8)
    # # ax1.scatter(arr2[:, 6], arr2[:, 3], c='royalblue', s=size/1e4, edgecolors='black', linewidths=0.1, alpha=0.8)
    # ax1.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    # ax1.set_xlim(-5, 100)
    # ax1.set_ylim(0, 0.6)
    # plt.savefig('EIA.ps') 
    # # plt.savefig('C4000.ps') 
    # plt.clf()

    # # For SI figure
    # def plotSI(new_array_outputs, name):
    #     size = new_array_outputs[:, 0]
    #     scale = 1e5
    #     ax1=plt.subplot(321)
    #     ax1.scatter(new_array_outputs[:, 6], new_array_outputs[:, 3], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax1.scatter(new_array_outputs[:, 7], new_array_outputs[:, 3], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax1.scatter(new_array_outputs[:, 8], new_array_outputs[:, 3], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax1.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    #     ax2=plt.subplot(322, sharex=ax1, sharey=ax1)
    #     ax2.scatter(new_array_outputs[:, 6], new_array_outputs[:, 1], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax2.scatter(new_array_outputs[:, 7], new_array_outputs[:, 1], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax2.scatter(new_array_outputs[:, 8], new_array_outputs[:, 1], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax2.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    #     ax1.set_xlim(-5, 105)
    #     ax1.set_ylim(0, 0.6)
    #     ax3=plt.subplot(323) 
    #     ax3.scatter(new_array_outputs[:, 6], new_array_outputs[:, 4], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax3.scatter(new_array_outputs[:, 7], new_array_outputs[:, 4], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax3.scatter(new_array_outputs[:, 8], new_array_outputs[:, 4], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax3.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    #     ax4=plt.subplot(324, sharex=ax3, sharey=ax3)
    #     ax4.scatter(new_array_outputs[:, 6], new_array_outputs[:, 2], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax4.scatter(new_array_outputs[:, 7], new_array_outputs[:, 2], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax4.scatter(new_array_outputs[:, 8], new_array_outputs[:, 2], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax4.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    #     ax3.set_xlim(-5, 105)
    #     ax3.set_ylim(0, 0.6)
    #     ax5=plt.subplot(325) 
    #     ax5.scatter(new_array_outputs[:, 6], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax5.scatter(new_array_outputs[:, 7], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax5.scatter(new_array_outputs[:, 8], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax5.plot(np.r_[0, 0], np.r_[0.0, 1.5], color='black', linestyle='--', linewidth='1')
    #     ax6=plt.subplot(326, sharex=ax5, sharey=ax5)
    #     ax6.scatter(new_array_outputs[:, 6], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax6.scatter(new_array_outputs[:, 7], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax6.scatter(new_array_outputs[:, 8], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    #     ax6.plot(np.r_[0, 0], np.r_[0.0, 1.5], color='black', linestyle='--', linewidth='1')
    #     ax5.set_xlim(-5, 105)
    #     ax5.set_ylim(0, 1.5)
    #     # plt.show() 
    #     plt.savefig(name+'.ps', dpi=2000) 
    #     plt.clf()
    # plotSI(arr1, 'EIA')
    # plotSI(arr2, 'C4000')
    # """




    # %%
    """
    # Impact of TES on renewables
    import MV2 as MV, pickle
    import numpy as np, cdms2 as cdms, MV2 as MV, regionmask
    import matplotlib
    import matplotlib.pyplot as plt 
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import matplotlib.colors as colors
    import matplotlib as mpl
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.path as mpath

    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR','DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA','KR','ES','SD','SE','TH','TN','TR','UA','GB','US','VE','VN']
    find_idx_list = [82, 9, 137, 29, 3, 10, 139, 32, 163, 43, 121, 59, 98, 8, 107, 141, 155, 164, 148,
                 27, 162, 72, 136, 56, 156, 31, 113, 18, 158, 25, 96, 132, 14, 110, 91, 81, 124, 112, 143, 4, 40, 94]
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])

    with open('Scenario1_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)


    # -------------------------------------------------------------
    # Text starts here:
    ChangeEIA_100p, ChangeEIA_99p = [], []
    ChangeC4K_100p, ChangeC4K_99p = [], []
    for idx in range(len(TwoLettersCode)):
        sys_cos_EIA1 = np.array(table_AdvaNuclear_EIA[idx]['system_cost']).astype(float)
        sys_cos_EIA2 = np.array(table_ConvNuclear_EIA[idx]['system_cost']).astype(float)
        sys_cos_EIA3 = np.array(table_AdvaNuclear_4000[idx]['system_cost']).astype(float)
        sys_cos_EIA4 = np.array(table_ConvNuclear_4000[idx]['system_cost']).astype(float)
        change1 = (sys_cos_EIA2 - sys_cos_EIA1) / sys_cos_EIA1 * 100; ChangeEIA_100p.append(change1[-1]); ChangeEIA_99p.append(change1[-5])
        change2 = (sys_cos_EIA4 - sys_cos_EIA3) / sys_cos_EIA3 * 100; ChangeC4K_100p.append(change2[-1]); ChangeC4K_99p.append(change2[-5])
    print (np.max(ChangeEIA_100p))
    print (np.max(ChangeEIA_99p))
    print (np.max(ChangeC4K_100p))
    print (np.max(ChangeC4K_99p))

    output_array = np.zeros([len(TwoLettersCode), 4])
    output_array[:,0] = ChangeEIA_100p
    output_array[:,1] = ChangeEIA_99p
    output_array[:,2] = ChangeC4K_100p
    output_array[:,3] = ChangeC4K_99p
    np.savetxt("Table_S3.csv", output_array, fmt='%.5f', delimiter=",")
    stop 






    # Text ends here
    # -------------------------------------------------------------
    
    
    total_check = 42
    solar1, wind1, nuclear1 = np.zeros(total_check), np.zeros(total_check), np.zeros(total_check)
    solar2, wind2, nuclear2 = np.zeros(total_check), np.zeros(total_check), np.zeros(total_check)
    case_idx = 0
    Consider_Case_Idx = -5
    compare_case1 = table_AdvaNuclear_EIA
    compare_case2 = table_ConvNuclear_EIA
    for CtyIdx in range(len(TwoLettersCode)):
        if total_check == 6:
            if TwoLettersCode[CtyIdx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
                solar1[case_idx], wind1[case_idx], nuclear1[case_idx] = compare_case1[CtyIdx]['solar_cap'][Consider_Case_Idx], compare_case1[CtyIdx]['wind_cap'][Consider_Case_Idx], compare_case1[CtyIdx]['nuclear_cap'][Consider_Case_Idx]
                solar2[case_idx], wind2[case_idx], nuclear2[case_idx] = compare_case2[CtyIdx]['solar_cap'][Consider_Case_Idx], compare_case2[CtyIdx]['wind_cap'][Consider_Case_Idx], compare_case2[CtyIdx]['conventional_nuclear_cap'][Consider_Case_Idx]
                case_idx += 1
        else:
            solar1[case_idx], wind1[case_idx], nuclear1[case_idx] = compare_case1[CtyIdx]['solar_cap'][Consider_Case_Idx], compare_case1[CtyIdx]['wind_cap'][Consider_Case_Idx], compare_case1[CtyIdx]['nuclear_cap'][Consider_Case_Idx]
            solar2[case_idx], wind2[case_idx], nuclear2[case_idx] = compare_case2[CtyIdx]['solar_cap'][Consider_Case_Idx], compare_case2[CtyIdx]['wind_cap'][Consider_Case_Idx], compare_case2[CtyIdx]['conventional_nuclear_cap'][Consider_Case_Idx]
            case_idx += 1

    # The bar plot here:
    # plt.bar(np.arange(total_check)-0.1, solar1-solar2, width=0.1)
    # plt.bar(np.arange(total_check)+0.0, wind1-wind2, width=0.1)
    # plt.bar(np.arange(total_check)+0.1, nuclear1-nuclear2, width=0.1)
    # plt.plot(np.r_[-0.4, 5.4], np.r_[0, 0], color='black', linestyle='--', linewidth=1)
    # plt.xlim(-0.4, 5.4)
    # plt.ylim(-0.6, 0.8)
    # plt.show()  
    # plt.clf()
    # stop 


    # Get country size here:
    with open('TableS2_showTableS2_1_210508.pickle', 'rb') as handle:
        arr1 = pickle.load(handle)
    size = arr1[:, 0]

    # ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
    # ax1.scatter(nuclear1 - nuclear2, (wind1+solar1) - (wind2+solar2), c='firebrick', edgecolor='black', s=size/3e4, alpha=0.7)
    # # ax1.scatter(nuclear1 - nuclear2, wind1 - wind2, c='firebrick', edgecolor='black', s=size/3e4, alpha=0.7)
    # # ax1.scatter(nuclear1 - nuclear2, solar1 - solar2, c='firebrick', edgecolor='black', s=size/3e4, alpha=0.7)
    # ax1.plot(np.r_[-0.4, 0.2], np.r_[0, 0], color='black', linestyle='--', linewidth=0.5)
    # ax1.plot(np.r_[0, 0], np.r_[-1.0, 1.0], color='black', linestyle='--', linewidth=0.5)
    # ax1.set_xlim(-0.4, 0.2)
    # ax1.set_ylim(-1.0, 1.0)
    # plt.show() 
    # # plt.savefig('test.ps') 
    # plt.clf()
    # stop 

    # The map plot here:
    f_axis = cdms.open('SWGDN.nc')
    v=f_axis('SWGDN')
    lat, lon=v.getAxis(1), v.getAxis(2)
    f_axis.close()
    world_countries_array = regionmask.defined_regions.natural_earth.countries_110
    mask = np.array(world_countries_array.mask(lon, lat, wrap_lon=False))
    f_land_mask = cdms.open('land_sea_mask_merra.nc4')
    ocean_mask = f_land_mask('FROCEAN',squeeze=1)
    ocean_mask[ocean_mask>=0.5] = 1.
    ocean_mask[ocean_mask<0.5]  = 0.
    f_land_mask.close()
    Consider_Case_Idx = -5
    # compare_case1 = table_AdvaNuclear_EIA
    # compare_case2 = table_ConvNuclear_EIA
    compare_case1 = table_AdvaNuclear_4000
    compare_case2 = table_ConvNuclear_4000
    total_mask_solar = np.zeros([len(lat), len(lon)])
    mask_array = np.zeros([len(lat), len(lon)]) # masked no data regions
    for CtyIdx in range(len(TwoLettersCode)):
        new_mask = np.copy(mask)
        mask_new = MV.filled(MV.masked_not_equal(new_mask, find_idx_list[CtyIdx]) * 0. + 1, 0)
        Rews1 = compare_case1[CtyIdx]['solar_cap'][Consider_Case_Idx] + compare_case1[CtyIdx]['wind_cap'][Consider_Case_Idx]
        Rews2 = compare_case2[CtyIdx]['solar_cap'][Consider_Case_Idx] + compare_case2[CtyIdx]['wind_cap'][Consider_Case_Idx]
        RewsD = Rews1 - Rews2
        total_mask_solar = total_mask_solar + RewsD * mask_new
        mask_array = mask_array + MV.filled(MV.masked_not_equal(new_mask, find_idx_list[CtyIdx]) * 0. + 1, 0)
    mask_array_new = np.ma.masked_equal(mask_array + ocean_mask, 1)

    
    # def plotP(var, col, name):
    #     ax1 = plt.subplot(111, projection=ccrs.PlateCarree())
    #     ax1.add_feature(cfeature.COASTLINE)
    #     ax1.add_feature(cfeature.BORDERS)
    #     ax1.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())
    #     mp = ax1.pcolor(lon, lat, np.ma.masked_equal(var, 0), cmap=col, norm=colors.Normalize(vmin=-1, vmax=1), transform=ccrs.PlateCarree())
    #     ax1.contourf(lon, lat, mask_array_new, colors='none', hatches=['.'*5], transform=ccrs.PlateCarree())
    #     plt.colorbar(mp, ax=ax1, extend='both', shrink=0.5, orientation='vertical')
    #     # plt.show()
    #     # plt.savefig(name+'.png', dpi=1500)
    #     plt.savefig(name+'.ps')
    #     plt.clf()
    # plotP(total_mask_solar, 'bwr', 'TestC400099p')

    stop  

    # """





    # %%
    """
    # Examine the impact of dispatch-ability of nuclear
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    table_AdvaNuclear_EIA,  table_ConvNuclear_EIA  = [], []
    table_AdvaNuclear_4000, table_ConvNuclear_4000 = [], []
    table_AdvaNuclear_2000, table_ConvNuclear_2000 = [], []
    TwoLettersCode = ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load']
    
    # table_AdvaNuclear_EIA, table_AdvaNuclear_EIA_NoCurtNucl = [], []
    # table_AdvaNuclear_c4k, table_AdvaNuclear_c4k_NoCurtNucl = [], []
    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name1 = f'U_AdvaNuclear_Year2019_{cty_idx}_Co2Cons';                 table_AdvaNuclear_EIA            += [Get_Table(case_name1, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name2 = f'AdvaNuclear_NoCurtailment_Year2019_{cty_idx}_Co2Cons';     table_AdvaNuclear_EIA_NoCurtNucl += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name3 = f'U_AdvaNuclear4000_Year2019_{cty_idx}_Co2Cons';             table_AdvaNuclear_c4k            += [Get_Table(case_name3, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name4 = f'AdvaNuclear4000_NoCurtailment_Year2019_{cty_idx}_Co2Cons'; table_AdvaNuclear_c4k_NoCurtNucl += [Get_Table(case_name4, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario2_210508.pickle', 'wb') as handle:
    #     pickle.dump([table_AdvaNuclear_EIA, table_AdvaNuclear_EIA_NoCurtNucl, table_AdvaNuclear_c4k, table_AdvaNuclear_c4k_NoCurtNucl], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario2_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA, table_AdvaNuclear_EIA_NoCurtNucl, table_AdvaNuclear_c4k, table_AdvaNuclear_c4k_NoCurtNucl = pickle.load(handle)

    # Plot here
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]
    
    def plot_cost(CurrentCase, default_case_name):
        ax = plt.subplot(111)
        y_lists = [np.array(CurrentCase['natgas_tot']), 
                   np.array(CurrentCase['natgas_ccs_tot']), 
                   np.array(CurrentCase['solar_fix']), 
                   np.array(CurrentCase['wind_fix']), 
                   np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                   np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                   np.array(CurrentCase['storage_fix']),
                   np.array(CurrentCase['lost_load_var'])]
        y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']
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
        ax.set_ylim(0, 0.10)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        plt.clf()
    for cty_idx in range(len(TwoLettersCode)):
        plot_cost(table_AdvaNuclear_EIA[cty_idx], f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')
        plot_cost(table_AdvaNuclear_EIA_NoCurtNucl[cty_idx], f'Nuclear_with_TES_EIA_NoCur_{TwoLettersCode[cty_idx]}')
        plot_cost(table_AdvaNuclear_c4k[cty_idx], f'Nuclear_with_TES_C4K_{TwoLettersCode[cty_idx]}')
        plot_cost(table_AdvaNuclear_c4k_NoCurtNucl[cty_idx], f'Nuclear_with_TES_C4K_NoCur_{TwoLettersCode[cty_idx]}')
    # """


    # %%
    """
    # Examine the impact of free-resistent-heater
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    TwoLettersCode = ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load', 'Resistant Heater']
    
    # table_AdvaNuclear_EIA_FreeResi = []
    # table_AdvaNuclear_c4k_FreeResi = []
    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name2 = f'AdvaNuclear_FreeResisHeat_Year2019_{cty_idx}_Co2Cons';     table_AdvaNuclear_EIA_FreeResi += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name4 = f'AdvaNuclear4000_FreeResisHeat_Year2019_{cty_idx}_Co2Cons'; table_AdvaNuclear_c4k_FreeResi += [Get_Table(case_name4, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario3_210508.pickle', 'wb') as handle:
    #     pickle.dump([table_AdvaNuclear_EIA_FreeResi, table_AdvaNuclear_c4k_FreeResi], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario3_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA_FreeResi, table_AdvaNuclear_c4k_FreeResi = pickle.load(handle)

    # Plot here
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]

    def nonan(input):
        input[input==0] = np.nan
        return input
    
    def plot_cost(CurrentCase, default_case_name):
        ax1 = plt.subplot(111)
        ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_cap'])), color='black')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_ccs_cap'])), color='grey')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['solar_cap'])), color='wheat')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['wind_cap'])), color='skyblue')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_cap'])), color='tomato')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_generator_REAmatch_cap'])) +
                         nonan(np.array(CurrentCase['nuclear_generator_TESmatch_cap'])), color='limegreen')
        ax1.plot(x_axis, nonan(np.array(CurrentCase['Resistant Heater_cap'])), color='darkblue')
        ax2 = ax1.twinx()
        ax2.plot(x_axis, nonan(np.array(CurrentCase['storage_cap'])), color='violet', linestyle='--')
        ax2.plot(x_axis, nonan(np.array(CurrentCase['heat_storage_cap'])), color='indigo', linestyle='--')
        ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax1.set_xticks( xticks )
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 2.5)
        ax2.set_ylim(0, 8)
        # plt.show()
        plt.savefig(default_case_name+'_cap.ps')
        plt.clf()

    for cty_idx in range(len(TwoLettersCode)):
        plot_cost(table_AdvaNuclear_EIA_FreeResi[cty_idx], f'EIA_FreeResi_{TwoLettersCode[cty_idx]}')
        plot_cost(table_AdvaNuclear_c4k_FreeResi[cty_idx], f'c4k_FreeResi_{TwoLettersCode[cty_idx]}')
    # """



    # %%
    """
    # Multiple-counties and multiple-years
    import numpy as np, cdms2 as cdms, MV2 as MV
    import pickle, os, regionmask
    from Postprocess_func import Get_Table
    import matplotlib
    import matplotlib.pyplot as plt 
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import matplotlib.colors as colors
    import matplotlib as mpl
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.path as mpath

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR','DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA','KR','ES','SD','SE','TH','TN','TR','UA','GB','US','VE','VN']
    year_list = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
                 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load']

    # Get Results first
    EIA_1e24, EIA_50, EIA_99 = [], [], []
    C4K_1e24, C4K_50, C4K_99 = [], [], []
    for cty_idx in TwoLettersCode:
        print (cty_idx)
        dividing_point1 = len('U_AdvaNuclear_Year');     case_name1 = f'U_AdvaNuclear_Year_{cty_idx}_Co2Cons50';     EIA_50 += [Get_Table(case_name1, repeat_list = year_list, data_path = data_find, dividing_name_point = dividing_point1, tech_name_list=new_tech_lists)]
        dividing_point2 = len('U_AdvaNuclear4000_Year'); case_name2 = f'U_AdvaNuclear4000_Year_{cty_idx}_Co2Cons50'; C4K_50 += [Get_Table(case_name2, repeat_list = year_list, data_path = data_find, dividing_name_point = dividing_point2, tech_name_list=new_tech_lists)]
        dividing_point3 = len('U_AdvaNuclear_Year');     case_name3 = f'U_AdvaNuclear_Year_{cty_idx}_Co2Cons1';      EIA_99 += [Get_Table(case_name3, repeat_list = year_list, data_path = data_find, dividing_name_point = dividing_point3, tech_name_list=new_tech_lists)]
        dividing_point4 = len('U_AdvaNuclear4000_Year'); case_name4 = f'U_AdvaNuclear4000_Year_{cty_idx}_Co2Cons1';  C4K_99 += [Get_Table(case_name4, repeat_list = year_list, data_path = data_find, dividing_name_point = dividing_point4, tech_name_list=new_tech_lists)]
    with open('Scenario4_210508.pickle', 'wb') as handle:
        pickle.dump([EIA_50, EIA_99, C4K_50, C4K_99], handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('Scenario4_210508.pickle', 'rb') as handle:
    #     EIA_50, EIA_99, C4K_50, C4K_99 = pickle.load(handle)


    # Numbers in text
    solar_cap = []
    wind_cap = []
    nuclear_cap = []
    for idx in range(42):
        solar_cap.append(np.mean(EIA_99[idx]['solar_cap']))
        wind_cap.append(np.mean(EIA_99[idx]['wind_cap']))
        nuclear_cap.append(np.mean(EIA_99[idx]['nuclear_cap']))
    sp = np.array(solar_cap)
    wp = np.array(wind_cap)
    nu = np.array(nuclear_cap)
    print (np.mean(sp), np.mean(wp), np.mean(nu))
    nu[nu>0]=1
    print (np.sum(nu)/42*100)
    stop 

    # tech_name_list = ['natgas', 'natgas_fixed', 'natgas_ccs', 'natgas_ccs_fixed', 'solar', 'solar_fixed', 'wind', 'wind_fixed', 'storage', 'storage_fixed', 'lost_load', 'advanced_nuclear', 'advanced_nuclear_fixed']
    # SummaryTable_eia_50to99 = []
    # SummaryTable_c4k_50to99 = []
    # for country_idx in TwoLettersCode:
    #     print (country_idx)
    #     case_name1 = 'zzzto99_U_AdvaNuclear_Year' + '_' + country_idx + '_Co2Cons50'
    #     dividing_point1 = len('zzzto99_U_AdvaNuclear_Year') 
    #     SummaryTable_eia_50to99 += [Get_Table(case_name1, repeat_list = year_list, dividing_name_point = dividing_point1, data_path = data_find, tech_name_list = tech_name_list)]
    #     case_name2 = 'zzzto99_U_AdvaNuclear4000_Year' + '_' + country_idx + '_Co2Cons50'
    #     dividing_point2 = len('zzzto99_U_AdvaNuclear4000_Year') 
    #     SummaryTable_c4k_50to99 += [Get_Table(case_name2, repeat_list = year_list, dividing_name_point = dividing_point2, data_path = data_find, tech_name_list = tech_name_list)]
    # with open('Scenario5_210508.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable_eia_50to99, SummaryTable_c4k_50to99], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario5_210508.pickle', 'rb') as handle:
        SummaryTable_eia_50to99, SummaryTable_c4k_50to99 = pickle.load(handle)

    info = {}
    totctys, totyears, totcase = len(TwoLettersCode), len(year_list), 6
    def InitialArray(info, NameArray, totctys, totcase):
        for name_idx in NameArray:
            info[name_idx] = np.zeros([totctys, totcase, 2])
    NameList1 = ['natgas_cap', 'natgas_ccs_cap', 'solar_cap', 'wind_cap', 'storage_cap', 'nuclear_cap', 'heat_storage_cap', 'nuclear_generator_REAmatch_cap', 'nuclear_generator_TESmatch_cap']
    InitialArray(info, NameList1, totctys, totcase)
    NameList2 = ['natgas_fixed_cap', 'natgas_ccs_fixed_cap', 'solar_fixed_cap', 'wind_fixed_cap', 'storage_fixed_cap', 'nuclear_fixed_cap', 'heat_storage_fixed_cap', 'nuclear_generator_fixed_REAmatch_cap', 'nuclear_generator_fixed_TESmatch_cap']
    InitialArray(info, NameList2, totctys, totcase)
    info['co2_emi'] = np.zeros([totctys, totcase])
    info['sys_cos'] = np.zeros([totctys, totcase])
    def PartitionResults(info, NameList, SummaryTable, ScenarioIdx, type='base'):
        def cal_mean_std(array, series, idx, ScenarioIdx):
            array[idx, ScenarioIdx, 0] = np.mean(series)
            array[idx, ScenarioIdx, 1] = np.std(series)
        for idx in range(totctys):
            CtyList = SummaryTable[idx]
            info['co2_emi'][idx, ScenarioIdx] = np.mean(CtyList['co2_emissions'])
            info['sys_cos'][idx, ScenarioIdx] = np.mean(CtyList['system_cost'])
            for name_idx in NameList:
                cal_mean_std(info[name_idx], CtyList[name_idx], idx, ScenarioIdx)
    PartitionResults(info, NameList1, EIA_50, 0)
    PartitionResults(info, NameList1, EIA_99, 1)
    PartitionResults(info, NameList1, C4K_50, 2)
    PartitionResults(info, NameList1, C4K_99, 3)
    PartitionResults(info, np.r_[NameList1, NameList2], SummaryTable_eia_50to99, 4)
    PartitionResults(info, np.r_[NameList1, NameList2], SummaryTable_c4k_50to99, 5)


    # # Map plot
    # f_axis = cdms.open('SWGDN.nc')
    # v=f_axis('SWGDN')
    # lat, lon=v.getAxis(1), v.getAxis(2)
    # f_axis.close()
    # world_countries_array = regionmask.defined_regions.natural_earth.countries_110
    # mask = np.array(world_countries_array.mask(lon, lat, wrap_lon=False))
    # f_land_mask = cdms.open('land_sea_mask_merra.nc4')
    # ocean_mask = f_land_mask('FROCEAN',squeeze=1)
    # ocean_mask[ocean_mask>=0.5] = 1.
    # ocean_mask[ocean_mask<0.5]  = 0.
    # f_land_mask.close()
    # def plotP(var, col, name):
    #     ax1 = plt.subplot(111, projection=ccrs.PlateCarree())
    #     ax1.add_feature(cfeature.COASTLINE)
    #     ax1.add_feature(cfeature.BORDERS)
    #     ax1.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())
    #     mp = ax1.pcolor(lon, lat, np.ma.masked_equal(var, 0), cmap=col, norm=colors.Normalize(vmin=0, vmax=1.5), transform=ccrs.PlateCarree())
    #     ax1.contourf(lon, lat, mask_array_new, colors='none', hatches=['.'*5], transform=ccrs.PlateCarree())
    #     plt.colorbar(mp, ax=ax1, extend='max', shrink=0.5, orientation='vertical')
    #     # plt.show()
    #     plt.savefig(name+'.ps')
    #     plt.clf()
    # check_case_list = [0, 1, 2, 3]
    # find_idx_list = [82, 9, 137, 29, 3, 10, 139, 32, 163, 43, 121, 59, 98, 8, 107, 141, 155, 164, 148, 27, 162, 72, 136, 56, 156, 31, 113, 18, 158, 25, 96, 132, 14, 110, 91, 81, 124, 112, 143, 4, 40, 94]
    # for CaseIdx in check_case_list:
    #     map_plot_co2emit = info['natgas_cap'][:, CaseIdx, 0] + info['natgas_ccs_cap'][:, CaseIdx, 0]
    #     map_plot_solar   = info['solar_cap'][:, CaseIdx, 0]
    #     map_plot_wind    = info['wind_cap'][:, CaseIdx, 0]
    #     map_plot_nuclear = info['nuclear_cap'][:, CaseIdx, 0]
    #     map_plot_storage = info['heat_storage_cap'][:, CaseIdx, 0] + info['storage_cap'][:, CaseIdx, 0]
    #     total_mask_co2emitting = np.zeros([len(lat), len(lon)])
    #     total_mask_solar = np.zeros([len(lat), len(lon)])
    #     total_mask_wind = np.zeros([len(lat), len(lon)])
    #     total_mask_heat_source = np.zeros([len(lat), len(lon)])
    #     total_mask_all_storage = np.zeros([len(lat), len(lon)])
    #     mask_array = np.zeros([len(lat), len(lon)]) # masked no data regions
    #     for idx_idx in range(len(find_idx_list)):
    #         new_mask = np.copy(mask)
    #         mask_new = MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
    #         total_mask_co2emitting = total_mask_co2emitting + map_plot_co2emit[idx_idx] * mask_new
    #         total_mask_solar       = total_mask_solar       + map_plot_solar[idx_idx]   * mask_new
    #         total_mask_wind        = total_mask_wind        + map_plot_wind[idx_idx]    * mask_new
    #         total_mask_heat_source = total_mask_heat_source + map_plot_nuclear[idx_idx] * mask_new
    #         total_mask_all_storage = total_mask_all_storage + map_plot_storage[idx_idx] * mask_new
    #         mask_array = mask_array + MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
    #     mask_array_new = np.ma.masked_equal(mask_array + ocean_mask, 1)
    #     plotP(total_mask_co2emitting, 'Greys', 'natgasMAP_'+str(CaseIdx)) 
    #     plotP(total_mask_solar, 'Reds', 'solarMAP_'+str(CaseIdx)) 
    #     plotP(total_mask_wind, 'Blues', 'windMAP_'+str(CaseIdx)) 
    #     plotP(total_mask_heat_source, 'Oranges', 'nuclearMAP_'+str(CaseIdx)) 
    #     plotP(total_mask_all_storage, 'Purples', 'generatorMAP_'+str(CaseIdx)) 



    # # For 50 to 99 and 0 to 99, calculate the difference
    # def cal_mean_std(array, series, idx):
    #     array[idx, 0] = np.mean(series)
    #     array[idx, 1] = np.std(series)
    # def Scenario3Fig2(table1, table2, name):
    #     solar_cap, wind_cap, nuclear_cap, tes_cap = np.zeros([totctys, 2]), np.zeros([totctys, 2]), np.zeros([totctys, 2]), np.zeros([totctys, 2])
    #     for idx in range(len(TwoLettersCode)):
    #         CtyList1 = table1[idx]
    #         CtyList2 = table2[idx]
    #         cal_mean_std(solar_cap,   np.array(CtyList1['solar_cap']) -   np.array(CtyList2['solar_cap']) -   np.array(CtyList2['solar_fixed_cap']),   idx)
    #         cal_mean_std(wind_cap,    np.array(CtyList1['wind_cap']) -    np.array(CtyList2['wind_cap']) -    np.array(CtyList2['wind_fixed_cap']),    idx)
    #         cal_mean_std(nuclear_cap, np.array(CtyList1['nuclear_cap']) - np.array(CtyList2['nuclear_cap']) - np.array(CtyList2['nuclear_fixed_cap']), idx)
    #         cal_mean_std(tes_cap,     np.array(CtyList1['heat_storage_cap']) - np.array(CtyList2['heat_storage_cap']) - np.array(CtyList2['heat_storage_fixed_cap']), idx)
    #     x1, x2 = -1, 42
    #     y1, y2 = -1.5, 1.0
    #     xaxis1 = np.arange(totctys)
    #     ax1 = plt.subplot(311);                         ax1.bar(xaxis1, solar_cap[:, 0],   yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='wheat');   ax1.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    #     ax2 = plt.subplot(312, sharex=ax1, sharey=ax1); ax2.bar(xaxis1, wind_cap[:, 0],    yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='skyblue'); ax2.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    #     ax3 = plt.subplot(313, sharex=ax1, sharey=ax1); ax3.bar(xaxis1, nuclear_cap[:, 0], yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='tomato');  ax3.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    #     ax1.set_xlim(x1, x2); ax1.set_ylim(y1, y2)
    #     ax1.set_xticks(xaxis1)
    #     ax1.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0])
    #     # plt.show() 
    #     plt.savefig(name+'.ps') 
    #     plt.clf()
    # Scenario3Fig2(EIA_99, SummaryTable_eia_50to99, 'eia')
    # Scenario3Fig2(C4K_99, SummaryTable_c4k_50to99, 'c4k')


    # sys_cost_diff = []
    # for idx in range(len(TwoLettersCode)):
    #     CtyList1 = np.mean(EIA_99[idx]['system_cost'])
    #     CtyList2 = np.mean(SummaryTable_eia_50to99[idx]['system_cost'])
    #     # CtyList1 = np.mean(C4K_99[idx]['system_cost'])
    #     # CtyList2 = np.mean(SummaryTable_c4k_50to99[idx]['system_cost'])
    #     DiffInPerc = ( CtyList2 - CtyList1 ) / CtyList1 * 100
    #     sys_cost_diff.append(DiffInPerc)
    # print (np.array(sys_cost_diff).max())
    # print (np.array(sys_cost_diff).min())

    # def plotP(var, col, name):
    #     ax1 = plt.subplot(111, projection=ccrs.PlateCarree())
    #     ax1.add_feature(cfeature.COASTLINE)
    #     ax1.add_feature(cfeature.BORDERS)
    #     ax1.set_extent([-180, 180, -60, 90], crs=ccrs.PlateCarree())
    #     mp = ax1.pcolor(lon, lat, np.ma.masked_equal(var, 0), cmap=col, norm=colors.Normalize(vmin=0, vmax=12), transform=ccrs.PlateCarree())
    #     ax1.contourf(lon, lat, mask_array_new, colors='none', hatches=['.'*5], transform=ccrs.PlateCarree())
    #     plt.colorbar(mp, ax=ax1, extend='max', shrink=0.5, orientation='vertical')
    #     # plt.show()
    #     plt.savefig(name+'.ps')
    #     plt.clf()
    # f_axis = cdms.open('SWGDN.nc')
    # v=f_axis('SWGDN')
    # lat, lon=v.getAxis(1), v.getAxis(2)
    # f_axis.close()
    # world_countries_array = regionmask.defined_regions.natural_earth.countries_110
    # mask = np.array(world_countries_array.mask(lon, lat, wrap_lon=False))
    # f_land_mask = cdms.open('land_sea_mask_merra.nc4')
    # ocean_mask = f_land_mask('FROCEAN',squeeze=1)
    # ocean_mask[ocean_mask>=0.5] = 1.
    # ocean_mask[ocean_mask<0.5]  = 0.
    # f_land_mask.close()
    # mask_ocean = MV.masked_equal(ocean_mask, 1) + 1
    # total_mask_sc = np.zeros([len(lat), len(lon)])
    # mask_array = np.zeros([len(lat), len(lon)])
    # find_idx_list = [82, 9, 137, 29, 3, 10, 139, 32, 163, 43, 121, 59, 98, 8, 107, 141, 155, 164, 148, 27, 162, 72, 136, 56, 156, 31, 113, 18, 158, 25, 96, 132, 14, 110, 91, 81, 124, 112, 143, 4, 40, 94]
    # for idx_idx in range(len(find_idx_list)):
    #     new_mask = np.copy(mask)
    #     find_region = MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1
    #     mask_new = MV.filled(find_region * mask_ocean, 0)
    #     total_mask_sc = total_mask_sc + sys_cost_diff[idx_idx] * mask_new
    #     mask_array = mask_array + MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
    # mask_array_new = np.ma.masked_equal(mask_array + ocean_mask, 1)
    # plotP(total_mask_sc, 'Reds', 'system_cost_eia') 
    # """






    # %%
    """
    ### Check discount rates
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    TwoLettersCode = ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load']

    # EIA_2p, EIA_7p, EIA_12p = [], [], []
    # C4K_2p, C4K_7p, C4K_12p = [], [], []
    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name1 = f'U_AdvaNuclear_DisCou2p_Year2019_{cty_idx}_Co2Cons';      EIA_2p  += [Get_Table(case_name1, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name2 = f'U_AdvaNuclear_Year2019_{cty_idx}_Co2Cons';               EIA_7p  += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name3 = f'U_AdvaNuclear_DisCou12p_Year2019_{cty_idx}_Co2Cons';     EIA_12p += [Get_Table(case_name3, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name4 = f'U_AdvaNuclear4000_DisCou2p_Year2019_{cty_idx}_Co2Cons';  C4K_2p  += [Get_Table(case_name4, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name5 = f'U_AdvaNuclear4000_Year2019_{cty_idx}_Co2Cons';           C4K_7p  += [Get_Table(case_name5, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name6 = f'U_AdvaNuclear4000_DisCou12p_Year2019_{cty_idx}_Co2Cons'; C4K_12p += [Get_Table(case_name6, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario6_2_210508.pickle', 'wb') as handle:
    #     pickle.dump([EIA_2p, EIA_7p, EIA_12p, C4K_2p, C4K_7p, C4K_12p], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario6_2_210508.pickle', 'rb') as handle:
        EIA_2p, EIA_7p, EIA_12p, C4K_2p, C4K_7p, C4K_12p = pickle.load(handle)

    # Plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
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
                   np.array(CurrentCase['lost_load_var'])]
        y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']
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
        ax.set_ylim(0, 0.16)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        plt.clf()
    for cty_idx in range(len(TwoLettersCode)):
        # plot_cost(EIA_2p[cty_idx],  f'EIA_2p_{TwoLettersCode[cty_idx]}')
        # plot_cost(EIA_7p[cty_idx],  f'EIA_7p_{TwoLettersCode[cty_idx]}')
        # plot_cost(EIA_12p[cty_idx], f'EIA_12p_{TwoLettersCode[cty_idx]}')
        plot_cost(C4K_2p[cty_idx],  f'C4K_2p_{TwoLettersCode[cty_idx]}')
        plot_cost(C4K_7p[cty_idx],  f'C4K_7p_{TwoLettersCode[cty_idx]}')
        plot_cost(C4K_12p[cty_idx], f'C4K_12p_{TwoLettersCode[cty_idx]}')
    # """



    # %% 

    """
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table, get_case_dispatch
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    table_AdvaNuclear_EIA_ERA5_scaled,  table_AdvaNuclear_4000_ERA5_scaled  = [], []
    table_AdvaNuclear_EIA_ERA5_origin,  table_AdvaNuclear_4000_ERA5_origin  = [], []
    TwoLettersCode = ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 
                           80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 
                           40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])
    new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'advanced_nuclear', 'lost_load']
    

    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name1 = f'U_AdvaNuclear_ERA5_Year2019_{cty_idx}_Co2Cons';         table_AdvaNuclear_EIA_ERA5_scaled  += [Get_Table(case_name1, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name2 = f'U_AdvaNuclear_ERA5222_Year2019_{cty_idx}_Co2Cons';      table_AdvaNuclear_EIA_ERA5_origin  += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name3 = f'U_AdvaNuclear4000_ERA5_Year2019_{cty_idx}_Co2Cons';     table_AdvaNuclear_4000_ERA5_scaled += [Get_Table(case_name3, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    #     case_name4 = f'U_AdvaNuclear4000_ERA5222_Year2019_{cty_idx}_Co2Cons';  table_AdvaNuclear_4000_ERA5_origin += [Get_Table(case_name4, repeat_list = co2_cons, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario7_210508.pickle', 'wb') as handle:
    #     pickle.dump([table_AdvaNuclear_EIA_ERA5_scaled, table_AdvaNuclear_EIA_ERA5_origin, table_AdvaNuclear_4000_ERA5_scaled, table_AdvaNuclear_4000_ERA5_origin], handle, protocol=pickle.HIGHEST_PROTOCOL)
    # stop 


    with open('Scenario7_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA_ERA5_scaled, table_AdvaNuclear_EIA_ERA5_origin, table_AdvaNuclear_4000_ERA5_scaled, table_AdvaNuclear_4000_ERA5_origin = pickle.load(handle)
    with open('Scenario1_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)

    # Plot
    xlist = np.array([100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                       60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                       20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])/100
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
                   np.array(CurrentCase['lost_load_var'])]
        y_color = ['black', 'grey', 'wheat', 'skyblue', 'tomato', 'indigo', 'plum', 'cadetblue']

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
        ax.set_ylim(0, 0.12)
        # plt.show()
        plt.savefig(default_case_name+'.ps')
        # plt.savefig(default_case_name+'.png', dpi='1000')
        plt.clf()

    for cty_idx in range(len(TwoLettersCode)):
        plot_cost(table_AdvaNuclear_EIA_ERA5_scaled[cty_idx],  f'Nuclear_with_TES_EIA_ERA5_{TwoLettersCode[cty_idx]}')
        plot_cost(table_AdvaNuclear_EIA_ERA5_origin[cty_idx],  f'Nuclear_with_TES_EIA_ERA5222_{TwoLettersCode[cty_idx]}')
        # plot_cost(table_AdvaNuclear_4000_ERA5_scaled[cty_idx], f'Nuclear_with_TES_4000_ERA5_{TwoLettersCode[cty_idx]}')
        # plot_cost(table_AdvaNuclear_4000_ERA5_origin[cty_idx], f'Nuclear_with_TES_4000_ERA5222_{TwoLettersCode[cty_idx]}')
    

    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
                      'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
                      'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
                      'VE','VN']
    for cty_idx in range(len(TwoLettersCode)):
        if TwoLettersCode[cty_idx] in ['US', 'CN', 'DE', 'ZA', 'AU', 'BR']:
            plot_cost(table_AdvaNuclear_EIA[cty_idx],              f'Nuclear_with_TES_EIA_{TwoLettersCode[cty_idx]}')
            # plot_cost(table_AdvaNuclear_4000[cty_idx],             f'Nuclear_with_TES_4000_{TwoLettersCode[cty_idx]}')
    # """



    # %%
    """
    # Check-battery with/without nuclear
    import numpy as np
    import pickle, os
    from Postprocess_func import Get_Table
    from scipy import stats
    import matplotlib.pyplot as plt

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults3/'
    table_NoNuclear_EIA,  table_NoNuclear_4000  = [], []
    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
                      'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
                      'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
                      'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
                      'VE','VN']
    co2_cons = np.array([1e24, 98, 96, 94, 92, 90, 88, 86, 84, 82, 
                           80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 
                           60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 
                           40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 
                           20, 18, 16, 14, 12, 10, 8,  6,  4,  2,  1, 0.1, 0.01, 0.001, 0])

    # co2_cons = np.array([1])
    # tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'lost_load']
    # for cty_idx in TwoLettersCode:
    #     print (cty_idx)
    #     case_name1 = f'U_AdvaNuclear_NoNuclear_Year2019_{cty_idx}_Co2Cons';       table_NoNuclear_EIA  += [Get_Table(case_name1, repeat_list = co2_cons, data_path = data_find, tech_name_list=tech_lists)]
    #     case_name2 = f'U_AdvaNuclear4000_NoNuclear_Year2019_{cty_idx}_Co2Cons';   table_NoNuclear_4000 += [Get_Table(case_name2, repeat_list = co2_cons, data_path = data_find, tech_name_list=tech_lists)]
    # with open('Scenario8_210508.pickle', 'wb') as handle:
    #     pickle.dump([table_NoNuclear_EIA, table_NoNuclear_4000], handle, protocol=pickle.HIGHEST_PROTOCOL)
    # stop 

    with open('Scenario8_210508.pickle', 'rb') as handle:
        table_NoNuclear_EIA, table_NoNuclear_4000 = pickle.load(handle)
    with open('Scenario1_210508.pickle', 'rb') as handle:
        table_AdvaNuclear_EIA, table_AdvaNuclear_4000, table_AdvaNuclear_2000, table_ConvNuclear_EIA, table_ConvNuclear_4000, table_ConvNuclear_2000 = pickle.load(handle)
    
    storage_cap_NoNuclear = [] 
    storage_cap_EIA = [] 
    storage_cap_c4k = [] 
    for idx in range(len(TwoLettersCode)):
        storage_cap_NoNuclear.append(table_NoNuclear_EIA[idx]['storage_cap'][0])
        storage_cap_EIA.append(table_AdvaNuclear_EIA[idx]['storage_cap'][-5]+table_AdvaNuclear_EIA[idx]['heat_storage_cap'][-5]*0.370800284)
        storage_cap_c4k.append(table_AdvaNuclear_4000[idx]['storage_cap'][-5]+table_AdvaNuclear_EIA[idx]['heat_storage_cap'][-5]*0.370800284)

    print (co2_cons[-5])
    print (np.average(storage_cap_NoNuclear), np.std(storage_cap_NoNuclear), np.min(storage_cap_NoNuclear), np.max(storage_cap_NoNuclear))
    print (np.average(storage_cap_EIA), np.std(storage_cap_EIA), np.min(storage_cap_EIA), np.max(storage_cap_EIA))
    print (np.average(storage_cap_c4k), np.std(storage_cap_c4k), np.min(storage_cap_c4k), np.max(storage_cap_c4k))

    output_array = np.array([storage_cap_NoNuclear, storage_cap_EIA, storage_cap_c4k])
    np.savetxt("TableS4.csv", output_array.T, fmt='%.5f', delimiter=",")
    # """

    



    # %%