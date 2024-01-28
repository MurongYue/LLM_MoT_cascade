import json
import pickle
import openai
import backoff
from time import sleep
from openai.error import RateLimitError
import func_timeout
from math import isclose
from collections import Counter
import tiktoken


def read_json(json_file):
    with open(json_file, 'r') as f:
        d = json.load(f)
    return d


def read_jsonl(jsonl_file):
    with open(jsonl_file) as f:
        data = [json.loads(line) for line in f]
    return data


def save_json(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


def save2pickle(pkl_file, data):
    with open(pkl_file, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_pickle(pkl_file):
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)
    return data


@backoff.on_exception(backoff.expo, RateLimitError)
def completions_with_backoff_V2(sys_prompt, user_prompt):
    got_res = False
    res = {'choices': []}
    try_time = 0
    while got_res is False and try_time < 100:
        try_time += 1
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n\nQuestion"],
                n=1
            )
            got_res = True
        except openai.error.InvalidRequestError:
            raise Exception("openai.error.InvalidRequestError")
        except RateLimitError:
            sleep(3)
        except Exception:
            sleep(3)
    return res


def get_gpt_turbo_response(sys_prompt, user_prompt):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    response = completions_with_backoff_V2(sys_prompt, user_prompt)
    if response["choices"] == []:
        return ""
    return response["choices"][0]["message"]['content']


def get_gpt_turbo_multiple_response(sys_prompt, user_prompt):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    response = completions_with_backoff_V2(sys_prompt, user_prompt)
    if response["choices"] == []:
        return ""
    return [response["choices"][i]["message"]['content'] for i in range(len(response["choices"]))]


def safe_execute(code_string: str, keys=None):
    def execute(x):
        try:
            exec(x)
            locals_ = locals()
            if keys is None:
                return locals_.get('ans', None)
            else:
                return [locals_.get(k, None) for k in keys]
        except Exception:
            return None

    try:
        ans = func_timeout.func_timeout(2, execute, args=(code_string,))
    except func_timeout.FunctionTimedOut:
        ans = None
    return ans


def floatify_ans(ans):
    if ans is None:
        return None
    elif type(ans) == dict:
        ans = list(ans.values())[0]
    elif type(ans) == bool:
        ans = ans
    elif type(ans) in [list, tuple]:
        if not ans:
            return None
        else:
            try:
                ans = float(ans[0])
            except Exception:
                ans = str(ans[0])
    else:
        try:
            ans = float(ans)
        except Exception:
            ans = str(ans)
    return ans


def convert_percent_to_decimal(percent_string):
    percent_string = percent_string.replace("%", "")
    return "0." + percent_string


def program_convert(raw_program):
    # Define a dictionary to map each instruction to its Python equivalent
    instruction_map = {
        "add": lambda x, y: f"{x}+{y}",
        "subtract": lambda x, y: f"{x}-{y}",
        "multiply": lambda x, y: f"{x}*{y}",
        "divide": lambda x, y: f"{x}/{y}",
        "exp": lambda x, y: f"{x}**{y}",
        "greater": lambda x, y: f"{x}>{y}",
        "table_average": lambda x, y: f"mean({x})",
        "table_max": lambda x, y: f"max({x})",
        "table_min": lambda x, y: f"min({x})",
        "table_sum": lambda x, y: f"sum({x})"
    }
    raw_program = raw_program.split('), ')
    # Generate Python code for each instruction in the raw_program list
    code = ""
    index = 0
    for instruction in raw_program:
        # Parse the instruction into its component parts
        instruction = instruction.replace(")", '')
        parts = instruction.split("(")
        op_name = parts[0]
        args_0, args_1 = parts[1].split(",")
        args_1 = args_1[1:]
        if args_0[0] == "#":
            cur_idx = args_0.split('#')[-1]
            args_0 = f'x_{cur_idx}'
        elif args_0[0] == "c":
            args_0 = args_0.split('const_')[-1]
        elif "%" in args_0:
            args_0 = convert_percent_to_decimal(args_0)
        if args_1[0] == "#":
            cur_idx = args_1.split('#')[-1]
            args_1 = f'x_{cur_idx}'
        elif args_1[0] == "c":
            args_1 = args_1.split('const_')[-1]
        elif args_1[0] == '-':
            args_1 = f"({args_1})"
        elif "%" in args_1:
            args_1 = convert_percent_to_decimal(args_1)
        # Generate the Python code for this instruction
        if index + 1 == len(raw_program):
            code += f"ans = {instruction_map[op_name](args_0, args_1)}"
        else:
            code += f"x_{index} = {instruction_map[op_name](args_0, args_1)}; "
            index += 1

    # Return the generated Python code
    return code


