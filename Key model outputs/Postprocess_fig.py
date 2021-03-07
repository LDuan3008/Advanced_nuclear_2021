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

# color_list = {'natgas_cap':'black', 'natgas_tot':'black',
#               'natgas_ccs_cap':'grey', 'natgas_ccs_tot':'grey',
#               'solar_cap':'wheat', 'solar_fix':'wheat',
#               'wind_cap':'skyblue', 'wind_fix':'skyblue',
#               'conventional_nuclear_cap':'brown', 'conventional_nuclear_fix':'brown',
#                 'nuclear_cap':'tomato', 'nuclear_fix':'tomato',
#                 'nuclear_generator_cap':'limegreen', 'nuclear_generator_fix':'limegreen',
#                 'resistant_heater_cap':'darkblue', 'resistant_heater_fix':'darkblue',
#                 'storage_cap':'indigo', 'storage_fix':'indigo',
#                 'heat_storage_cap':'violet', 'heat_storage_fix':'violet',
#                 'system_cost':'black',
#                 'lost_load_var':'cadetblue'}

def Scenario1Fig1(default_case_name, summary_table, type):

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

    if type == 'SysCos':
        for idx in range(6):
            sc1 = summary_table[idx]['system_cost']
            sc2 = summary_table[idx+6]['system_cost']
            plt.plot(x_axis, sc1, color='black')
            plt.plot(x_axis, sc2, color='black', linestyle='--')
            plt.xticks( xticks )
            plt.xlim(0, 1)
            plt.ylim(0, 0.14)
            # plt.show() 
            # plt.savefig(default_case_name+str(idx)+'.png', dpi=1500)
            plt.savefig(default_case_name+str(idx)+'.ps')
            plt.clf() 

    for idx in range(NumOfCases):

        CurrentCase = summary_table[idx]
        starting_idx = 0

        if type == 'cap':
            ax1 = plt.subplot(111)
            ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_cap'])[starting_idx:]), color='black')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_ccs_cap'])[starting_idx:]), color='grey')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['solar_cap'])[starting_idx:]), color='wheat')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['wind_cap'])[starting_idx:]), color='skyblue')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['conventional_nuclear_cap'])[starting_idx:]), color='brown')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_cap'])[starting_idx:]), color='tomato')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_generator_REAmatch_cap'])[starting_idx:]) +
                             nonan(np.array(CurrentCase['nuclear_generator_TESmatch_cap'])[starting_idx:]), color='limegreen')
            ax2 = ax1.twinx()
            ax2.plot(x_axis, nonan(np.array(CurrentCase['storage_cap'])[starting_idx:]), color='violet', linestyle='--')
            ax2.plot(x_axis, nonan(np.array(CurrentCase['heat_storage_cap'])[starting_idx:]), color='indigo', linestyle='--')
            ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax1.set_xticks( xticks )
            ax1.set_xlim(0, 1)
            # ax1.set_ylim(0, 4) 
            ax1.set_ylim(0, 2.5)
            ax2.set_ylim(0, 3)
            # plt.show()
            # plt.savefig(default_case_name+str(idx)+'_cap.png', dpi=1500)
            plt.savefig(default_case_name+str(idx)+'_cap.ps')
            plt.clf()

        if type == 'cost':
            y_lists = [np.array(CurrentCase['natgas_tot']), 
                       np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']), 
                       np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['conventional_nuclear_fix']), 
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                       np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                       np.array(CurrentCase['lost_load_var'])
                       ]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'violet', 'tomato', 'indigo', 'cadetblue']
            ax1 = plt.subplot(111)
            ax1.stackplot(x_axis, y_lists, colors=y_color)
            ax1.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax1.set_xticks( xticks )
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 0.14)
            # plt.show()
            # plt.savefig(default_case_name+name+str(idx)+'_cost.png', dpi=1500)
            plt.savefig(default_case_name+str(idx)+'_cost.ps')
            plt.clf()



