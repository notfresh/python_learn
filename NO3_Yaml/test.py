import yaml # 安装包是 pyyaml
import io

s = {'host': {'ip00': '10.0.0.1', 'ip01': {'one': '10.0.0.2', 'two': '10.0.0.3'}},
     'sort': {'apache': 2.2, 'php': 5.3, 'mysql': 5.7}}
# yml 文件写入
f1 = "ss.yml"
import pdb
pdb.set_trace()
with io.open(f1, 'w', encoding="utf-8") as wf:
    yaml.dump(s, wf)

# # yml 读取
# with io.open("ss.yml", 'r', encoding="utf-8") as rf:
#     ss = yaml.load(rf)
#     print(ss)
# {'host': {'ip00': '10.0.0.1',
# 'ip01': {'one': '10.0.0.2', 'two': '10.0.0.3'}},
# 'sort': {'apache': 2.2, 'mysql': 5.7, 'php': 5.3}}


# python2 中执行dump 时候 文件中显示 !!python/unicode
# 解决方式：
# with io.open(f1, 'w', encoding="utf-8") as wf:
#     yaml.safe_dump(s, wf, default_flow_style=False, line_break=True, indent=4, allow_unicode=True)