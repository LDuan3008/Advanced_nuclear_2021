from Core_Model import core_model
from Extract_Cvxpy_Output import extract_cvxpy_output
from Save_Basic_Results import save_basic_results
import os

def run_model_main_fun(case_dic, tech_list):
    output_folder = case_dic['output_path'] + '/' + case_dic['case_name']
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print ('Macro_Energy_Model: Executing core model')
    constraint_list,cvxpy_constraints,cvxpy_prob,cvxpy_capacity_dic,cvxpy_dispatch_dic,cvxpy_stored_dic = core_model(case_dic, tech_list)
    prob_dic,capacity_dic,dispatch_dic,stored_dic = extract_cvxpy_output(case_dic,tech_list,constraint_list,cvxpy_constraints,cvxpy_prob,cvxpy_capacity_dic,cvxpy_dispatch_dic,cvxpy_stored_dic)
    print ('Simple_Energy_Model: Saving basic results')
    [[input_case_dic,  input_tech_list,  input_time_dic],
     [results_case_dic,results_tech_dic,results_time_dic]] = save_basic_results(case_dic, tech_list, cvxpy_constraints,prob_dic,capacity_dic,dispatch_dic,stored_dic)
