import json
import pprint
import sys
import xml.etree.ElementTree as ET
import xmltodict


def convert_xml_to_dict(xml_file):
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    return xmltodict.parse(xml_content)
    # return ET.fromstring(xml_content)

def convert_xml_to_iob(xml_file, iob_file=None):
    dfg = convert_xml_to_dict(xml_file)
    # pprint.pprint(dfg, indent=2)
    if iob_file is None:
        iob_file = xml_file.replace('.xml', '.iob')

    with open(iob_file, 'w') as f:
        json.dump(dfg, f, indent=2)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: python3 convert_xml_to_iob.py XML_FILE [IOB_FILE]')
        sys.exit(1)

    xml_file_name = sys.argv[1]
    iob_file_name = sys.argv[2] if len(sys.argv) == 3 else None
    convert_xml_to_iob(xml_file_name, iob_file_name)


if __name__ == '__main__':
    main()
