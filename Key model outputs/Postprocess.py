
import numpy as np, pickle, os
from Postprocess_func import Get_Table, get_case_dispatch
from scipy import stats
    
if __name__ == "__main__":

    data_find = '/Volumes/My Passport/MEM_AdvNuc/SingleCountryResults2/'

    """ 
    # Scenario 1, basic comparisions using 2019 weather data and one-year demand
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # SummaryTable_US2019_Nucl = []
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('ConvNuclear_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # with open('Scenario1_1.pickle', 'wb') as handle:
    #     pickle.dump(SummaryTable_US2019_Nucl, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario1_1.pickle', 'rb') as handle:
        SummaryTable_US2019_Nucl = pickle.load(handle)
    from Postprocess_fig import Scenario1Fig1
    Scenario1Fig1('Cap', SummaryTable_US2019_Nucl, 'cap')
    Scenario1Fig1('Cost', SummaryTable_US2019_Nucl, 'cost')
    Scenario1Fig1('SysCos', SummaryTable_US2019_Nucl, 'SysCos')

    # FirstDayofMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    # case_idx = '1.0/' # '0.0' for 100% decarbonization
    # case_name = ['ConvNuclear_Year2019_US_Co2Cons' + case_idx,
    #              'ConvNuclear_Year2019_CN_Co2Cons' + case_idx,
    #              'ConvNuclear_Year2019_DE_Co2Cons' + case_idx,
    #              'ConvNuclear_Year2019_ZA_Co2Cons' + case_idx,
    #              'ConvNuclear_Year2019_AU_Co2Cons' + case_idx,
    #              'ConvNuclear_Year2019_BR_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_US_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_CN_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_DE_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_ZA_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_AU_Co2Cons' + case_idx,
    #              'AdvaNuclear_Year2019_BR_Co2Cons' + case_idx]
    # DicNew = [] 
    # for case_name_idx in case_name:
    #     DicNew += get_case_dispatch(case_name_idx, data_find)
    # with open('Scenario1_2.pickle', 'wb') as handle:
    #     pickle.dump(DicNew, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario1_2.pickle', 'rb') as handle:
        DicNew = pickle.load(handle)
    from Postprocess_fig import Scenario1Fig2
    Scenario1Fig2(DicNew)

    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    # NumOfCty = len(TwoLettersCode)
    # NumOfCas = len(co2_const)
    # SummaryTableTES2019 = []
    # base_case_name = 'AdvaNuclear_Year2019_'
    # for name_idx in TwoLettersCode:
    #     print (name_idx)
    #     case_name = base_case_name + name_idx + '_Co2Cons'
    #     SummaryTableTES2019 += [Get_Table(case_name, repeat_list = co2_const, data_path = data_find)]
    # def nonan(input):
    #     input[input==0] = np.nan
    #     return input
    # ToDrawArray = np.zeros([NumOfCty, NumOfCas])
    # for idx in range(NumOfCty):
    #     a1 = nonan(np.array(SummaryTableTES2019[idx]['heat_storage_cap']))
    #     a3 = nonan(np.array(SummaryTableTES2019[idx]['nuclear_cap']))
    #     ratio = a1/a3
    #     ToDrawArray[idx, :] = ratio
    # with open('Scenario1_3.pickle', 'wb') as handle:
    #     pickle.dump(ToDrawArray, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario1_3.pickle', 'rb') as handle:
        ToDrawArray = pickle.load(handle)
    from Postprocess_fig import Scenario1Fig3
    Scenario1Fig3(ToDrawArray, 4)
    # """



    """
    # Scenario 2, Fixed nuclear capacity at 0.01 kWh-e
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # NumOfCty = len(TwoLettersCode)
    # NumOfCas = len(co2_const)
    # SummaryTableFixed001Nuclear2019 = []
    # base_case_name = 'Fixed001Nuclear_Year2019_'
    # for name_idx in TwoLettersCode:
    #     print (name_idx)
    #     case_name = base_case_name + name_idx + '_Co2Cons'
    #     SummaryTableFixed001Nuclear2019 += [Get_Table(case_name, repeat_list = co2_const, data_path = data_find)]
    # def nonan(input):
    #     input[input==0] = np.nan
    #     return input
    # ToDrawArray = np.zeros([NumOfCty, NumOfCas])
    # for idx in range(NumOfCty):
    #     a1 = nonan(np.array(SummaryTableFixed001Nuclear2019[idx]['heat_storage_cap']))
    #     a3 = nonan(np.array(SummaryTableFixed001Nuclear2019[idx]['nuclear_cap']))
    #     ratio = a1/a3
    #     ToDrawArray[idx, :] = ratio
    # # Save in Pickle for further uses
    # with open('Scenario2.pickle', 'wb') as handle:
    #     pickle.dump(ToDrawArray, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario2.pickle', 'rb') as handle:
        ToDrawArray = pickle.load(handle)
    from Postprocess_fig import Scenario1Fig3
    Scenario1Fig3(ToDrawArray, 200)
    # """




    """
    # Scenario 3, Multiple countries, multiple years, and from 50% to 100%
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    # year_list = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
    #              1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
    #              2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    #              2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    # totctys, totyears, totcase = len(TwoLettersCode), len(year_list), 5

    # default_name = 'AdvaNuclear_'
    # SummaryTable_4000_1e24 = []
    # SummaryTable_4000_05 = []
    # SummaryTable_4000_01 = []
    # SummaryTable_4000_00 = []
    # for country_idx in TwoLettersCode:
    #     case_name = 'AdvaNuclear_Year' + '_' + country_idx + '_Co2Cons1e+24'
    #     dividing_point = len('AdvaNuclear_Year')
    #     SummaryTable_4000_1e24 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find)]
    #     case_name = 'AdvaNuclear_Year' + '_' + country_idx + '_Co2Cons50.0'
    #     dividing_point = len('AdvaNuclear_Year')
    #     SummaryTable_4000_05 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find)]
    #     case_name = 'AdvaNuclear_Year' + '_' + country_idx + '_Co2Cons1.0'
    #     dividing_point = len('AdvaNuclear_Year')
    #     SummaryTable_4000_01 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find)]
    #     case_name = 'AdvaNuclear_Year' + '_' + country_idx + '_Co2Cons0.0'
    #     dividing_point = len('AdvaNuclear_Year')
    #     SummaryTable_4000_00 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find)]
    # with open('Scenario3_1.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable_4000_1e24, SummaryTable_4000_05, SummaryTable_4000_01, SummaryTable_4000_00], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario3_1.pickle', 'rb') as handle:
        SummaryTable_4000_1e24, SummaryTable_4000_05, SummaryTable_4000_01, SummaryTable_4000_00 = pickle.load(handle)
    
    # tech_name_list = ['natgas', 'natgas_fixed', 'natgas_ccs', 'natgas_ccs_fixed', 'solar', 'solar_fixed', 'wind', 'wind_fixed', 
    #                   'storage', 'storage_fixed', 'conventional_nuclear', 'conventional_nuclear_fixed', 'lost_load', 
    #                   'advanced_nuclear', 'advanced_nuclear_fixed']
    # default_name = 'zzzto100_AdvaNuclear_'
    # SummaryTable_4000_50to100 = []
    # SummaryTable_4000_50to99 = []
    # for country_idx in TwoLettersCode:
    #     # case_name = default_name + 'Year' + '_' + country_idx + '_Co2Cons50.0'
    #     # dividing_point = len(default_name + 'Year') 
    #     # SummaryTable_4000_50to100 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find, tech_name_list = tech_name_list)]
    #     case_name = default_name + 'Year' + '_' + country_idx + '_Co2Cons50.0_Co2Const1.0'
    #     dividing_point = len(default_name + 'Year') 
    #     SummaryTable_4000_50to99 += [Get_Table(case_name, repeat_list = year_list, dividing_name_point = dividing_point, data_path = data_find, tech_name_list = tech_name_list)]
    #     print (len(SummaryTable_4000_50to99))
    # with open('Scenario3_2.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable_4000_50to99], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario3_2.pickle', 'rb') as handle:
        SummaryTable_4000_50to99 = pickle.load(handle)[0]


    def InitialArray(info, NameArray, totctys, totcase):
        for name_idx in NameArray:
            info[name_idx] = np.zeros([totctys, totcase, 2])
    info = {}
    NameList1 = ['natgas_cap', 'natgas_ccs_cap', 'solar_cap', 'wind_cap', 'storage_cap', 'conventional_nuclear_cap','nuclear_cap', 'heat_storage_cap', 'nuclear_generator_REAmatch_cap', 'nuclear_generator_TESmatch_cap']
    InitialArray(info, NameList1, totctys, totcase)
    NameList2 = ['natgas_fixed_cap', 'natgas_ccs_fixed_cap', 'solar_fixed_cap', 'wind_fixed_cap', 'storage_fixed_cap', 'conventional_nuclear_fixed_cap', 'nuclear_fixed_cap', 'heat_storage_fixed_cap', 'nuclear_generator_fixed_REAmatch_cap', 'nuclear_generator_fixed_TESmatch_cap']
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
    PartitionResults(info, NameList1, SummaryTable_4000_1e24, 0)
    PartitionResults(info, NameList1, SummaryTable_4000_05, 1)
    PartitionResults(info, NameList1, SummaryTable_4000_01, 2)
    PartitionResults(info, NameList1, SummaryTable_4000_00, 3)
    PartitionResults(info, np.r_[NameList1, NameList2], SummaryTable_4000_50to99, 4)
    from Postprocess_fig import Scenario3Fig1  # Map plot
    Scenario3Fig1(info, [0,1,2,3])
    from Postprocess_fig import Scenario3Fig4  # Scatter plot
    Scenario3Fig4(info)

    # Calculat difference between with/ot pre-fixed capacities
    def cal_mean_std(array, series, idx):
        array[idx, 0] = np.mean(series)
        array[idx, 1] = np.std(series)
    totctys = len(TwoLettersCode)
    solar_cap, wind_cap, nuclear_cap = np.zeros([totctys, 2]), np.zeros([totctys, 2]), np.zeros([totctys, 2])
    tes_cap = np.zeros([totctys, 2])
    def caldifferences(SummaryTable1, SummaryTable2):
        for idx in range(len(TwoLettersCode)):
            CtyList1 = SummaryTable1[idx]
            CtyList2 = SummaryTable2[idx]
            cal_mean_std(solar_cap,   np.array(CtyList1['solar_cap']) -   np.array(CtyList2['solar_cap']) -   np.array(CtyList2['solar_fixed_cap']),   idx)
            cal_mean_std(wind_cap,    np.array(CtyList1['wind_cap']) -    np.array(CtyList2['wind_cap']) -    np.array(CtyList2['wind_fixed_cap']),    idx)
            cal_mean_std(nuclear_cap, np.array(CtyList1['nuclear_cap']) - np.array(CtyList2['nuclear_cap']) - np.array(CtyList2['nuclear_fixed_cap']), idx)
            cal_mean_std(tes_cap,     np.array(CtyList1['heat_storage_cap']) - np.array(CtyList2['heat_storage_cap']) - np.array(CtyList2['heat_storage_fixed_cap']), idx)
    caldifferences(SummaryTable_4000_01, SummaryTable_4000_50to99) 
    from Postprocess_fig import Scenario3Fig2
    Scenario3Fig2(solar_cap, wind_cap, nuclear_cap)
    sys_cost_diff = []
    for idx in range(len(TwoLettersCode)):
        CtyList1 = np.mean(SummaryTable_4000_01[idx]['system_cost'])
        CtyList2 = np.mean(SummaryTable_4000_50to99[idx]['system_cost'])
        DiffInPerc = ( CtyList2 - CtyList1 ) / CtyList1 * 100
        sys_cost_diff.append(DiffInPerc)
    from Postprocess_fig import Scenario3Fig3
    Scenario3Fig3(sys_cost_diff)
    # """




    """
    # Scenario 4, Unmet demand cost
    # unmet_demand_cost = [10**(-3), 10**(-2.8), 10**(-2.6), 10**(-2.4), 10**(-2.2),
    #                      10**(-2), 10**(-1.8), 10**(-1.6), 10**(-1.4), 10**(-1.2),
    #                      10**(-1), 10**(-0.8), 10**(-0.6), 10**(-0.4), 10**(-0.2),
    #                      10**0,    10**0.2,    10**0.4,    10**0.6,    10**0.8,
    #                      10**1]
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN'] 
    # new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 'conventional_nuclear', 'advanced_nuclear', 'lost_load', 'shift_load']
    # SummaryTable_LostLoad, SummaryTable_ShiftLoad = [], []
    # for idx in TwoLettersCode:
    #     print (idx)
    #     SummaryTable_LostLoad += [Get_Table('LostLoad_Year2019_' + idx + '_LostLoad', repeat_list = unmet_demand_cost, data_path = data_find)]
    #     SummaryTable_ShiftLoad += [Get_Table('ShiftLoad_Year2019_' + idx + '_LoadShift', repeat_list = unmet_demand_cost, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario4.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable_LostLoad, SummaryTable_ShiftLoad], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario4.pickle', 'rb') as handle:
        SummaryTable_LostLoad, SummaryTable_ShiftLoad = pickle.load(handle)
    from Postprocess_fig import Scenario4Fig2
    Scenario4Fig2(SummaryTable_LostLoad, 1.5, 'loadlost')
    Scenario4Fig2(SummaryTable_ShiftLoad, 1.5, 'loadshift')
    # """  




    """  
    # Scenario 5, Resistance heater
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # TwoLettersCode = ['US','CN','DE','ZA','AU','BR']
    # new_tech_lists = ['natgas', 'natgas_ccs', 'solar', 'wind', 'storage', 
    #                   'conventional_nuclear', 'advanced_nuclear', 'lost_load', 
    #                   'Resistant Heater']
    # SummaryTable_RH = []
    # for idx in TwoLettersCode:
    #     SummaryTable_RH += [Get_Table('FreeResisHeater_Year2019_' + idx + '_Co2Cons', repeat_list = co2_const, data_path = data_find, tech_name_list=new_tech_lists)]
    # with open('Scenario5.pickle', 'wb') as handle:
    #     pickle.dump(SummaryTable_RH, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario5.pickle', 'rb') as handle:
        SummaryTable_RH = pickle.load(handle)
    from Postprocess_fig import Scenario5Fig1
    Scenario5Fig1('Cap', SummaryTable_RH, 'cap')
    Scenario5Fig1('Cost', SummaryTable_RH, 'cost')
    # """  




    """  
    # Scenario 6, Different nuclear costs
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # TwoLettersCode = ['US','CN','DE','ZA','AU','BR']
    # SummaryTable2019_2000 = []
    # SummaryTable2019_3000 = []
    # SummaryTable2019_4000 = []
    # SummaryTable2019_5000 = []
    # SummaryTable2019_6000 = []
    # for cty_idx in TwoLettersCode:
    #     SummaryTable2019_2000 += [Get_Table(f'Adva2000Nuclear_Year2019_{cty_idx}_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    #     SummaryTable2019_3000 += [Get_Table(f'Adva3000Nuclear_Year2019_{cty_idx}_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    #     SummaryTable2019_4000 += [Get_Table(f'AdvaNuclear_Year2019_{cty_idx}_Co2Cons',     repeat_list = co2_const, data_path = data_find)]
    #     SummaryTable2019_5000 += [Get_Table(f'Adva5000Nuclear_Year2019_{cty_idx}_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    #     SummaryTable2019_6000 += [Get_Table(f'Adva6000Nuclear_Year2019_{cty_idx}_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # # Save in Pickle for further uses
    # with open('Scenario6.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable2019_2000, SummaryTable2019_3000, SummaryTable2019_4000, SummaryTable2019_5000, SummaryTable2019_6000], handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario6.pickle', 'rb') as handle:
        SummaryTable2019_2000, SummaryTable2019_3000, SummaryTable2019_4000, SummaryTable2019_5000, SummaryTable2019_6000 = pickle.load(handle)
    from Postprocess_fig import Scenario1Fig1
    Scenario1Fig1('Cap2', SummaryTable2019_2000, 'cap')
    Scenario1Fig1('Cap3', SummaryTable2019_3000, 'cap')
    Scenario1Fig1('Cap4', SummaryTable2019_4000, 'cap')
    Scenario1Fig1('Cap5', SummaryTable2019_5000, 'cap')
    Scenario1Fig1('Cap6', SummaryTable2019_6000, 'cap')
    Scenario1Fig1('Cost2k', SummaryTable2019_2000, 'cost')
    Scenario1Fig1('Cost3k', SummaryTable2019_3000, 'cost')
    Scenario1Fig1('Cost4k', SummaryTable2019_4000, 'cost')
    Scenario1Fig1('Cost5k', SummaryTable2019_5000, 'cost')
    Scenario1Fig1('Cost6k', SummaryTable2019_6000, 'cost')
    # """  




    """  
    # Scenario 7, No TES
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # SummaryTable_US2019_Nucl = []
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoTES_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # with open('Scenario7.pickle', 'wb') as handle:
    #     pickle.dump(SummaryTable_US2019_Nucl, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario7.pickle', 'rb') as handle:
        SummaryTable_US2019_Nucl = pickle.load(handle)    
    from Postprocess_fig import Scenario1Fig1
    Scenario1Fig1('Cap', SummaryTable_US2019_Nucl, 'cap')
    Scenario1Fig1('SysCos', SummaryTable_US2019_Nucl, 'SysCos')
    # """  




    """  
    # Scenario 8, $6000/kW nuclear costs for all countries
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    # SummaryTable2019_6000 = []
    # for cty_idx in TwoLettersCode:
    #     SummaryTable2019_6000 += [Get_Table(f'Adva6000Nuclear_Year2019_{cty_idx}_Co2Cons1.0', data_path = data_find)]
    # with open('Scenario8.pickle', 'wb') as handle:
    #     pickle.dump(SummaryTable2019_6000, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario8.pickle', 'rb') as handle:
        SummaryTable2019_6000 = pickle.load(handle)    
    from Postprocess_fig import Scenario8Fig1
    Scenario8Fig1('test', SummaryTable2019_6000)
    # """  




    """ 
    #------------------------------------ Table S2
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN','CO','EG','FR',
    #                   'DE','GH','IN','ID','IR','IT','JP','LY','MY','MX',
    #                   'MA','MZ','NZ','NG','PY','PE','PL','RU','SA','ZA',
    #                   'KR','ES','SD','SE','TH','TN','TR','UA','GB','US',
    #                   'VE','VN']
    # # Basic table
    # SummaryTable2019 = []
    # for name_idx in TwoLettersCode:
    #     print (name_idx)
    #     case_name2 = 'AdvaNuclear_Year2019_' + str(name_idx) + '_Co2Cons'
    #     SummaryTable2019 += [Get_Table(case_name2, repeat_list = co2_const, data_path = data_find)]
    # # Dispatch percentage
    # DicNew = [] 
    # for idx1 in range(len(TwoLettersCode)):
    #     cty_name = TwoLettersCode[idx1]
    #     print (cty_name)
    #     DicCty = []
    #     for idx2 in range(len(co2_const)):
    #         co2_name = co2_const[idx2]
    #         case_name = 'AdvaNuclear_Year2019_'+cty_name+'_Co2Cons'+str(co2_name)+'/'
    #         DicCty.append(get_case_dispatch(case_name, data_find)[0]['percentage'])
    #     DicNew += [DicCty]
    # with open('TableS2.pickle', 'wb') as handle:
    #     pickle.dump([SummaryTable2019, DicNew], handle, proto col=pickle.HIGHEST_PROTOCOL)
    with open('TableS2.pickle', 'rb') as handle:
        SummaryTable2019, DicNew = pickle.load(handle)
    from Postprocess_fig import showTableS2
    showTableS2(SummaryTable2019, DicNew)
    # """



    """
    # Scenario 9, no curtailment from nuclear
    # co2_const = [1e+24, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
    #               80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
    #               60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
    #               38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
    #               16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0]
    # SummaryTable_US2019_Nucl = []
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_US_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_CN_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_DE_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_ZA_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_AU_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # SummaryTable_US2019_Nucl += [Get_Table('AdvaNuclear_NoCurtailment_Year2019_BR_Co2Cons', repeat_list = co2_const, data_path = data_find)]
    # with open('Scenario9.pickle', 'wb') as handle:
    #     pickle.dump(SummaryTable_US2019_Nucl, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario9_1.pickle', 'rb') as handle:
        SummaryTable_US2019_Nucl = pickle.load(handle) 
    from Postprocess_fig import ScenarioNewFig1
    ScenarioNewFig1('Cost', SummaryTable_US2019_Nucl, 'cost')

    # FirstDayofMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    # case_idx = '1.0/'
    # case_name = ['AdvaNuclear_NoCurtailment_Year2019_US_Co2Cons' + case_idx,
    #              'AdvaNuclear_NoCurtailment_Year2019_CN_Co2Cons' + case_idx,
    #              'AdvaNuclear_NoCurtailment_Year2019_DE_Co2Cons' + case_idx,
    #              'AdvaNuclear_NoCurtailment_Year2019_ZA_Co2Cons' + case_idx,
    #              'AdvaNuclear_NoCurtailment_Year2019_AU_Co2Cons' + case_idx,
    #              'AdvaNuclear_NoCurtailment_Year2019_BR_Co2Cons' + case_idx]
    # DicNew = [] 
    # for case_name_idx in case_name:
    #     DicNew += get_case_dispatch(case_name_idx, data_find)
    # with open('Scenario9_2.pickle', 'wb') as handle:
    #     pickle.dump(DicNew, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Scenario9_2.pickle', 'rb') as handle:
        DicNew = pickle.load(handle) 
    from Postprocess_fig import Scenario1Fig2
    Scenario1Fig2(DicNew)
    # """