def Scenario1Fig2(DicNew):

    def ReshapeData(TS, choice):
        TS_reshape = TS.reshape(-1, 24)
        if choice == 0:
            return np.mean(TS_reshape, axis=0)
        if choice == 1:
            return np.mean(TS_reshape, axis=1)
        if choice == 2:
            return np.array(TS)
    
    choice_lengh = {0:24, 1:365, 2:8760}
    choice = 2
    xaxisn = choice_lengh[choice]
    FirstDayofMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    for idx in range(len(DicNew)):
        plt.stackplot( np.arange(xaxisn), 
                       ReshapeData(DicNew[idx]['conventional_nuclear_potential'], choice), 
                       ReshapeData(DicNew[idx]['advanced_nuclear_potential'], choice), 
                       ReshapeData(DicNew[idx]['heat_storage_dispatch'], choice), 
                       ReshapeData(DicNew[idx]['solar_potential'], choice), 
                       ReshapeData(DicNew[idx]['wind_potential'], choice), 
                       ReshapeData(DicNew[idx]['natgas_dispatch'], choice), 
                       ReshapeData(DicNew[idx]['natgas_ccs_dispatch'], choice), 
                       ReshapeData(DicNew[idx]['storage_dispatch'], choice),
                       ReshapeData(DicNew[idx]['lost_load_dispatch'], choice),
                       colors = ['brown', 'tomato', 'indigo', 'wheat', 'skyblue', 'black', 'grey', 'violet', 'cadetblue'] )
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
        plt.savefig('Dispatch'+str(idx)+'.ps') 
        # plt.savefig('Dispatch'+str(idx)+'.png', dpi=1500) 
        plt.clf()



def Scenario1Fig3(ToDrawArray, MaxVal):
    # Let's first remove the 1.0, 0.1, 0.01 to get equal intervals
    # ToDrawArray = np.delete(ToDrawArray, (-2), axis=1)
    # ToDrawArray = np.delete(ToDrawArray, (-2), axis=1)
    # ToDrawArray = np.delete(ToDrawArray, (-2), axis=1)
    Xarray, Yarray = [], []
    for idx in range(ToDrawArray.shape[0]):
        TakeCty = ToDrawArray[idx]
        WhereIsNan = np.isnan(TakeCty)
        TakeCty[WhereIsNan] = 0.0
        idx_max = np.argmax(ToDrawArray[idx])
        Xarray.append(idx+0.5)
        Yarray.append(idx_max+0.5)
    ToDrawArray = np.ma.masked_equal(ToDrawArray, 0)
    ax1 = plt.subplot(111)
    mp = ax1.pcolormesh(ToDrawArray, cmap='Reds', edgecolors='grey', linewidths='0.1', vmin=0, vmax=MaxVal)
    ax1.scatter(Yarray, Xarray, s=10, marker=(5, 1), edgecolors='black', linewidths='0.1')
    start=30; end=55
    ax1.set_xlim(start, end)
    ax1.set_xticks( np.arange(end-start)+start+0.5 )
    ax1.set_yticks( np.arange(ToDrawArray.shape[0])+0.5 )
    plt.colorbar(mp, ax=ax1, extend='max', shrink=0.8, orientation='vertical')
    # ax1.set_aspect('equal')
    # plt.show() 
    plt.savefig('test.ps') 
    plt.clf()






def Scenario3Fig1(info, CaseIdx):

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

    def plotP(var, col, name):
        ax1 = plt.subplot(111, projection=ccrs.PlateCarree())
        ax1.add_feature(cfeature.COASTLINE)
        ax1.add_feature(cfeature.BORDERS)
        ax1.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
        mp = ax1.pcolor(lon, lat, np.ma.masked_equal(var, 0), cmap=col, norm=colors.Normalize(vmin=0, vmax=1.5), transform=ccrs.PlateCarree())
        ax1.contourf(lon, lat, mask_array_new, colors='none', hatches=['.'*5], transform=ccrs.PlateCarree())
        plt.colorbar(mp, ax=ax1, extend='max', shrink=0.5, orientation='vertical')
        # plt.show()
        # plt.savefig(name+'.png', dpi=1500)
        plt.savefig(name+'.ps')
        plt.clf()

    for CaseIdx in CaseIdx:
        map_plot_co2emit = info['natgas_cap'][:, CaseIdx, 0] + info['natgas_ccs_cap'][:, CaseIdx, 0]
        map_plot_solar   = info['solar_cap'][:, CaseIdx, 0]
        map_plot_wind    = info['wind_cap'][:, CaseIdx, 0]
        map_plot_nuclear = info['nuclear_cap'][:, CaseIdx, 0] + info['conventional_nuclear_cap'][:, CaseIdx, 0]
        map_plot_storage = info['heat_storage_cap'][:, CaseIdx, 0] + info['storage_cap'][:, CaseIdx, 0]

        total_mask_co2emitting = np.zeros([len(lat), len(lon)])
        total_mask_solar = np.zeros([len(lat), len(lon)])
        total_mask_wind = np.zeros([len(lat), len(lon)])
        total_mask_heat_source = np.zeros([len(lat), len(lon)])
        total_mask_all_storage = np.zeros([len(lat), len(lon)])
        mask_array = np.zeros([len(lat), len(lon)]) # masked no data regions
        for idx_idx in range(len(find_idx_list)):
            new_mask = np.copy(mask)
            mask_new = MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
            total_mask_co2emitting = total_mask_co2emitting + map_plot_co2emit[idx_idx] * mask_new
            total_mask_solar       = total_mask_solar       + map_plot_solar[idx_idx]   * mask_new
            total_mask_wind        = total_mask_wind        + map_plot_wind[idx_idx]    * mask_new
            total_mask_heat_source = total_mask_heat_source + map_plot_nuclear[idx_idx] * mask_new
            total_mask_all_storage = total_mask_all_storage + map_plot_storage[idx_idx] * mask_new
            mask_array = mask_array + MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
        mask_array_new = np.ma.masked_equal(mask_array + ocean_mask, 1)

        plotP(total_mask_co2emitting, 'Greys', 'natgasMAP_'+str(CaseIdx)) 
        plotP(total_mask_solar, 'Reds', 'solarMAP_'+str(CaseIdx)) 
        plotP(total_mask_wind, 'Blues', 'windMAP_'+str(CaseIdx)) 
        plotP(total_mask_heat_source, 'Oranges', 'nuclearMAP_'+str(CaseIdx)) 
        plotP(total_mask_all_storage, 'Purples', 'generatorMAP_'+str(CaseIdx)) 


