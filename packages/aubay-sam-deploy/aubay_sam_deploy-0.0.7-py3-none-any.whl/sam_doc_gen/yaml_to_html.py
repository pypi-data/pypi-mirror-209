import os
import sys
import argparse

from pathlib import Path
from string import Template
from prettytable import PrettyTable
from loremipsum import get_sentences

import oyaml as yaml

def prepare_input_active(type, source):
    """
        Determina la ubicación esperada del activo de entrada
        :param type: Definición de activo propuesta (file / connector)
        :param source: Activo a localizar
    """
    if source is None:
        return (None, None)
    
    SPECIFICATIONS = 'specifications'

    if type == 'connector':
        source = SPECIFICATIONS + '/' + source + '/specification.yaml'

    f = Path(source)
    if not f.is_file():
        return (source, None)
    stf = os.path.split(os.path.abspath(source))
    swe = stf[0].split(SPECIFICATIONS)
    
    return (source, '' if len(swe) == 1 else swe[1], stf[1])

def prepare_output_active(type, target, extra):
    """
        Determina la ubicación esperada del activo de salida
        :param type: Definición de activo propuesta (folder / stream)
        :param source: Activo a localizar
    """
    if type == 'folder':

        if not target:
            target = 'target'

        if not extra and not isinstance(extra, tuple):
            extra = ('', 'specification.yaml')

        f = Path(target)
        if not f.is_dir():
            return (target, False)
        
        os.makedirs(target + extra[0], exist_ok = True)
        f = Path(target + extra[0], extra[1])
        
        return (f.with_suffix('.html'), True)
    
    else:
        return (None, False)

def traslate_yaml(yaml, html_template):
    """
        Convierte jerarquía de objetos YAML a lista anidada de sentencias HTML
        :param yaml: Jerarquía de objetos YAML
        :param template: HTML template class
    """
    response = []
    response.append("<html>")
    response.append(html_template.getHead())

    body_st = []
    body_st.append('''<body class="swagger-section">''')
    body_st.append(html_template.getBodyHead())

    body_st.append('''<div id="swagger-ui-container" class="swagger-ui-wrap"><ul id="resources">''')

    item_template = Template(html_template.getItemList())
    info_template = Template(html_template.getInfoCategory())

    item_list = []
    item_list.append(item_template.substitute(key='Publicación en blockchain:', value='Habilitado' if yaml.get("publishBlockchain") else 'Deshabilitado', title=''))
    item_list.append(item_template.substitute(key='Publicación justificantes:', value='Habilitado' if yaml.get("publishCertificates") else 'Deshabilitado', title=''))
    item_list.append(item_template.substitute(key='Publicación justificantes privados:', value='Habilitado' if yaml.get("publishPrivateCertificate") else 'Deshabilitado', title=''))

    body_st.append(info_template.substitute(name=yaml.get('name'), description=yaml.get('description'), row_list=''.join(item_list)))

    body_st.append(buildDictItems(html_template, yaml.get('customSettings'), 'get', 'Ajustes'))

    body_st.append(buildListItems(html_template, yaml.get('parameters'), 'good', 'Parámetros'))
    body_st.append(buildListItems(html_template, yaml.get('templates'), 'good', 'Plantillas'))

    body_st.append(buildDictDictItems(html_template, yaml.get('configLocale'), 'put', 'Internationalización'))

    body_st.append(buildListItems(html_template, yaml.get('alarmsDefinition'), 'good', 'Alarmas', True))


    body_st.append("</ul></div>")

    body_st.append("</body>")
    response.append(" ".join(body_st))

    response.append("</html>")
    return response

def generate_report(origin, inTarget, target, outTarget, template):
    """
        Genera un informe HTML a partir de un activo con formato YAML

        :param origin: Jerarquía de objetos YAML
        :param inTarget: HTML template class
        :param target: Jerarquía de objetos YAML
        :param outTarget: HTML template class
        :param template: Template HTML utilizado para generar el informe
    """
    inFile, inSubPath, inActive = prepare_input_active(origin, inTarget)
    if inSubPath is None:
        sys.exit("Input file [" + inFile + "] does not exists")

    outFile, result = prepare_output_active(target, outTarget, (inSubPath, inActive))
    if not result:
        sys.exit("Output source [" + str(outFile) + "] failed to be generated")

    with open(inFile) as file:
        yaml_file_object = yaml.load(file, Loader=yaml.FullLoader)

        html_st = traslate_yaml(yaml_file_object, template)

        if target == 'folder':
            f = open(outFile, "w")
            f.write(" ".join(html_st))
            f.close()
            print("File " + str(outFile) + " has been generated")

def generate_active_report():
    if __name__ == "__main__":
        import templates.open_api as open_api
    else:
        import sam_doc_gen.templates.open_api as open_api

    parser = argparse.ArgumentParser(description='YAML file to (HTML) table converter',
                    epilog='text table will be printed as STDOUT - html table will be save in html file ')
    parser.add_argument('--in', dest='origin', choices=['connector', 'file'], required=True, help="Discriminates the input between 'connector' or 'file' source")
    parser.add_argument('--source', dest='inputTarget', required=True, help="input connector or yaml file to process")
    parser.add_argument('--out', dest='target', choices=['folder', 'stream'], required=True, help="Discriminates the output target generated between 'folder' or 'stream' destination")
    parser.add_argument('--target', dest='outputTarget', help="output target to write html output")

    args = parser.parse_args()
    generate_report(args.origin, args.inputTarget, args.target, args.outputTarget, open_api.OpenApiTemplate());

