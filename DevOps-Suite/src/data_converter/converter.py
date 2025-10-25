import json
import xmltodict
import dicttoxml

class DataConverter:
    def json_to_xml(self, json_data):
        try:
            data = json.loads(json_data)
            xml = dicttoxml.dicttoxml(data)
            return xml.decode('utf-8'), None
        except Exception as e:
            return None, str(e)

    def xml_to_json(self, xml_data):
        try:
            data = xmltodict.parse(xml_data)
            return json.dumps(data, indent=4), None
        except Exception as e:
            return None, str(e)