def Scenario3Fig2(solar_cap, wind_cap, nuclear_cap):
    x1, x2 = -1, 42
    y1, y2 = -1.5, 1.0
    TotNumCty = solar_cap.shape[0]
    xaxis1 = np.arange(TotNumCty)
    print (xaxis1)
    ax1 = plt.subplot(311);                         ax1.bar(xaxis1, solar_cap[:, 0],   yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='wheat');   ax1.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax2 = plt.subplot(312, sharex=ax1, sharey=ax1); ax2.bar(xaxis1, wind_cap[:, 0],    yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='skyblue'); ax2.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1); ax3.bar(xaxis1, nuclear_cap[:, 0], yerr=solar_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='tomato');  ax3.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax1.set_xlim(x1, x2); ax1.set_ylim(y1, y2)
    ax1.set_xticks(xaxis1)
    ax1.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0])
    # plt.show() 
    plt.savefig('diff.ps') 
    plt.clf()

def Scenario3Fig2_tes(tes_cap):
    x1, x2 = -1, 42
    y1, y2 = -7.0, 5.0
    TotNumCty = tes_cap.shape[0]
    xaxis1 = np.arange(TotNumCty)

    ax1 = plt.subplot(111)
    ax1.bar(xaxis1, tes_cap[:, 0], yerr=tes_cap[:, 1], width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='purple')
    ax1.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)

    ax1.set_xlim(x1, x2); ax1.set_ylim(y1, y2)
    ax1.set_xticks(xaxis1)
    # ax1.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0])
    # plt.show() 
    plt.savefig('diff2.ps') 
    plt.clf()


def Scenario3Fig3(sys_cost_diff):

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
    mask_ocean = MV.masked_equal(ocean_mask, 1) + 1

    def plotP(var, col, name):
        ax1 = plt.subplot(111, projection=ccrs.PlateCarree())
        ax1.add_feature(cfeature.COASTLINE)
        ax1.add_feature(cfeature.BORDERS)
        ax1.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
        mp = ax1.pcolor(lon, lat, np.ma.masked_equal(var, 0), cmap=col, norm=colors.Normalize(vmin=0, vmax=12), transform=ccrs.PlateCarree())
        ax1.contourf(lon, lat, mask_array_new, colors='none', hatches=['.'*5], transform=ccrs.PlateCarree())
        plt.colorbar(mp, ax=ax1, extend='max', shrink=0.5, orientation='vertical')
        # plt.show()
        # plt.savefig(name+'.png', dpi=1500)
        plt.savefig(name+'.ps')
        plt.clf()

    for CaseIdx in range(1):
        total_mask_sc = np.zeros([len(lat), len(lon)])
        mask_array = np.zeros([len(lat), len(lon)])
        for idx_idx in range(len(find_idx_list)):
            new_mask = np.copy(mask)
            find_region = MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1
            mask_new = MV.filled(find_region * mask_ocean, 0)
            total_mask_sc = total_mask_sc + sys_cost_diff[idx_idx] * mask_new
            mask_array = mask_array + MV.filled(MV.masked_not_equal(new_mask, find_idx_list[idx_idx]) * 0. + 1, 0)
        mask_array_new = np.ma.masked_equal(mask_array + ocean_mask, 1)
        plotP(total_mask_sc, 'Reds', 'system_cost'+str(CaseIdx)) 


