from Preprocess_Input import read_csv_dated_data_file
import numpy as np
import datetime

def GetNameList():
    TwoLettersCode = ['DZ','AR','AU','BR','CA','CL','CN',
                      'CO','EG','FR','DE','GH','IN','ID',
                      'IR','IT','JP','LY','MY','MX','MA',
                      'MZ','NZ','NG','PY','PE','PL','RU',
                      'SA','ZA','KR','ES','SD','SE','TH',
                      'TN','TR','UA','GB','US','VE','VN']
    return TwoLettersCode


def GetCFsName(region_name, source='MERRA2'):
    FullDemandList = {'DZ': 'demand_series_Dan_normalized_to_1_mean_Algeria.csv', 'AR': 'demand_series_Dan_normalized_to_1_mean_Argentina.csv',
                      'AU': 'demand_series_Dan_normalized_to_1_mean_Australia.csv', 'BR': 'demand_series_Dan_normalized_to_1_mean_Brazil.csv',
                      'CA': 'demand_series_Dan_normalized_to_1_mean_Canada.csv', 'CL': 'demand_series_Dan_normalized_to_1_mean_Chile.csv',
                      'CN': 'demand_series_Dan_normalized_to_1_mean_China.csv', 'CO': 'demand_series_Dan_normalized_to_1_mean_Colombia.csv',
                      'EG': 'demand_series_Dan_normalized_to_1_mean_Egypt.csv', 'FR': 'demand_series_Dan_normalized_to_1_mean_France.csv',
                      'DE': 'demand_series_Dan_normalized_to_1_mean_Germany.csv', 'GH': 'demand_series_Dan_normalized_to_1_mean_Ghana.csv',
                      'IN': 'demand_series_Dan_normalized_to_1_mean_India.csv', 'ID': 'demand_series_Dan_normalized_to_1_mean_Indonesia.csv',
                      'IR': 'demand_series_Dan_normalized_to_1_mean_Iran.csv', 'IT': 'demand_series_Dan_normalized_to_1_mean_Italy.csv',
                      'JP': 'demand_series_Dan_normalized_to_1_mean_Japan.csv', 'LY': 'demand_series_Dan_normalized_to_1_mean_Libya.csv',
                      'MY': 'demand_series_Dan_normalized_to_1_mean_Malaysia.csv', 'MX': 'demand_series_Dan_normalized_to_1_mean_Mexico.csv',
                      'MA': 'demand_series_Dan_normalized_to_1_mean_Morocco.csv', 'MZ': 'demand_series_Dan_normalized_to_1_mean_Mozambique.csv',
                      'NZ': 'demand_series_Dan_normalized_to_1_mean_New Zealand.csv', 'NG': 'demand_series_Dan_normalized_to_1_mean_Nigeria.csv',
                      'PY': 'demand_series_Dan_normalized_to_1_mean_Paraguay.csv', 'PE': 'demand_series_Dan_normalized_to_1_mean_Peru.csv',
                      'PL': 'demand_series_Dan_normalized_to_1_mean_Poland.csv', 'RU': 'demand_series_Dan_normalized_to_1_mean_Russia.csv',
                      'SA': 'demand_series_Dan_normalized_to_1_mean_Saudi Arabia.csv', 'ZA': 'demand_series_Dan_normalized_to_1_mean_South Africa.csv',
                      'KR': 'demand_series_Dan_normalized_to_1_mean_South Korea.csv', 'ES': 'demand_series_Dan_normalized_to_1_mean_Spain.csv',
                      'SD': 'demand_series_Dan_normalized_to_1_mean_Sudan.csv', 'SE': 'demand_series_Dan_normalized_to_1_mean_Sweden.csv',
                      'TH': 'demand_series_Dan_normalized_to_1_mean_Thailand.csv', 'TN': 'demand_series_Dan_normalized_to_1_mean_Tunisia.csv',
                      'TR': 'demand_series_Dan_normalized_to_1_mean_Turkey.csv', 'UA': 'demand_series_Dan_normalized_to_1_mean_Ukraine.csv',
                      'GB': 'demand_series_Dan_normalized_to_1_mean_United Kingdom.csv', 'US': 'demand_series_Dan_normalized_to_1_mean_United States.csv',
                      'VE': 'demand_series_Dan_normalized_to_1_mean_Venezuela.csv', 'VN': 'demand_series_Dan_normalized_to_1_mean_Vietnam.csv'}
    DemandName = FullDemandList[region_name]
    
    if source == 'MERRA2':
        SolarCFsName = '20201218_' + str(region_name) + '_mthd3_solar.csv'
        WindCFsName = '20201218_' + str(region_name) + '_mthd3_wind.csv'
    elif source == 'ERA5':
        SolarCFsName = ['20201218_' + str(region_name) + '_mthd3_solar.csv', '20210617_' + str(region_name) + '_mthd3_1980-2020_solar.csv']
        WindCFsName  = ['20201218_' + str(region_name) + '_mthd3_wind.csv',  '20210617_' + str(region_name) + '_mthd3_1980-2020_wind.csv']
    else:
        print (f'source {source} not recognized')
        stop 

    return DemandName, SolarCFsName, WindCFsName



