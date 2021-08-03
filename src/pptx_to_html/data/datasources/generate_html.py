from pptx_to_html.domain.entities.elements.Image import Image
from pptx_to_html.domain.entities.elements.Text import Text
import xml.etree.cElementTree as ET

from pptx_to_html.domain.entities.elements.slide import Slide


def generate_html(content: []):
    root = ET.Element("html")

    for element in content:
        if isinstance(element, Text):
            ET.SubElement(root, element.tag).text = element.text
        if isinstance(element, Slide):
            ET.SubElement(root, element.tag)
        if isinstance(element, Image):
            #print(element.base)
            #ET.SubElement(root, "img", src = "data:image/png;base64, "+element.base.decode('utf-8'))
            pass

    tree = ET.ElementTree(root)
    #tree.write("filename.html")
    return ET.tostring(root).decode("utf-8")
