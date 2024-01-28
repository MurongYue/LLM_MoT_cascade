from prompting.date import *
from utils import *

if __name__ == '__main__':
    M = 8  # example number
    N = 20  # SC number
    data_cot11 = read_json('GPT3_result/date_cot1_t=0.4.json')
    data_cot12 = read_json('GPT3_result/date_cot1_t=0.4.json')
    data_cot21 = read_json('GPT3_result/date_cot2_t=0.4.json')
    data_cot22 = read_json('GPT3_result/date_cot2_t=0.4.json')
    data_pot11 = read_json('GPT3_result/date_pot1_t=0.4.json')
    data_pot12 = read_json('GPT3_result/date_pot1_t=0.4.json')
    data_pot21 = read_json('GPT3_result/date_pot2_t=0.4.json')
    data_pot22 = read_json('GPT3_result/date_pot2_t=0.4.json')
    gpt4_cot1 = read_json('GPT4_result/date_cot1.json')
    gpt4_cot2 = read_json('GPT4_result/date_cot2.json')
    gpt4_pot1 = read_json('GPT4_result/date_pot1.json')
    gpt4_pot2 = read_json('GPT4_result/date_pot2.json')
    gpt4_cot1_greedy = read_json('GPT4_result/date_greedy_cot1.json')
    gpt4_cot2_greedy = read_json('GPT4_result/date_greedy_cot2.json')
    gpt4_pot1_greedy = read_json('GPT4_result/date_greedy_pot1.json')
    gpt4_pot2_greedy = read_json('GPT4_result/date_greedy_pot2.json')
    data_list = [data_cot11, data_cot12, data_cot21, data_cot22, data_pot11, data_pot12,
                 data_pot21, data_pot22, gpt4_cot1, gpt4_cot2, gpt4_pot1, gpt4_pot2, gpt4_cot1_greedy,
                 gpt4_cot2_greedy, gpt4_pot1_greedy, gpt4_pot2_greedy]
    cot_prompt_list = [date_CoT1_prompting, date_CoT2_prompting]
    pot_prompt_list = [date_PoT1_prompting, date_PoT2_prompting]
    eval_acc_cost(threshold_list=[0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.9, 1], M=M, N=N, data_list=data_list,
                  cot_prompt_list=cot_prompt_list, pot_prompt_list=pot_prompt_list)