def GetCFsName2(region_name1, region_name2):
    FullDemandList = {'DZ': 'demand_series_Dan_normalized_to_1_mean_Algeria.csv', 'AR': 'demand_series_Dan_normalized_to_1_mean_Argentina.csv',
                      'AU': 'demand_series_Dan_normalized_to_1_mean_Australia.csv', 'BR': 'demand_series_Dan_normalized_to_1_mean_Brazil.csv',
                      'CA': 'demand_series_Dan_normalized_to_1_mean_Canada.csv', 'CL': 'demand_series_Dan_normalized_to_1_mean_Chile.csv',
                      'CN': 'demand_series_Dan_normalized_to_1_mean_China.csv', 'CO': 'demand_series_Dan_normalized_to_1_mean_Colombia.csv',
                      'EG': 'demand_series_Dan_normalized_to_1_mean_Egypt.csv', 'FR': 'demand_series_Dan_normalized_to_1_mean_France.csv',
                      'DE': 'demand_series_Dan_normalized_to_1_mean_Germany.csv', 'GH': 'demand_series_Dan_normalized_to_1_mean_Ghana.csv',
                      'IN': 'demand_series_Dan_normalized_to_1_mean_India.csv', 'ID': 'demand_series_Dan_normalized_to_1_mean_Indonesia.csv',
                      'IR': 'demand_series_Dan_normalized_to_1_mean_Iran.csv', 'IT': 'demand_series_Dan_normalized_to_1_mean_Italy.csv',
                      'JP': 'demand_series_Dan_normalized_to_1_mean_Japan.csv', 'LY': 'demand_series_Dan_normalized_to_1_mean_Libya.csv',
                      'MY': 'demand_series_Dan_normalized_to_1_mean_Malaysia.csv', 'MX': 'demand_series_Dan_normalized_to_1_mean_Mexico.csv',
                      'MA': 'demand_series_Dan_normalized_to_1_mean_Morocco.csv', 'MZ': 'demand_series_Dan_normalized_to_1_mean_Mozambique.csv',
                      'NZ': 'demand_series_Dan_normalized_to_1_mean_New Zealand.csv', 'NG': 'demand_series_Dan_normalized_to_1_mean_Nigeria.csv',
                      'PY': 'demand_series_Dan_normalized_to_1_mean_Paraguay.csv', 'PE': 'demand_series_Dan_normalized_to_1_mean_Peru.csv',
                      'PL': 'demand_series_Dan_normalized_to_1_mean_Poland.csv', 'RU': 'demand_series_Dan_normalized_to_1_mean_Russia.csv',
                      'SA': 'demand_series_Dan_normalized_to_1_mean_Saudi Arabia.csv', 'ZA': 'demand_series_Dan_normalized_to_1_mean_South Africa.csv',
                      'KR': 'demand_series_Dan_normalized_to_1_mean_South Korea.csv', 'ES': 'demand_series_Dan_normalized_to_1_mean_Spain.csv',
                      'SD': 'demand_series_Dan_normalized_to_1_mean_Sudan.csv', 'SE': 'demand_series_Dan_normalized_to_1_mean_Sweden.csv',
                      'TH': 'demand_series_Dan_normalized_to_1_mean_Thailand.csv', 'TN': 'demand_series_Dan_normalized_to_1_mean_Tunisia.csv',
                      'TR': 'demand_series_Dan_normalized_to_1_mean_Turkey.csv', 'UA': 'demand_series_Dan_normalized_to_1_mean_Ukraine.csv',
                      'GB': 'demand_series_Dan_normalized_to_1_mean_United Kingdom.csv', 'US': 'demand_series_Dan_normalized_to_1_mean_United States.csv',
                      'VE': 'demand_series_Dan_normalized_to_1_mean_Venezuela.csv', 'VN': 'demand_series_Dan_normalized_to_1_mean_Vietnam.csv'}
    DemandName = FullDemandList[region_name1]
    SolarCFsName = '20201218_' + str(region_name2) + '_mthd3_solar.csv'
    WindCFsName = '20201218_' + str(region_name2) + '_mthd3_wind.csv'
    return DemandName, SolarCFsName, WindCFsName



