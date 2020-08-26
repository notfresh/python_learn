import logging, os

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser


def parsePDF(PDF_path,TXT_path):
    logging.info('>>>Parsing pdf file:%s ...'%os.path.basename(PDF_path))
    with open(PDF_path, 'rb')as fp: # 以二进制读模式打开
        praser = PDFParser(fp)  #用文件对象来创建一个pdf文档分析器
        doc = PDFDocument() # 创建一个PDF文档
        praser.set_document(doc) # 连接分析器与文档对象
        doc.set_parser(praser)
        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()
        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            logging.info('>>>Parsing failed...')
            raise PDFTextExtractionNotAllowed
        else:
            rsrcmgr = PDFResourceManager()# 创建PDf 资源管理器 来管理共享资源
            laparams = LAParams() # 创建一个PDF设备对象
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device) # 创建一个PDF解释器对象

            # 循环遍历列表，每次处理一个page的内容
            for page in doc.get_pages(): # doc.get_pages() 获取page列表
                interpreter.process_page(page)
                layout = device.get_result() # 接受该页面的LTPage对象
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        with open(TXT_path, 'a',encoding='utf-8',errors='ignore') as f:
                            results = x.get_text()
                            f.write(results+'\n')
    logging.info('>>>Done!')


if __name__ == '__main__':
    parsePDF("django学习日记.pdf", 'test.py')
