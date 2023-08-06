from typing import List

"""
桑基图
"""


class SankeyChart:
    @staticmethod
    def sankey(data: List[dict], title: str = "", **kwargs):
        """
        :param title: 图题
        :param data: 数据,示例：[{"name":"INB1330","label":"感知设备与服务","child_name":"INB133001","depth":1}]
        :return:
        """
        data_list = []
        link_list = []
        for item in data:
            name = item.pop("name")
            label = item.pop("label")
            depth = item.pop("depth")
            other = item.pop("other", {})
            child_name = item.pop("child_name")
            info = {
                "name": name,
                "label": label,
                "value": name,
                "depth": depth
            }
            if other:
                info.update(other)
            data_list.append(info)
            if child_name and name:
                link_list.append({"source": name, "target": child_name, "value": name})
        result = {
            "series": [
                {
                    "name": title,
                    "data": data_list,
                    "links": link_list
                }
            ]
        }
        if kwargs:
            result["pool"] = kwargs

        return result