def update_series(case_dic, tech_dic):
    series = read_csv_dated_data_file(case_dic['year_start'],
                                      case_dic['month_start'],
                                      case_dic['day_start'],
                                      case_dic['hour_start'],
                                      case_dic['year_end'],
                                      case_dic['month_end'],
                                      case_dic['day_end'],
                                      case_dic['hour_end'],
                                      case_dic['data_path'],
                                      tech_dic['series_file'])
    if 'normalization' in tech_dic:
        if tech_dic['normalization'] >= 0.0:
            series = series * tech_dic['normalization']/np.average(series)
    tech_dic['series'] = series


def update_timenum(case_dic):
    num_time_periods = (24 * (
            datetime.date(case_dic['year_end'],case_dic['month_end'],case_dic['day_end']) - 
            datetime.date(case_dic['year_start'],case_dic['month_start'],case_dic['day_start'])
            ).days +
            (case_dic['hour_end'] - case_dic['hour_start'] ) + 1)
    return num_time_periods







def update_series_ERA5(case_dic, tech_dic, case_name): 

    num_time_periods = update_timenum(case_dic) 
    
    series1 = read_csv_dated_data_file(case_dic['year_start'],case_dic['month_start'],case_dic['day_start'],case_dic['hour_start'],
                                       case_dic['year_end'],  case_dic['month_end'],  case_dic['day_end'],  case_dic['hour_end'],
                                       case_dic['data_path'], case_name[0]) 
    series2 = read_csv_dated_data_file(case_dic['year_start'],case_dic['month_start'],case_dic['day_start'],case_dic['hour_start'],
                                       case_dic['year_end'],  case_dic['month_end'],  case_dic['day_end'],  case_dic['hour_end'],
                                       case_dic['data_path'], case_name[1]) 
    
    # Interpolate to 0.5
    time_old = np.arange(num_time_periods) 

    time_new = time_old + 0.5 

    series2_new = np.interp(time_new, time_old, series2) 

    # Scale
    series2_new = series2_new * np.average(series1)/np.average(series2_new) 

    tech_dic['series'] = series2_new 

    

def update_series_ERA52(case_dic, tech_dic, case_name): 

    num_time_periods = update_timenum(case_dic) 

    series2 = read_csv_dated_data_file(case_dic['year_start'],case_dic['month_start'],case_dic['day_start'],case_dic['hour_start'],
                                       case_dic['year_end'],  case_dic['month_end'],  case_dic['day_end'],  case_dic['hour_end'],
                                       case_dic['data_path'], case_name[1]) 
    
    # Interpolate to 0.5
    time_old = np.arange(num_time_periods) 

    time_new = time_old + 0.5 

    series2_new = np.interp(time_new, time_old, series2) 

    tech_dic['series'] = series2_new 