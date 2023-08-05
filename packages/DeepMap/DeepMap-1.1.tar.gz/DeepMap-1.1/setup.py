import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DeepMap",
    version = 1.1,
    author="IRRI South Asia Hub",
    author_email="irrisah@gmail.com",
    description="The DeepMap is a deep learning based python package for genotype to phenotype mapping.",
    long_description="Deep Learning has rapidly evolved and is now routinely being used in prediction-based studies for crop improvement. In this study, an effort was made to develop the DeepMap, a unique deep learning-enabled python package using DNN for genomic prediction. It can be outstretched across crops such as maize, wheat, soybean etc. It utilizes epistatic interactions for data augmentation and outperforms the existing state-of-the-art machine/deep learning models such as Bayesian LASSO, GBLUP, DeepGS, and dualCNN. It is hosted on Python Package Index (PyPI) for ease of use to encourage reproducibility with four-line code execution that imports libraries, takes genotypic and phenotypic data, invokes model for training/testing data and stores result. The DeepMap can be further improve by adding environmental interactions, incorporating nascent architecture of deep learning such as GANs, autoencoders, transformers, and the development of a graphical user interface would increase the user community. Please contact, irrisah@gmail.com for more information.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/DeepMap",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/DeepMap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)