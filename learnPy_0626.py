import configparser

print("コンフィグ#############")
"""
[DEFAULT]
debug = False

[Web_serer]
host = 127.10.10
port = 3306
"""

# コンフィグファイルの書き込み
# import configparser
#
# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
# config['web_server'] = {
#     'host': '127.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.1',
#     'port': 80
# }
#
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

# コンフィグファイルの読み込み
# config = configparser.ConfigParser()
# config.read('config.ini')
# print(config['web_server'])
# print(config['web_server']['host'])
# print(config['web_server']['port'])
# print(config['DEFAULT']['debug'])

print("yaml#############")
"""
web_server:
  host: 123.34.4
  posrt: 80

db_server:
  host: 123.34.4
  port: 3345
"""
import yaml

# with open('config.yaml', 'w') as yaml_file:
#     yaml.dump({
#         'web_server':{
#             'host': '123.34.45',
#             'port': 80
#         },
#         'db_server': {
#             'host': '123.34.45',
#             'port': 39485
#         }
#     }, yaml_file)

with open('config.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])

























