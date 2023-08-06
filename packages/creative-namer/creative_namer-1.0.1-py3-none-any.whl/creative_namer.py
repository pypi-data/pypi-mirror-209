#!/usr/bin/env python
import argparse
import json
import os
import uuid
from datetime import datetime

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
    print(prompt)
    q = openai_chat_thread_taiwan(prompt, model='gpt-4')
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


def to_underscore(str1):
    return str1.replace('@', '_').replace(':', '_').replace('.', '_')


def creative_namer(project_description, n=DEFAULT_N, user=DEFAULT_USER, start_tag=DEFAULT_START_TAG,
                   end_tag=DEFAULT_END_TAG):
    response = generate_project_names(project_description, n)
    dic_json = get_json_dic(response, start_tag, end_tag)
    id1 = str(uuid.uuid4())
    timestamp_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    path = f'data/users/{to_underscore(DEFAULT_USER)}/creative_namer/'
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, f'type_creative_namer_time_{timestamp_utc}_id_{id1}')
    file_path = to_underscore(file_path)
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
        print(f'\n{start_tag}\n{json_content}\n{end_tag}\n')
        f.write(json_content)


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_description", help="專案描述文字")
    parser.add_argument("--n", type=int, default=DEFAULT_N, help="生成英文專案名稱的數量")
    parser.add_argument("--user", default=DEFAULT_USER, help="使用者的電子郵件地址")
    parser.add_argument("--start_tag", default=DEFAULT_START_TAG, help="JSON內容起始標記")
    parser.add_argument("--end_tag", default=DEFAULT_END_TAG, help="JSON內容結束標記")
    return parser


def main():
    args = get_args_parser().parse_args()
    creative_namer(args.project_description, n=args.n, user=args.user, start_tag=args.start_tag, end_tag=args.end_tag)


if __name__ == '__main__':
    main()