def Scenario3Fig4(info):
    # Find cty size
    f_axis = cdms.open('SWGDN.nc')
    v=f_axis('SWGDN')
    lat, lon=v.getAxis(1), v.getAxis(2)
    bounds_lat = lat.getBounds() 
    bounds_lon = lon.getBounds() 
    f_axis.close()
    world_countries_array = regionmask.defined_regions.natural_earth.countries_110
    mask = np.array(world_countries_array.mask(lon, lat, wrap_lon=False))
    name = world_countries_array.names

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

    solar_cap05,   solar_cap00   = info['solar_cap'][:,1,0],   info['solar_cap'][:,2,0]
    wind_cap05,    wind_cap00    = info['wind_cap'][:,1,0],    info['wind_cap'][:,2,0]
    nuclear_cap05, nuclear_cap00 = info['nuclear_cap'][:,1,0], info['nuclear_cap'][:,2,0]
    for find_idx in range(len(find_idx_list)):
        plt.scatter( (nuclear_cap00-nuclear_cap05)[find_idx], (solar_cap00-solar_cap05)[find_idx], s=tot_area_list[find_idx]/2e10, c='wheat',   edgecolor='black')
        # plt.scatter( (nuclear_cap00-nuclear_cap05)[find_idx], (wind_cap00-wind_cap05)[find_idx],   s=tot_area_list[find_idx]/2e10, c='skyblue', edgecolor='black')
        if tot_area_list[find_idx] > np.mean(tot_area_list):
            print (find_idx, TwoLettersCode[find_idx], tot_area_list[find_idx])
            plt.text((nuclear_cap00-nuclear_cap05)[find_idx], (solar_cap00-solar_cap05)[find_idx], TwoLettersCode[find_idx])
            # plt.text((nuclear_cap00-nuclear_cap05)[find_idx], (wind_cap00-wind_cap05)[find_idx],      TwoLettersCode[find_idx])
    plt.plot(np.r_[0.0, 1.2], np.r_[0, 0], color='black', linewidth=1)
    plt.xlim(0.0, 1.2)
    plt.ylim(-1.2, 0.8)
    # plt.show() 
    plt.savefig('test1.ps') 
    plt.clf()







