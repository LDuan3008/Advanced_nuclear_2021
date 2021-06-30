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


def GetCFsName(region_name):
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
    FullSolCFsList = {'DZ': 'solar_cf_Dan_normalized_to_0.29_mean_Algeria.csv', 'AR': 'solar_cf_Dan_normalized_to_0.27_mean_Argentina.csv',
                      'AU': 'solar_cf_Dan_normalized_to_0.29_mean_Australia.csv', 'BR': 'solar_cf_Dan_normalized_to_0.25_mean_Brazil.csv',
                      'CA': 'solar_cf_Dan_normalized_to_0.17_mean_Canada.csv', 'CL': 'solar_cf_Dan_normalized_to_0.33_mean_Chile.csv',
                      'CN': 'solar_cf_Dan_normalized_to_0.27_mean_China.csv', 'CO': 'solar_cf_Dan_normalized_to_0.21_mean_Colombia.csv',
                      'EG': 'solar_cf_Dan_normalized_to_0.31_mean_Egypt.csv', 'FR': 'solar_cf_Dan_normalized_to_0.21_mean_France.csv',
                      'DE': 'solar_cf_Dan_normalized_to_0.19_mean_Germany.csv', 'GH': 'solar_cf_Dan_normalized_to_0.21_mean_Ghana.csv',
                      'IN': 'solar_cf_Dan_normalized_to_0.26_mean_India.csv', 'ID': 'solar_cf_Dan_normalized_to_0.2_mean_Indonesia.csv',
                      'IR': 'solar_cf_Dan_normalized_to_0.3_mean_Iran.csv', 'IT': 'solar_cf_Dan_normalized_to_0.24_mean_Italy.csv',
                      'JP': 'solar_cf_Dan_normalized_to_0.22_mean_Japan.csv', 'LY': 'solar_cf_Dan_normalized_to_0.3_mean_Libya.csv',
                      'MY': 'solar_cf_Dan_normalized_to_0.19_mean_Malaysia.csv', 'MX': 'solar_cf_Dan_normalized_to_0.28_mean_Mexico.csv',
                      'MA': 'solar_cf_Dan_normalized_to_0.3_mean_Morocco.csv', 'MZ': 'solar_cf_Dan_normalized_to_0.28_mean_Mozambique.csv',
                      'NZ': 'solar_cf_Dan_normalized_to_0.22_mean_New Zealand.csv', 'NG': 'solar_cf_Dan_normalized_to_0.24_mean_Nigeria.csv',
                      'PY': 'solar_cf_Dan_normalized_to_0.25_mean_Paraguay.csv', 'PE': 'solar_cf_Dan_normalized_to_0.28_mean_Peru.csv',
                      'PL': 'solar_cf_Dan_normalized_to_0.18_mean_Poland.csv', 'RU': 'solar_cf_Dan_normalized_to_0.16_mean_Russia.csv',
                      'SA': 'solar_cf_Dan_normalized_to_0.3_mean_Saudi Arabia.csv', 'ZA': 'solar_cf_Dan_normalized_to_0.3_mean_South Africa.csv',
                      'KR': 'solar_cf_Dan_normalized_to_0.23_mean_South Korea.csv', 'ES': 'solar_cf_Dan_normalized_to_0.26_mean_Spain.csv',
                      'SD': 'solar_cf_Dan_normalized_to_0.3_mean_Sudan.csv', 'SE': 'solar_cf_Dan_normalized_to_0.15_mean_Sweden.csv',
                      'TH': 'solar_cf_Dan_normalized_to_0.22_mean_Thailand.csv', 'TN': 'solar_cf_Dan_normalized_to_0.28_mean_Tunisia.csv',
                      'TR': 'solar_cf_Dan_normalized_to_0.27_mean_Turkey.csv', 'UA': 'solar_cf_Dan_normalized_to_0.2_mean_Ukraine.csv',
                      'GB': 'solar_cf_Dan_normalized_to_0.17_mean_United Kingdom.csv', 'US': 'solar_cf_Dan_normalized_to_0.25_mean_United States.csv',
                      'VE': 'solar_cf_Dan_normalized_to_0.24_mean_Venezuela.csv', 'VN': 'solar_cf_Dan_normalized_to_0.21_mean_Vietnam.csv'}
    FullWinCFsList = {'DZ': 'wind_cf_Dan_normalized_to_0.36_mean_Algeria.csv', 'AR': 'wind_cf_Dan_normalized_to_0.43_mean_Argentina.csv',
                      'AU': 'wind_cf_Dan_normalized_to_0.38_mean_Australia.csv', 'BR': 'wind_cf_Dan_normalized_to_0.18_mean_Brazil.csv',
                      'CA': 'wind_cf_Dan_normalized_to_0.32_mean_Canada.csv', 'CL': 'wind_cf_Dan_normalized_to_0.3_mean_Chile.csv',
                      'CN': 'wind_cf_Dan_normalized_to_0.29_mean_China.csv', 'CO': 'wind_cf_Dan_normalized_to_0.1_mean_Colombia.csv',
                      'EG': 'wind_cf_Dan_normalized_to_0.37_mean_Egypt.csv', 'FR': 'wind_cf_Dan_normalized_to_0.32_mean_France.csv',
                      'DE': 'wind_cf_Dan_normalized_to_0.37_mean_Germany.csv', 'GH': 'wind_cf_Dan_normalized_to_0.15_mean_Ghana.csv',
                      'IN': 'wind_cf_Dan_normalized_to_0.21_mean_India.csv', 'ID': 'wind_cf_Dan_normalized_to_0.15_mean_Indonesia.csv',
                      'IR': 'wind_cf_Dan_normalized_to_0.27_mean_Iran.csv', 'IT': 'wind_cf_Dan_normalized_to_0.22_mean_Italy.csv',
                      'JP': 'wind_cf_Dan_normalized_to_0.27_mean_Japan.csv', 'LY': 'wind_cf_Dan_normalized_to_0.34_mean_Libya.csv',
                      'MY': 'wind_cf_Dan_normalized_to_0.15_mean_Malaysia.csv', 'MX': 'wind_cf_Dan_normalized_to_0.21_mean_Mexico.csv',
                      'MA': 'wind_cf_Dan_normalized_to_0.27_mean_Morocco.csv', 'MZ': 'wind_cf_Dan_normalized_to_0.25_mean_Mozambique.csv',
                      'NZ': 'wind_cf_Dan_normalized_to_0.34_mean_New Zealand.csv', 'NG': 'wind_cf_Dan_normalized_to_0.24_mean_Nigeria.csv',
                      'PY': 'wind_cf_Dan_normalized_to_0.33_mean_Paraguay.csv', 'PE': 'wind_cf_Dan_normalized_to_0.1_mean_Peru.csv',
                      'PL': 'wind_cf_Dan_normalized_to_0.35_mean_Poland.csv', 'RU': 'wind_cf_Dan_normalized_to_0.3_mean_Russia.csv',
                      'SA': 'wind_cf_Dan_normalized_to_0.31_mean_Saudi Arabia.csv', 'ZA': 'wind_cf_Dan_normalized_to_0.33_mean_South Africa.csv',
                      'KR': 'wind_cf_Dan_normalized_to_0.25_mean_South Korea.csv', 'ES': 'wind_cf_Dan_normalized_to_0.26_mean_Spain.csv',
                      'SD': 'wind_cf_Dan_normalized_to_0.37_mean_Sudan.csv', 'SE': 'wind_cf_Dan_normalized_to_0.19_mean_Sweden.csv',
                      'TH': 'wind_cf_Dan_normalized_to_0.16_mean_Thailand.csv', 'TN': 'wind_cf_Dan_normalized_to_0.33_mean_Tunisia.csv',
                      'TR': 'wind_cf_Dan_normalized_to_0.19_mean_Turkey.csv', 'UA': 'wind_cf_Dan_normalized_to_0.34_mean_Ukraine.csv',
                      'GB': 'wind_cf_Dan_normalized_to_0.46_mean_United Kingdom.csv', 'US': 'wind_cf_Dan_normalized_to_0.38_mean_United States.csv',
                      'VE': 'wind_cf_Dan_normalized_to_0.16_mean_Venezuela.csv', 'VN': 'wind_cf_Dan_normalized_to_0.15_mean_Vietnam.csv'}
    
    DemandName = FullDemandList[region_name]
    SolarCFsName = FullSolCFsList[region_name]
    WindCFsName = FullWinCFsList[region_name]
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