def generate_active():
    if __name__ == "__main__":
        import templates.open_api as open_api
    else:
        import sam_doc_gen.templates.open_api as open_api

    parser = argparse.ArgumentParser(description='YAML file to (HTML) table converter',
                    epilog='text table will be printed as STDOUT - html table will be save in html file ')
    parser.add_argument('--source', dest='inputActive', required=True, help="input connector or yaml file to process")
    parser.add_argument('--target', dest='outputFolder', help="output target to write html output")

    args = parser.parse_args()
    generate_report('connector', args.inputActive, 'folder', args.outputFolder, open_api.OpenApiTemplate());

def buildListItems(html_template, nodeObj, opColor, titleLabel, descObj = None):
    """
        Iterate over List object to build container list template's

        :param html_template: Template HTLM utilizado
        :param nodeObj: Listado a representar
        :param opColor: Color operacional
        :param titleLabel: Etiqueta de la agrupación
        :param descObj: Gestor de descripciones
    """
    if isinstance(nodeObj, list) and len(nodeObj) > 0:
        item_list = []
        key_list = []
        label_list = []
        label_template = Template(html_template.getLabelPropertiesCategory())
        value_template = Template(html_template.getValuePropertiesCategory())

        for item in nodeObj[0]:
            key_list.append(item)
            label_list.append(label_template.substitute(label=item))

        if descObj:
            label_list.append(label_template.substitute(label='description'))

        for item in nodeObj:
            item_list.append("<tr>")
            for key in key_list:
                item_list.append(value_template.substitute(value=item.get(key)))

            if descObj:
                item_list.append(value_template.substitute(value=''))
            item_list.append("</tr>")
        
        containar_template = Template(html_template.getPropertiesCategory())
        item_list_template = Template(html_template.getPropertiesItemCategory())
        return containar_template.substitute(title=titleLabel, 
                                                 item_list=item_list_template.substitute(color=opColor,
                                                                                         labels=''.join(label_list),
                                                                                         row_list=''.join(item_list)))
    else:
        return ''

def buildDictItems(html_template, nodeObj, opColor, titleLabel, descObj = None):
    """
        Itera sobre un esquema de un listado de diccionario

        :param html_template: Template HTLM utilizado
        :param nodeObj: Diccionario a representar
        :param opColor: Color operacional
        :param titleLabel: Etiqueta de la agrupación
        :param descObj: Gestor de descripciones
    """
    if isinstance(nodeObj, dict) and len(nodeObj) > 0:
        item_list = []
        label_list = []
        label_template = Template(html_template.getLabelPropertiesCategory())
        label_list.append(label_template.substitute(label='name'))
        label_list.append(label_template.substitute(label='value'))
        label_list.append(label_template.substitute(label='description'))

        item_template = Template(html_template.getItemList())
        for item in nodeObj:
            item_list.append(item_template.substitute(key=item, 
                                                    value=nodeObj.get(item), 
                                                    title='' if descObj is None else ''))

        containar_template = Template(html_template.getPropertiesCategory())
        item_list_template = Template(html_template.getPropertiesItemCategory())
        return containar_template.substitute(title=titleLabel, 
                                                    item_list=item_list_template.substitute(color=opColor,
                                                                                            labels=''.join(label_list),
                                                                                            row_list=''.join(item_list)))
    else:
        return ''

def buildDictDictItems(html_template, nodeObj, opColor, titleLabel, descObj = None):
    """
        Itera sobre un diccionario que contiene subesquema de listado diccionarios

        :param html_template: Template HTLM utilizado
        :param nodeObj: Diccionario a representar
        :param opColor: Color operacional
        :param titleLabel: Etiqueta de la agrupación
        :param descObj: Gestor de descripciones
    """
    dict_st = []
    if isinstance(nodeObj, dict):

        part_up_head_template = Template(html_template.getPropertiesPartUpCategory().replace('operations', 'grupal operations'))

        dict_st.append(part_up_head_template.substitute(title=titleLabel))

        for key in nodeObj:
            dict_st.append(buildDictItems(html_template, nodeObj.get(key), opColor, key, descObj))

        dict_st.append(html_template.getPropertiesPartDownCategory())
    
    return ''.join(dict_st)

"""
Este módulo posibilita la conversión de un archivo en formato YAML a un archivo HTML.

El documento HTML generado presenta el estilo OpenAPI, por defecto, describiendo a cada agrupación YAML como una agrupación (secciones) endpoint de OpenAPI.

El enfoque conectores asume la existenca del directorio `specifications`, donde se distribuirán cada una de las especificaciones.

Ejemplo al utilizar el script:

   $ python sam_doc_gen/yaml_to_html.py --in file --source specifications/sample.yaml --out folder
   $ python sam_doc_gen/yaml_to_html.py --in connector --source isylight/calle --out folder

Ejemplo de archivo YAML:
~~~~~~~~~~~~~~~~~~~~~~~~
`
name: "Activo"
publishBlockchain: false
publishCertificates: false
publishPrivateCertificate: false
description: "Descripcion de activo"
customSettings:
  defaultFilters:
  - "identificacion.nombre"
  displayQR: false
configLocale:
  ...
`

"""
if __name__ == "__main__":
    generate_active_report()