def Scenario4Fig1(default_case_name, summary_table, type):

    NumOfCases = len(summary_table)

    xlist = np.array([10**(-3), 10**(-2.8), 10**(-2.6), 10**(-2.4), 10**(-2.2),
                      10**(-2), 10**(-1.8), 10**(-1.6), 10**(-1.4), 10**(-1.2),
                      10**(-1), 10**(-0.8), 10**(-0.6), 10**(-0.4), 10**(-0.2),
                      10**0,    10**0.2,    10**0.4,    10**0.6,    10**0.8,
                      10**1])
    x_axis = np.log10(xlist)
    xticks = x_axis
    print (x_axis) 

    for idx in range(NumOfCases):

        CurrentCase = summary_table[idx]
        starting_idx = 0

        if type == 'cost_lostload':
            y_lists = [np.array(CurrentCase['natgas_tot']), 
                       np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']), 
                       np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['conventional_nuclear_fix']), 
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                       np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                       np.array(CurrentCase['lost_load_var'])
                       ]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'indigo', 'tomato', 'violet', 'cadetblue']
        
        if type == 'cost_loadshift':
            y_lists = [np.array(CurrentCase['natgas_tot']), 
                       np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']), 
                       np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['conventional_nuclear_fix']), 
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                       np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                       np.array(CurrentCase['lost_load_var']),
                       np.array(CurrentCase['shift_load_tot'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'indigo', 'tomato', 'violet', 'cadetblue', 'darkslategray']

        ax1 = plt.subplot(111)
        ax1.stackplot(x_axis, y_lists, colors=y_color)
        ax1.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
        ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
        ax1.set_xticks( xticks )
        ax1.set_xlim(-3, 1)
        ax1.set_ylim(0, 0.14)
        plt.show()
        # plt.savefig(default_case_name+name+str(idx)+'_cost.png', dpi=1500)
        # plt.savefig(default_case_name+str(idx)+'_cost.ps')
        plt.clf()


def Scenario4Fig2(ToDrawArray, MaxVal, name):
    unmet_demand_cost = [10**(-3), 10**(-2.8), 10**(-2.6), 10**(-2.4), 10**(-2.2),
                         10**(-2), 10**(-1.8), 10**(-1.6), 10**(-1.4), 10**(-1.2),
                         10**(-1), 10**(-0.8), 10**(-0.6), 10**(-0.4), 10**(-0.2),
                         10**0,    10**0.2,    10**0.4,    10**0.6,    10**0.8,
                         10**1]
    ToDraw_S = np.zeros([42, len(unmet_demand_cost)])
    ToDraw_W = np.zeros([42, len(unmet_demand_cost)])
    ToDraw_N = np.zeros([42, len(unmet_demand_cost)])
    Xarray, Yarray = [], []
    for idx in range(42):
        ToDraw_S[idx] = np.array(ToDrawArray[idx]['solar_cap'])
        ToDraw_W[idx] = np.array(ToDrawArray[idx]['wind_cap'])
        ToDraw_N[idx] = np.array(ToDrawArray[idx]['nuclear_cap'])
    ToDraw_S = np.ma.masked_equal(ToDraw_S, 0)
    ToDraw_W = np.ma.masked_equal(ToDraw_W, 0)
    ToDraw_N = np.ma.masked_equal(ToDraw_N, 0)
    ax1 = plt.subplot(131)
    ax2 = plt.subplot(132,sharex=ax1,sharey=ax1)
    ax3 = plt.subplot(133,sharex=ax1,sharey=ax1)
    mp1 = ax1.pcolormesh(ToDraw_S, cmap='Reds', edgecolors='grey', linewidths='0.1', vmin=0, vmax=MaxVal)
    mp2 = ax2.pcolormesh(ToDraw_W, cmap='Reds', edgecolors='grey', linewidths='0.1', vmin=0, vmax=MaxVal)
    mp3 = ax3.pcolormesh(ToDraw_N, cmap='Reds', edgecolors='grey', linewidths='0.1', vmin=0, vmax=MaxVal)
    plt.colorbar(mp3, ax=ax3, extend='max', shrink=0.8, orientation='vertical')
    ax1.set_xlim(0, len(unmet_demand_cost))
    ax1.set_xticks(np.arange(len(unmet_demand_cost))+0.5)
    ax1.set_xticklabels([''])
    ax1.set_ylim(0, 42)
    ax1.set_yticks(np.arange(42)+0.5 )
    ax1.set_yticklabels([''])
    # plt.show()
    plt.savefig(name+'.ps') 
    plt.clf() 











def Scenario5Fig1(default_case_name, summary_table, type):

    NumOfCases = len(summary_table)

    xlist = np.array([100, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
                  80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
                  60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
                  38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
                  16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]

    for idx in range(NumOfCases):

        CurrentCase = summary_table[idx]
        starting_idx = 0

        if type == 'cap':
            ax1 = plt.subplot(111)
            ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_cap'])[starting_idx:]), color='black')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['natgas_ccs_cap'])[starting_idx:]), color='grey')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['solar_cap'])[starting_idx:]), color='wheat')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['wind_cap'])[starting_idx:]), color='skyblue')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['conventional_nuclear_cap'])[starting_idx:]), color='brown')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_cap'])[starting_idx:]), color='tomato')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['nuclear_generator_REAmatch_cap'])[starting_idx:]) +
                             nonan(np.array(CurrentCase['nuclear_generator_TESmatch_cap'])[starting_idx:]), color='limegreen')
            ax1.plot(x_axis, nonan(np.array(CurrentCase['Resistant Heater_cap'])[starting_idx:]), color='darkblue')
            ax2 = ax1.twinx()
            ax2.plot(x_axis, nonan(np.array(CurrentCase['storage_cap'])[starting_idx:]), color='indigo', linestyle='--')
            ax2.plot(x_axis, nonan(np.array(CurrentCase['heat_storage_cap'])[starting_idx:]), color='violet', linestyle='--')
            ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax1.set_xticks( xticks )
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 4)
            ax2.set_ylim(0, 3)
            # plt.show()
            # plt.savefig(default_case_name+name+str(idx)+'_cap.png', dpi=1500)
            plt.savefig(default_case_name+str(idx)+'_cap.ps')
            plt.clf()

        if type == 'cost':
            y_lists = [np.array(CurrentCase['natgas_tot']), 
                       np.array(CurrentCase['natgas_ccs_tot']), 
                       np.array(CurrentCase['solar_fix']), 
                       np.array(CurrentCase['wind_fix']), 
                       np.array(CurrentCase['conventional_nuclear_fix']), 
                       np.array(CurrentCase['storage_fix']),
                       np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                       np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                       np.array(CurrentCase['lost_load_var']),
                       np.array(CurrentCase['Resistant Heater_fix'])]
            y_color = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'indigo', 'tomato', 'violet', 'cadetblue', 'darkblue']
            ax1 = plt.subplot(111)
            ax1.stackplot(x_axis, y_lists, colors=y_color)
            ax1.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax1.set_xticks( xticks )
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 0.14)
            # plt.show()
            # plt.savefig(default_case_name+name+str(idx)+'_cost.png', dpi=1500)
            plt.savefig(default_case_name+str(idx)+'_cost.ps')
            plt.clf()