def finqa_equal(prediction,
                reference,
                include_percentage: bool = False,
                is_close: float = False) -> bool:
    if prediction is None:
        return False
    elif type(prediction) == bool:
        # bool questions
        if prediction:
            return reference == 'yes'
        else:
            return reference == 'no'
    elif type(reference) == str or type(prediction) == str:
        # string questions
        return prediction == reference
    else:
        # number questions
        if include_percentage:
            gt_result = [reference / 100, reference, reference * 100]
        else:
            gt_result = [reference]
        for item in gt_result:
            try:
                if is_close:
                    if isclose(item, prediction, rel_tol=0.001):
                        return True
                precision = min(get_precision(prediction), get_precision(item))
                if round(prediction, precision) == round(item, precision):
                    return True
            except Exception:
                continue
        return False


def get_precision(gt_ans: float) -> int:
    precision = 5
    if '.' in str(gt_ans):
        precision = len(str(gt_ans).split('.')[-1])
    return precision


enc_3 = tiktoken.encoding_for_model("gpt-3.5-turbo")
enc_4 = tiktoken.encoding_for_model("gpt-4")
gpt3_input_cost = 0.0015
gpt3_output_cost = 0.002
gpt4_input_cost = 0.03
gpt4_output_cost = 0.06


def get_real_cost(data, prompt, version, k=-1):
    if version == 'gpt-3.5-turbo':
        enc = enc_3
        input_cost = gpt3_input_cost
        output_cost = gpt3_output_cost
    elif version == 'gpt-4':
        enc = enc_4
        input_cost = gpt4_input_cost
        output_cost = gpt4_output_cost
    input_text = prompt
    input_token_num = len(enc.encode(input_text))
    total_cost = 0
    for d in data:
        if k > 0:
            output_text = '\n'.join(d['generated'][:k])
        else:
            output_text = '\n'.join(d['generated'])
        output_token_num = len(enc.encode(output_text))
        total_cost += input_token_num * input_cost + output_token_num * output_cost
    return total_cost / 1000


def is_example_correct(example):
    pred = example['prediction']
    ans = example['answer']
    if finqa_equal(pred, ans):
        return True
    else:
        return False


def get_pred_result_for_ensemble(example, k):
    result_counter = Counter()
    if 'results' not in example or len(example['results']) == 0:
        return None
    results = example['results'][:k]
    for pred in results:
        if pred is not None:
            result_counter.update([pred])
    if len(result_counter) > 0:
        prediction = result_counter.most_common(1)[0][0]
    else:
        prediction = None
    return prediction


def consistency_larger_than_SC_threshold(example, threshold):
    results = example['results']
    results_counter = example['result_counter']
    if len(results_counter) == 0:
        return False
    major_answer = max(results_counter, key=results_counter.get)
    if results_counter[major_answer] >= len(results) * threshold:
        return True
    return False


def get_example_cost(input, output, version):
    if version == 'gpt-3.5-turbo':
        enc = enc_3
        input_cost = gpt3_input_cost
        output_cost = gpt3_output_cost
    else:
        enc = enc_4
        input_cost = gpt4_input_cost
        output_cost = gpt4_output_cost
    input_token_num = len(enc.encode(input))
    output_token_num = len(enc.encode(output))
    return (input_token_num * input_cost + output_token_num * output_cost) / 1000


def check_SC_result(weak_llm_res, strong_llm_res, threshold, prompt, cot1_prompting):
    correct = 0
    cost = get_example_cost(input=prompt, output="\n".join(weak_llm_res['generated']), version='gpt-3.5-turbo')
    if consistency_larger_than_SC_threshold(weak_llm_res, threshold):
        if is_example_correct(weak_llm_res):
            correct = 1
    else:
        cost += get_example_cost(input=cot1_prompting, output="\n".join(strong_llm_res['generated']), version='gpt-4')
        if is_example_correct(strong_llm_res):
            correct = 1
    return cost, correct


def merge_answer(weak_llm1, weak_llm2, k):
    res = {}
    for key in weak_llm1:
        if key == 'generated' or key == 'results':
            res[key] = weak_llm1[key][:k] + weak_llm2[key][:k]
        else:
            res[key] = weak_llm1[key]
    res['result_counter'], res['prediction'] = get_major_ans(res['results'])
    return res


def get_major_ans(lst):
    if len(lst) == 0:
        return {}, None
    result_counter = Counter()
    for r in lst:
        if r is not None:
            result_counter.update([r])
    if len(result_counter) == 0:
        return {}, None
    return result_counter, result_counter.most_common(1)[0][0]


def get_acc_for_3(data):
    c = 0
    for d in data:
        answer = d['answer']
        pred = d['prediction']
        if finqa_equal(prediction=pred, reference=answer):
            c += 1
    return c / len(data)


def get_acc_for_4(data):
    c = 0
    for d in data:
        answer = d['answer']
        pred = d['prediction']
        if finqa_equal(prediction=pred, reference=answer):
            c += 1
    return c / len(data)


def get_acc_for_cot_1d(data3, data4, threshold, prompt, cot1_prompt):
    assert len(data3) == len(data4)
    correct = 0
    cost = 0
    for i in range(len(data3)):
        d3 = data3[i]
        d4 = data4[i]
        cost += check_SC_result(d3, d4, threshold, prompt, cot1_prompt)[0]
        correct += check_SC_result(d3, d4, threshold, prompt, cot1_prompt)[1]
    return correct, cost


def merge_data(data1, data2, k):
    new_d = []
    for i in range(len(data1)):
        d1 = data1[i]
        d2 = data2[i]
        new_d.append(merge_answer(d1, d2, k))
    return new_d


def get_acc_for_verify(data1, data2, gpt_4_data, prompt, cot1_prompting, k):
    assert len(data1) == len(data2)
    correct = 0
    cost = 0
    for i in range(len(data1)):
        d1 = data1[i]
        d2 = data2[i]
        d_gpt4 = gpt_4_data[i]
        answer = d1['answer']
        d1_ensemble_res = get_pred_result_for_ensemble(d1, k)
        d2_ensemble_res = get_pred_result_for_ensemble(d2, k)
        cost += get_example_cost(input=prompt,
                                 output='\n'.join(d1['generated'][:k] + d2['generated'][:k]),
                                 version='gpt-3.5-turbo')
        if finqa_equal(d1_ensemble_res, d2_ensemble_res):
            if finqa_equal(d1_ensemble_res, answer):
                correct += 1
        else:
            cost += get_example_cost(input=cot1_prompting, output='\n'.join(d_gpt4['generated']), version='gpt-4')
            if is_example_correct(d_gpt4):
                correct += 1
    return correct, cost


