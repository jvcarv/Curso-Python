# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# pip install pypdf2
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'
PASTA_NOVA.mkdir(exist_ok=True)
reader = PdfReader(RELATORIO_BACEN)
# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()
page0 = reader.pages[0]
imagem0 = page0.images[0]
# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore
