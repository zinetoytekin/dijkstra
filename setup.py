
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='shortestpath2220674006',  # Buraya kendi öğrenci numaranı yaz
    version='0.1.0',
    author='Zine Toytekin',
    author_email='zinetoytekin@hacettepe.edu.tr',
    description='Shortest path calculation ',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/kullaniciadi/projeadi',  # GitHub repo adresin
    packages=find_packages(),  # 'projekodlari' klasörü otomatik bulunur
    install_requires=[
        'numpy>=1.21.0',
        'pytest>=1.3.0'  # Testler için pytest yeterli (numpy/pandas kullanmıyorsan gerekmez)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)



 