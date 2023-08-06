#!/usr/bin/env python
# creative_namer.py
import argparse
import json
import os
import uuid
from datetime import datetime
from functools import reduce

from openai_chat_thread import openai_chat_thread_taiwan

DEFAULT_START_TAG = '--start_json--'
DEFAULT_END_TAG = '--end_json--'
DEFAULT_USER = 'cbh@cameo.tw'
DEFAULT_N = 10


def generate_project_names(project_description, n=DEFAULT_N):
    prompt = f"請用 json 格式創造出 n={n} 個 github 最貼切「專案描述」的英文專案名稱\n" \
             f"json內容的英文名字是要用小寫與底線隔開的英文\n" \
             f"json格式是字典，project_name_en_1 project_name_en_2 ...\n" \
             f"json內容的起始標記為 --start_json-- 與結束 --end_json-- 有明確標記\n" \
             f"\n「專案描述」:{project_description}\n"
    print('\n--creative_namer.py,generate_project_names,prompt:\n', prompt)
    q = openai_chat_thread_taiwan(prompt)
    lst = []
    while True:
        response = q.get()
        if response is None:
            break
        else:
            lst.append(response)
        print(response, end="", flush=True)
    join_str = ''.join(lst)
    return join_str


def get_json_dic(description, start_tag=DEFAULT_START_TAG, end_tag=DEFAULT_END_TAG):
    start = description.find(start_tag)
    end = description.find(end_tag)
    if start != -1 and end != -1:
        json_string = description[start + len(start_tag):end].strip()
        return json.loads(json_string)
    else:
        print("JSON start or end marker not found.")
        return {}


def multi_replace(original_string, lst=['@', ':', '.'], replacement='_'):
    return reduce(lambda str1, ch: str1.replace(ch, replacement), lst, original_string)


def creative_namer(project_description, n=DEFAULT_N, user=DEFAULT_USER):
    response = generate_project_names(project_description, n)
    dic_json = get_json_dic(response, DEFAULT_START_TAG, DEFAULT_END_TAG)
    id1 = str(uuid.uuid4())
    timestamp_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    path = f'data/users/{multi_replace(DEFAULT_USER)}/creative_namer/'
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, f'type_creative_namer_time_{timestamp_utc}_id_{id1}')
    file_path = multi_replace(file_path)
    file_path += '.json'
    dic_output = {
        "user": user,
        "type": "creative_namer",
        "time": timestamp_utc,
        "id": id1,
        "file_path": file_path,
        'project_description': project_description,
    }

    dic_combine = {**dic_output, **dic_json}
    with open(dic_combine["file_path"], 'w', encoding='utf-8') as f:
        json_content = json.dumps(dic_combine, ensure_ascii=False, indent=2)
        f.write(json_content)
    return json_content


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_description", help="專案描述文字")
    parser.add_argument("--n", type=int, default=DEFAULT_N, help="生成英文專案名稱的數量")
    parser.add_argument("--user", default=DEFAULT_USER, help="使用者的電子郵件地址")
    return parser


def main():
    args = get_args_parser().parse_args()
    json_str = creative_namer(args.project_description, n=args.n, user=args.user)
    print('\n--creative_namer.py,main(),json_str:\n', json_str)


if __name__ == '__main__':
    main()
