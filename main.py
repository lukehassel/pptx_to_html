from data.datasources.powerpoint import PowerPoint

if __name__ == '__main__':
    pp = PowerPoint(path="presentation/samplepptx.pptx")
    c = pp.get_content()
    print(c)