def Scenario8Fig1(default_case_name, summary_table):
    sp, wp, nu = [], [], []
    for idx in range(42):
        sp.append(summary_table[idx]['solar_cap'][0])
        wp.append(summary_table[idx]['wind_cap'][0])
        nu.append(summary_table[idx]['nuclear_cap'][0])
    TotNumCty = 42
    xaxis1 = np.arange(TotNumCty)
    x1, x2 = -1, 42
    y1, y2 = 0, 3
    ax1 = plt.subplot(311);                         ax1.bar(xaxis1, np.array(sp), width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='wheat');   ax1.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax2 = plt.subplot(312, sharex=ax1, sharey=ax1); ax2.bar(xaxis1, np.array(wp), width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='skyblue'); ax2.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1); ax3.bar(xaxis1, np.array(nu), width=0.8, error_kw=dict(lw=1, capsize=1, capthick=0.8), color='tomato');  ax3.plot(np.r_[x1, x2], np.r_[0,0], color='black', linewidth=1)
    ax1.set_xlim(x1, x2); ax1.set_ylim(y1, y2)
    ax1.set_xticks(xaxis1)
    ax1.set_yticks([0, 1, 2, 3])
    # plt.show() 
    plt.savefig('diff.ps') 
    plt.clf()




def showTableS2(dict, DicNew):

    xlist = np.array([100, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
                      80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
                      60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
                      38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
                      16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0])
    ylist = 100 - xlist

    # Find cty size
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
        std_s = np.std(current_info['solar series'])
        mean_w = np.mean(current_info['wind series'])
        std_w = np.std(current_info['wind series'])

        # When start using Nuclear;
        for sub_idx in range(len(ylist)):
            if current_info['nuclear_cap'][sub_idx] > 0:
                find_n = current_info['nuclear_cap'][sub_idx]
                find_c = ylist[sub_idx]
                break

        for sub_idx in range(len(ylist)):
            if current_info['nuclear_cap'][sub_idx] > 0.5:
                find_50 = ylist[sub_idx]
                break
        for sub_idx in range(len(ylist)):
            if current_info['nuclear_cap'][sub_idx] > 0.8:
                find_80 = ylist[sub_idx]
                break
        for sub_idx in range(len(ylist)):
            if current_info['nuclear_cap'][sub_idx] > 0.99:
                find_99 = ylist[sub_idx]
                break
        find_50p = np.nan
        DispatchNuclearPercentage= DicNew[cty_idx]
        for sub_idx in range(len(DispatchNuclearPercentage)):
            if DispatchNuclearPercentage[sub_idx] >= 50:
                find_50p = ylist[sub_idx]
                break
        find_80p = np.nan
        DispatchNuclearPercentage= DicNew[cty_idx]
        for sub_idx in range(len(DispatchNuclearPercentage)):
            if DispatchNuclearPercentage[sub_idx] >= 80:
                find_80p = ylist[sub_idx]
                break
        find_99p = np.nan
        DispatchNuclearPercentage= DicNew[cty_idx]
        for sub_idx in range(len(DispatchNuclearPercentage)):
            if DispatchNuclearPercentage[sub_idx] >= 99:
                find_99p = ylist[sub_idx]
                break
        
        print (find_50, find_80, find_99, find_50p, find_80p, find_99p)
        new_array_outputs[cty_idx, 0] = tota_a
        new_array_outputs[cty_idx, 1] = mean_s
        new_array_outputs[cty_idx, 2] = std_s
        new_array_outputs[cty_idx, 3] = mean_w
        new_array_outputs[cty_idx, 4] = std_w
        new_array_outputs[cty_idx, 5] = find_n
        new_array_outputs[cty_idx, 6] = find_c
        new_array_outputs[cty_idx, 7] = find_50
        new_array_outputs[cty_idx, 8] = find_80
        new_array_outputs[cty_idx, 9] = find_99
        new_array_outputs[cty_idx, 10] = find_50p
        new_array_outputs[cty_idx, 11] = find_80p
        new_array_outputs[cty_idx, 12] = find_99p

    # Save as CSV table
    # np.savetxt("TableS2.csv", new_array_outputs, fmt='%.5f', delimiter=",")


    # # Only wind and base data
    # size = new_array_outputs[:, 0]
    # ax1=plt.subplot(111)
    # ax1.scatter(new_array_outputs[:, 6], new_array_outputs[:, 3], c='royalblue', s=size/1e4, edgecolors='black', linewidths=0.1, alpha=0.8)
    # ax1.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    # ax1.set_xlim(-5, 100)
    # ax1.set_ylim(0, 0.6)
    # # plt.show() 
    # plt.savefig('wind_co2.ps') 
    # plt.clf()

    # # Check Cty names
    # size = new_array_outputs[:, 0]
    # mean_size = np.mean(size)
    # ax1 = plt.subplot(111)
    # ax1.scatter(new_array_outputs[:, 6], new_array_outputs[:, 3], c='tan', s=size/1e4, edgecolors='black', linewidths=0.1)
    # for i in range(42):
    #     if size[i]>mean_size*0.4 and size[i]<=mean_size*0.8:
    #         ax1.text(new_array_outputs[i, 6], new_array_outputs[i, 3], TwoLettersCode[i])
    # ax1.set_xlim(-5, 100)
    # ax1.set_ylim(0, 0.6)
    # plt.show() 
    # # plt.savefig('solar_wind_co2.png', dpi=2000) 
    # plt.clf()



    # Second try
    size = new_array_outputs[:, 0]
    scale = 1e5
    ax1=plt.subplot(321)
    ax1.scatter(new_array_outputs[:, 6], new_array_outputs[:, 3], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax1.scatter(new_array_outputs[:, 7], new_array_outputs[:, 3], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax1.scatter(new_array_outputs[:, 9], new_array_outputs[:, 3], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax1.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    ax2=plt.subplot(322, sharex=ax1, sharey=ax1)
    ax2.scatter(new_array_outputs[:, 6], new_array_outputs[:, 1], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax2.scatter(new_array_outputs[:, 7], new_array_outputs[:, 1], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax2.scatter(new_array_outputs[:, 9], new_array_outputs[:, 1], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax2.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    ax1.set_xlim(-5, 105)
    ax1.set_ylim(0, 0.6)
    ax3=plt.subplot(323) 
    ax3.scatter(new_array_outputs[:, 6], new_array_outputs[:, 4], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax3.scatter(new_array_outputs[:, 7], new_array_outputs[:, 4], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax3.scatter(new_array_outputs[:, 9], new_array_outputs[:, 4], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax3.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    ax4=plt.subplot(324, sharex=ax3, sharey=ax3)
    ax4.scatter(new_array_outputs[:, 6], new_array_outputs[:, 2], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax4.scatter(new_array_outputs[:, 7], new_array_outputs[:, 2], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax4.scatter(new_array_outputs[:, 9], new_array_outputs[:, 2], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax4.plot(np.r_[0, 0], np.r_[0.0, 0.6], color='black', linestyle='--', linewidth='1')
    ax3.set_xlim(-5, 105)
    ax3.set_ylim(0, 0.6)
    ax5=plt.subplot(325) 
    ax5.scatter(new_array_outputs[:, 6], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax5.scatter(new_array_outputs[:, 7], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax5.scatter(new_array_outputs[:, 9], new_array_outputs[:, 4]/new_array_outputs[:, 3], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax5.plot(np.r_[0, 0], np.r_[0.0, 1.5], color='black', linestyle='--', linewidth='1')
    ax6=plt.subplot(326, sharex=ax5, sharey=ax5)
    ax6.scatter(new_array_outputs[:, 6], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='tan', s=size/scale, edgecolors='black', linewidths=0.1)
    ax6.scatter(new_array_outputs[:, 7], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='lightcoral', s=size/scale, edgecolors='black', linewidths=0.1)
    ax6.scatter(new_array_outputs[:, 9], new_array_outputs[:, 2]/new_array_outputs[:, 1], c='firebrick', s=size/scale, edgecolors='black', linewidths=0.1)
    ax6.plot(np.r_[0, 0], np.r_[0.0, 1.5], color='black', linestyle='--', linewidth='1')
    ax5.set_xlim(-5, 105)
    ax5.set_ylim(0, 1.5)
    # plt.show() 
    # plt.savefig('solar_wind_co2.png', dpi=2000) 
    plt.savefig('solar_wind_co2.ps', dpi=2000) 
    plt.clf()

    # # Third Try
    # y_axis = new_array_outputs[:, 3] # Mena wind 
    # x_axis = new_array_outputs[:, 1] # Mena solar 
    # size = new_array_outputs[:, 0]
    # timing = new_array_outputs[:, 6]
    # plt.scatter(x_axis, y_axis, s=size/2e4, c=timing, cmap='YlOrBr', vmin=-40, vmax=100, edgecolors='black', linewidths=0.1)
    # plt.xlim(0, 0.4)
    # plt.ylim(0, 0.6)
    # plt.show()
    # plt.savefig('test.png', dpi=1000)
    # plt.clf()







def ScenarioNewFig1(default_case_name, summary_table, type):

    NumOfCases = len(summary_table)

    xlist = np.array([100, 98.0, 96.0, 94.0, 92.0, 90.0, 88.0, 86.0, 84.0, 82.0,
                  80.0, 78.0, 76.0, 74.0, 72.0, 70.0, 68.0, 66.0, 64.0, 62.0,
                  60.0, 58.0, 56.0, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0,
                  38.0, 36.0, 34.0, 32.0, 30.0, 28.0, 26.0, 24.0, 22.0, 20.0, 18.0,
                  16.0, 14.0, 12.0, 10.0, 8.0,  6.0,  4.0,  2.0,  1.0, 0.1, 0.01, 0.001, 0.0])/100
    x_axis = 1 - 0.5**( np.log(xlist)/np.log(0.2) )
    xticks_addition_org = np.array([50.0, 10.0, 1.0])/100
    xticks_addition_cov = 1 - 0.5**( np.log(xticks_addition_org)/np.log(0.2) )
    xticks = np.r_[[0, 0.5, 0.75, 1.0], xticks_addition_cov]

    for idx in range(NumOfCases):

        CurrentCase = summary_table[idx]
        starting_idx = 0

        if type == 'cost':
            ax1 = plt.subplot(111)
            
            try:
                y_lists1 = [np.array(CurrentCase['natgas_tot']), 
                            np.array(CurrentCase['natgas_ccs_tot']), 
                            np.array(CurrentCase['solar_fix']), 
                            np.array(CurrentCase['wind_fix']), 
                            np.array(CurrentCase['conventional_nuclear_fix']), 
                            np.array(CurrentCase['storage_fix']),
                            np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                            np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                            np.array(CurrentCase['lost_load_var'])]
                y_color1 = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'violet', 'tomato', 'indigo', 'cadetblue']
                ax1.stackplot(x_axis, y_lists1, colors=y_color1)
            except:
                try:
                    y_lists1 = [np.array(CurrentCase['natgas_tot']), 
                                np.array(CurrentCase['natgas_ccs_tot']), 
                                np.array(CurrentCase['conventional_nuclear_fix']), 
                                np.array(CurrentCase['storage_fix']),
                                np.array(CurrentCase['nuclear_fix'])+np.array(CurrentCase['nuclear_generator_REAmatch_fix']),
                                np.array(CurrentCase['heat_storage_fix'])+np.array(CurrentCase['nuclear_generator_TESmatch_fix']),
                                np.array(CurrentCase['lost_load_var'])]
                    y_color1 = ['black', 'grey', 'brown', 'violet', 'tomato', 'indigo', 'cadetblue']
                    ax1.stackplot(x_axis, y_lists1, colors=y_color1)
                except:
                    try:
                        y_lists1 = [np.array(CurrentCase['natgas_tot']), 
                                    np.array(CurrentCase['natgas_ccs_tot']), 
                                    np.array(CurrentCase['solar_fix']), 
                                    np.array(CurrentCase['wind_fix']), 
                                    np.array(CurrentCase['conventional_nuclear_fix']), 
                                    np.array(CurrentCase['storage_fix']),
                                    np.array(CurrentCase['lost_load_var'])]
                        y_color1 = ['black', 'grey', 'wheat', 'skyblue', 'brown', 'violet', 'cadetblue']
                        ax1.stackplot(x_axis, y_lists1, colors=y_color1)
                    except:
                        y_lists1 = [np.array(CurrentCase['natgas_tot']), 
                                    np.array(CurrentCase['natgas_ccs_tot']), 
                                    np.array(CurrentCase['conventional_nuclear_fix']), 
                                    np.array(CurrentCase['storage_fix']),
                                    np.array(CurrentCase['lost_load_var'])]
                        y_color1 = ['black', 'grey', 'brown', 'violet', 'cadetblue']
                        ax1.stackplot(x_axis, y_lists1, colors=y_color1)

            ax1.plot(x_axis, np.array(CurrentCase['system_cost']), color='black', linestyle='--')
            ax1.plot(x_axis, np.zeros(len(x_axis)), color='black')
            ax1.set_xticks( xticks )
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 0.22)
            # plt.show()
            plt.savefig(default_case_name+str(idx)+'_cost.ps')
            plt.clf()