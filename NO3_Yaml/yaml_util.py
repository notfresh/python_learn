import os
import yaml


class YamlUtils():
    def __init__(self,folder_name='config'):
        self.foler_name = folder_name

    def get_yaml_load(self, file_name):
        yaml_filename = self.__get_yaml_file(file_name)
        f = open(yaml_filename, encoding='utf-8')
        yaml_load = yaml.full_load(f)
        return yaml_load

    def __get_yaml_file(self, file_name):
        """
        :param file_name: the filename of the configfile
        :return: the objection of the config
        """
        try:
            yaml_file = self.__get_file_path(self.foler_name, file_name)
            return yaml_file
        except Exception as e:
            print("read config file error:" + str(e))

    @staticmethod
    def __get_file_path(folder_name, file_name):
        """
        :param folder_name: the directory of the config ，the default directory is config
        :param file_name: the filename of the configfile
        :return: the objection of the config
        """
        try:
            config_path = os.path.abspath('..')
            folder_path = os.path.join(config_path, folder_name)
            file_path = os.path.join(folder_path, file_name)
            return file_path
        except Exception as e:
            print('read config file failed ' + str(e))

    def set_yaml(self, file_name,content):
        """
        调用此方法时，需新建一个YamlUtils().set_yaml(file_name,content)
        用原来的设置不会生效
        default_flow_style=False : 表示dump后的字典数据全部以yml格式显示,默认为为True
        sort_keys=False : 表示dump后的字典数据按原有的顺序示，为True时按字母的排序展示，默认为为True
        """
        yaml_filename = self.__get_yaml_file(file_name)
        f = open(yaml_filename,'w', encoding='utf-8')
        yaml_dump = yaml.dump(content,f,allow_unicode=True, default_flow_style=False,sort_keys=False)
        # print("数据更新完成")
        return yaml_dump