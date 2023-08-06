from setuptools import setup, find_packages

setup(
    name="holos",  # nome del pacchetto
    version="0.1",  # versione del pacchetto
    author="Your Name",  # il tuo nome
    author_email="robertodebiase80@gmail.com",  # la tua email
    description="A Python package for implementing the Technological Fields Theory.",  # una breve descrizione del pacchetto
    long_description=open('README.md').read(),  # la descrizione lunga, generalmente si usa il contenuto del file README.md
    long_description_content_type='text/markdown',  # specifica che la lunga descrizione è in formato Markdown
    url="https://github.com/rigeneprojectblockchain/holos-os",  # l'URL del progetto, generalmente il link al repository GitHub
    packages=find_packages(),  # pacchetti inclusi nel tuo progetto, se usi find_packages() trova automaticamente tutti i pacchetti
    classifiers=[  # un elenco di classificatori che aiutano gli utenti a trovare il tuo progetto
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # versione minima di Python richiesta
)
