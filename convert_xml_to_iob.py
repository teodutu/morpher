import json
import pprint
import sys
import xml.etree.ElementTree as ET
import xmltodict


class Param:
    def __init__(self, type, name, inout):
        self.type = type
        self.name = name
        self.inout = inout

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'    {self.type}\t{self.name}_{self.inout};'


class Module:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def __repr__(self):
        return str(self)

    def __str__(self):
        inputs = self._stringify_params(self.inputs)
        outputs = self._stringify_params(self.outputs)
        if inputs and outputs:
            params = inputs + '\n' + outputs
        elif inputs:
            params = inputs
        elif outputs:
            params = outputs
        else:
            params = ''

        module = f'module {self.name}()' + "{\n" + params + '\n#\nTODO\n}\n'
        return module

    def _stringify_params(self, params):
        return '\n'.join([str(param) for param in params])


def convert_xml_to_dict(xml_file):
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    return xmltodict.parse(xml_content)
    # return ET.fromstring(xml_content)


def _get_dict_field(dfg, fields, field):
    field_list = []
    dfg_fields = dfg[fields]

    if dfg_fields:
        dfg_field = dfg_fields[field]
        if isinstance(dfg_field, list):
            for fld in dfg_field:
                field_list.append(fld['@idx'])
        else:
            field_list.append(dfg_field['@idx'])

    return field_list


def _get_params(nodes_dict, params, inout):
    params_list = []
    idx = 0

    for param in params:
        param = nodes_dict[param]
        input_name = param['name']

        for param_obj in params_list:
            if param_obj.name == input_name:
                input_name = input_name + str(idx)
                idx += 1
                break

        params_list.append(Param(param['name'], input_name.lower(), inout))

    return params_list

def _get_inputs_outputs_as_params(nodes_dict, inputs, outputs):
    return _get_params(nodes_dict, inputs, 'in'), _get_params(nodes_dict, outputs, 'out')


def get_nodes_dict(dfg: dict):
    nodes_dict = {}

    for node in dfg['Node']:
        inputs = _get_dict_field(node, 'Inputs', 'Input')
        outputs = _get_dict_field(node, 'Outputs', 'Output')

        nodes_dict[node['@idx']] = {
            'name': node['OP'] + '_' + node['@idx'],
            'inputs': inputs,
            'outputs': outputs
        }

        # print(f"Node: op = {node['OP']}, idx = {node['@idx']}, inputs = {inputs}, outputs = {outputs}")
    
    return nodes_dict


def get_cfg_from_xml_dict(xml: dict):
    dfg = xml['xml']['DFG']
    nodes_dict = get_nodes_dict(dfg)
    modules = []

    for idx, node in nodes_dict.items():
        inputs, outputs = _get_inputs_outputs_as_params(nodes_dict, node['inputs'], node['outputs'])
        mod = Module(node['name'], inputs, outputs)
        modules.append(mod)

    return modules

def convert_xml_to_iob(xml_file, iob_file=None):
    xml_dict = convert_xml_to_dict(xml_file)
    # pprint.pprint(xml_dict, indent=2)

    if iob_file is None:
        iob_file = xml_file.replace('.xml', '.iob')

    cfg = get_cfg_from_xml_dict(xml_dict)
    for module in cfg:
        print(module)

    # print_xml_dict(xml_dict)

    # with open(iob_file, 'w') as f:
    #     json.dump(dfg, f, indent=2)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: python3 convert_xml_to_iob.py XML_FILE [IOB_FILE]')
        sys.exit(1)

    xml_file_name = sys.argv[1]
    iob_file_name = sys.argv[2] if len(sys.argv) == 3 else None
    convert_xml_to_iob(xml_file_name, iob_file_name)


if __name__ == '__main__':
    main()