def eval_acc_cost(M, N, data_list, cot_prompt_list, pot_prompt_list, threshold_list=None):
    if threshold_list is None:
        threshold_list = [0.4, 0.5, 0.55, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    k = int((N - M * 0.75) / 2)
    # metric for basic accuracy
    data_cot11 = data_list[0]
    data_cot12 = data_list[1]
    data_cot21 = data_list[2]
    data_cot22 = data_list[3]
    data_pot11 = data_list[4]
    data_pot12 = data_list[5]
    data_pot21 = data_list[6]
    data_pot22 = data_list[7]
    gpt4_cot1 = data_list[8]
    gpt4_cot2 = data_list[9]
    gpt4_pot1 = data_list[10]
    gpt4_pot2 = data_list[11]
    gpt4_cot1_greedy = data_list[12]
    gpt4_cot2_greedy = data_list[13]
    gpt4_pot1_greedy = data_list[14]
    gpt4_pot2_greedy = data_list[15]

    cot1_prompting = cot_prompt_list[0]
    cot2_prompting = cot_prompt_list[1]
    pot1_prompting = pot_prompt_list[0]
    pot2_prompting = pot_prompt_list[1]

    # Get CoT1 3.5 cost
    cost_cot11 = get_real_cost(data_cot11, cot1_prompting, 'gpt-3.5-turbo')
    cost_cot12 = get_real_cost(data_cot12, cot1_prompting, 'gpt-3.5-turbo')
    cost_cot1_3 = (cost_cot11 + cost_cot12) / 2

    # Get CoT2 3.5 cost
    cost_cot21 = get_real_cost(data_cot21, cot2_prompting, 'gpt-3.5-turbo')
    cost_cot22 = get_real_cost(data_cot22, cot2_prompting, 'gpt-3.5-turbo')
    cost_cot2_3 = (cost_cot21 + cost_cot22) / 2

    # Get PoT1 3.5 cost
    cost_pot11 = get_real_cost(data_pot11, pot1_prompting, 'gpt-3.5-turbo')
    cost_pot12 = get_real_cost(data_pot12, pot1_prompting, 'gpt-3.5-turbo')
    cost_pot1_3 = (cost_pot11 + cost_pot12) / 2

    # Get PoT2 3.5 cost
    cost_pot21 = get_real_cost(data_pot21, pot2_prompting, 'gpt-3.5-turbo')
    cost_pot22 = get_real_cost(data_pot22, pot2_prompting, 'gpt-3.5-turbo')
    cost_pot2_3 = (cost_pot21 + cost_pot22) / 2

    # Get CoT1 3.5 topK cost
    cost_cot11_to_ensemble = get_real_cost(data_cot11, cot1_prompting, 'gpt-3.5-turbo', k=k)
    cost_cot12_to_ensemble = get_real_cost(data_cot12, cot1_prompting, 'gpt-3.5-turbo', k=k)
    cost_cot1_3_to_ensemble = (cost_cot11_to_ensemble + cost_cot12_to_ensemble) / 2

    # Get CoT2 3.5 topK cost
    cost_cot21_to_ensemble = get_real_cost(data_cot21, cot2_prompting, 'gpt-3.5-turbo', k=k)
    cost_cot22_to_ensemble = get_real_cost(data_cot22, cot2_prompting, 'gpt-3.5-turbo', k=k)
    cost_cot2_3_to_ensemble = (cost_cot21_to_ensemble + cost_cot22_to_ensemble) / 2

    # Get PoT1 3.5 topK cost
    cost_pot11_to_ensemble = get_real_cost(data_pot11, pot1_prompting, 'gpt-3.5-turbo', k=k)
    cost_pot12_to_ensemble = get_real_cost(data_pot12, pot1_prompting, 'gpt-3.5-turbo', k=k)

    # Get PoT2 3.5 topK cost
    cost_pot21_to_ensemble = get_real_cost(data_pot21, pot2_prompting, 'gpt-3.5-turbo', k=k)
    cost_pot22_to_ensemble = get_real_cost(data_pot22, pot2_prompting, 'gpt-3.5-turbo', k=k)

    # Get CoT1 4 cost
    cost_cot1_4 = get_real_cost(gpt4_cot1, cot1_prompting, 'gpt-4')
    # Get CoT2 4 cost
    cost_cot2_4 = get_real_cost(gpt4_cot2, cot2_prompting, 'gpt-4')
    # Get PoT1 4 cost
    cost_pot1_4 = get_real_cost(gpt4_pot1, pot1_prompting, 'gpt-4')
    # Get PoT2 4 cost
    cost_pot2_4 = get_real_cost(gpt4_pot2, pot2_prompting, 'gpt-4')

    # Get CoT1 4-greedy cost
    cost_cot1_4_greedy = get_real_cost(gpt4_cot1_greedy, cot1_prompting, 'gpt-4')
    # Get CoT2 4-greedy cost
    cost_cot2_4_greedy = get_real_cost(gpt4_cot2_greedy, cot2_prompting, 'gpt-4')
    # Get PoT1 4-greedy cost
    cost_pot1_4_greedy = get_real_cost(gpt4_pot1_greedy, pot1_prompting, 'gpt-4')
    # Get PoT2 4-greedy cost
    cost_pot2_4_greedy = get_real_cost(gpt4_pot2_greedy, pot2_prompting, 'gpt-4')

    # acc for GPT-3.5-COT
    acc_cot11_3 = get_acc_for_3(data_cot11)
    acc_cot12_3 = get_acc_for_3(data_cot12)
    acc_cot21_3 = get_acc_for_3(data_cot21)
    acc_cot22_3 = get_acc_for_3(data_cot22)
    print(
        f"The final accuracy with GPT3-cot is {(acc_cot11_3 + acc_cot12_3 + acc_cot21_3 + acc_cot22_3) / 4}, cost is {(cost_cot1_3 + cost_cot1_3) / 2}")
    acc_pot11_3 = get_acc_for_3(data_pot11)
    acc_pot12_3 = get_acc_for_3(data_pot12)
    acc_pot21_3 = get_acc_for_3(data_pot21)
    acc_pot22_3 = get_acc_for_3(data_pot22)
    print(
        f"The final accuracy with GPT3-pot is {(acc_pot11_3 + acc_pot12_3 + acc_pot21_3 + acc_pot22_3) / 4}, cost is {(cost_pot1_3 + cost_pot1_3) / 2}")

    # acc for GPT-4
    acc_cot1_4 = get_acc_for_4(gpt4_cot1)
    acc_cot2_4 = get_acc_for_4(gpt4_cot2)
    acc_pot1_4 = get_acc_for_4(gpt4_pot1)
    acc_pot2_4 = get_acc_for_4(gpt4_pot2)
    print(
        f"The final accuracy with GPT4-cot is {(acc_cot1_4 + acc_cot2_4) / 2}, cost is {(cost_cot1_4 + cost_cot2_4) / 2}")
    print(
        f"The final accuracy with GPT4-pot is {(acc_pot1_4 + acc_pot2_4) / 2}, cost is {(cost_pot1_4 + cost_pot2_4) / 2}")

    # acc for GPT-4-greedy
    acc_cot1_4_greedy = get_acc_for_4(gpt4_cot1_greedy)
    acc_cot2_4_greedy = get_acc_for_4(gpt4_cot2_greedy)
    acc_pot1_4_greedy = get_acc_for_4(gpt4_pot1_greedy)
    acc_pot2_4_greedy = get_acc_for_4(gpt4_pot2_greedy)
    print(
        f"The final accuracy with GPT4-cot-greedy is {(acc_cot1_4_greedy + acc_cot2_4_greedy) / 2}, cost is {(cost_cot1_4_greedy + cost_cot2_4_greedy) / 2}")
    print(
        f"The final accuracy with GPT4-pot-greedy is {(acc_pot1_4_greedy + acc_pot2_4_greedy) / 2}, cost is {(cost_pot1_4_greedy + cost_pot2_4_greedy) / 2}")

    # print('Cot-1d-vote')
    # # acc for CoT-1d-vote
    # for threshold in threshold_list:
    #     acc_for_cot_1d_vote = 0
    #     cost_for_cot_1d_vote = 0
    #     total_data = len(data_cot11)
    #     for prompt, data in [(cot1_prompting, data_cot11), (cot1_prompting, data_cot12), (cot2_prompting, data_cot21),
    #                          (cot2_prompting, data_cot22)]:
    #         correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
    #         acc_for_cot_1d_vote += correct_acc
    #         cost_for_cot_1d_vote += cost
    #     print(
    #         f"{acc_for_cot_1d_vote / (total_data * 4)}\t{cost_for_cot_1d_vote / 4}")
    #
    # print('Pot-1d-vote')
    # # acc for PoT-1d-vote
    # for threshold in threshold_list:
    #     acc_for_pot_1d_vote = 0
    #     cost_for_pot_1d_vote = 0
    #     total_data = len(data_pot11)
    #     for prompt, data in [(pot1_prompting, data_pot11), (pot1_prompting, data_pot12), (pot2_prompting, data_pot21),
    #                          (pot2_prompting, data_pot22)]:
    #         correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
    #         acc_for_pot_1d_vote += correct_acc
    #         cost_for_pot_1d_vote += cost
    #     print(
    #         f"{acc_for_pot_1d_vote / (total_data * 4)}\t{cost_for_pot_1d_vote / 4}")

    # # acc for CoT-2d-vote
    print('CoT-2d-vote')
    for threshold in threshold_list:
        acc_for_cot_2d_vote = 0
        cost_for_cot_2d_vote = 0
        total_data = len(data_pot11)
        prompt = cot1_prompting + cot2_prompting
        for data1, data2 in [(data_cot11, data_cot21),
                             (data_cot11, data_cot22), (data_cot12, data_cot21),
                             (data_cot12, data_cot22)]:
            data = merge_data(data1, data2, k)
            correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
            acc_for_cot_2d_vote += correct_acc
            cost_for_cot_2d_vote += cost
        print(
            f"{acc_for_cot_2d_vote / (total_data * 4)}\t{cost_for_cot_2d_vote / 4}")

    # print('PoT-2d-vote')
    # for threshold in threshold_list:
    #     acc_for_pot_2d_vote = 0
    #     cost_for_pot_2d_vote = 0
    #     total_data = len(data_pot11)
    #     prompt = pot1_prompting + pot2_prompting
    #     for data1, data2 in [(data_pot11, data_pot21), (data_pot11, data_pot22), (data_pot12, data_pot21),
    #                          (data_pot12, data_pot22)]:
    #         data = merge_data(data1, data2, k)
    #         correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
    #         acc_for_pot_2d_vote += correct_acc
    #         cost_for_pot_2d_vote += cost
    #     print(
    #         f"{acc_for_pot_2d_vote / (total_data * 4)}\t{cost_for_pot_2d_vote / 4}")

    print('MoT-1d-vote')
    for threshold in threshold_list:
        acc_for_mot_1d_vote = 0
        cost_for_mot_1d_vote = 0
        total_data = len(data_pot11)
        prompt1 = cot1_prompting + pot1_prompting
        prompt2 = cot2_prompting + pot2_prompting
        for prompt, data1, data2 in [(prompt1, data_cot11, data_pot11), (prompt1, data_cot11, data_pot12),
                                     (prompt1, data_cot12, data_pot11), (prompt1, data_cot12, data_pot12),
                                     (prompt2, data_cot21, data_pot21), (prompt2, data_cot21, data_pot22),
                                     (prompt2, data_cot22, data_pot21), (prompt2, data_cot22, data_pot22)
                                     ]:
            data = merge_data(data1, data2, k)
            correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
            acc_for_mot_1d_vote += correct_acc
            cost_for_mot_1d_vote += cost
        print(
            f"{acc_for_mot_1d_vote / (total_data * 8)}\t{cost_for_mot_1d_vote / 8}")

    # print('MoT-2d-vote')
    # for threshold in threshold_list:
    #     acc_for_mot_2d_vote = 0
    #     cost_for_mot_2d_vote = 0
    #     total_data = len(data_pot11)
    #     prompt1 = cot1_prompting + pot2_prompting
    #     prompt2 = cot2_prompting + pot1_prompting
    #     for prompt, data1, data2 in [(prompt1, data_cot11, data_pot21), (prompt1, data_cot11, data_pot22),
    #                                  (prompt1, data_cot12, data_pot21), (prompt1, data_cot12, data_pot22),
    #                                  (prompt2, data_cot21, data_pot11), (prompt2, data_cot21, data_pot12),
    #                                  (prompt2, data_cot22, data_pot11), (prompt2, data_cot22, data_pot12)
    #                                  ]:
    #         data = merge_data(data1, data2, k)
    #         correct_acc, cost = get_acc_for_cot_1d(data, gpt4_cot1, threshold, prompt, cot1_prompting)
    #         acc_for_mot_2d_vote += correct_acc
    #         cost_for_mot_2d_vote += cost
    #     print(
    #         f"{acc_for_mot_2d_vote / (total_data * 8)}\t{cost_for_mot_2d_vote / 8}")

    print('verify')
    acc_for_cot_2d_verify = 0
    cost_for_cot_2d_verify = 0
    total_data = len(data_pot11)
    prompt = cot1_prompting + cot2_prompting
    for data1, data2 in [(data_cot11, data_cot21), (data_cot11, data_cot22), (data_cot12, data_cot21),
                         (data_cot12, data_cot22)]:
        correct_acc, cost = get_acc_for_verify(data1, data2, gpt4_cot1, prompt, cot1_prompting, k)
        acc_for_cot_2d_verify += correct_acc
        cost_for_cot_2d_verify += cost
    print(
        f"{acc_for_cot_2d_verify / (total_data * 4)}\t{cost_for_cot_2d_verify / 4}")
    acc_for_pot_2d_verify = 0
    cost_for_pot_2d_verify = 0
    prompt = pot1_prompting + pot2_prompting
    for data1, data2 in [(data_pot11, data_pot21), (data_pot11, data_pot22), (data_pot12, data_pot21),
                         (data_pot12, data_pot22)]:
        correct_acc, cost = get_acc_for_verify(data1, data2, gpt4_cot1, prompt, cot1_prompting, k)
        acc_for_pot_2d_verify += correct_acc
        cost_for_pot_2d_verify += cost
    print(
        f"{acc_for_pot_2d_verify / (total_data * 4)}\t{cost_for_pot_2d_verify / 4}")

    acc_for_mot_1d_verify = 0
    cost_for_mot_1d_verify = 0
    prompt1 = cot1_prompting + pot1_prompting
    prompt2 = cot2_prompting + pot2_prompting
    for prompt, data1, data2 in [(prompt1, data_cot11, data_pot11), (prompt1, data_cot11, data_pot12),
                                 (prompt1, data_cot12, data_pot11), (prompt1, data_cot12, data_pot12),
                                 (prompt2, data_cot21, data_pot21), (prompt2, data_cot21, data_pot22),
                                 (prompt2, data_cot22, data_pot21), (prompt2, data_cot22, data_pot22)
                                 ]:
        correct_acc, cost = get_acc_for_verify(data1, data2, gpt4_cot1, prompt, cot1_prompting, k)
        acc_for_mot_1d_verify += correct_acc
        cost_for_mot_1d_verify += cost
    print(
        f"{acc_for_mot_1d_verify / (total_data * 8)}\t{cost_for_mot_1d_verify / 8}")

    acc_for_mot_2d_verify = 0
    cost_for_mot_2d_verify = 0
    prompt1 = cot1_prompting + pot2_prompting
    prompt2 = cot2_prompting + pot1_prompting
    for prompt, data1, data2 in [(prompt1, data_cot11, data_pot21), (prompt1, data_cot11, data_pot22),
                                 (prompt1, data_cot12, data_pot21), (prompt1, data_cot12, data_pot22),
                                 (prompt2, data_cot21, data_pot11), (prompt2, data_cot21, data_pot12),
                                 (prompt2, data_cot22, data_pot11), (prompt2, data_cot22, data_pot12)
                                 ]:
        correct_acc, cost = get_acc_for_verify(data1, data2, gpt4_cot1, prompt, cot1_prompting, k)
        acc_for_mot_2d_verify += correct_acc
        cost_for_mot_2d_verify += cost
    print(
        f"{acc_for_mot_2d_verify / (total_data * 8)}\t{cost_for_mot_2d_verify / 8}")
