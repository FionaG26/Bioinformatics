# 🧬 Bioinformatics Toolbox

Welcome to my **Bioinformatics** repository — a collection of scripts, notebooks, and workflows for analyzing biological sequence data using computational tools. This folder reflects my journey through genomics, transcriptomics, and coding for data-driven biology.

---

## 📁 Folder Structure

```

bioinformatics/
├── fasta\_parser.py           # Read and parse FASTA sequences
├── fastq\_quality\_checker.py  # Analyze FASTQ quality scores
├── vcf\_parser.py             # Extract and analyze variants from VCF files
├── gtf\_annotation\_parser.py  # Parse gene/exon annotations from GTF
├── kmer\_counter.py           # Generate k-mer frequencies from DNA sequences
├── gc\_content\_plot.py        # GC content analysis using sliding window
├── motif\_finder.py           # Detect motifs like TATA boxes using regex
├── notebooks/
│   ├── sequence\_analysis.ipynb   # Jupyter notebook for interactive analysis
│   └── motif\_visualization.ipynb
├── example\_sequence.fasta    # Sample FASTA input
└── README.md                 # You're here!

````

---

## 🔬 Features

This repository includes core tools and scripts used across **bioinformatics**, **computational biology**, and **biomedical data science** workflows:

### 🧬 Sequence Analysis
- Parse and process **FASTA** & **FASTQ** files
- Identify **open reading frames (ORFs)** and translation products
- Detect **DNA motifs** using regex (e.g., TATA boxes)
- Generate **k-mer frequencies** for pattern recognition
- Perform **GC content analysis** using sliding windows
- Validate sequence quality and composition

### 🧠 Gene Expression & Transcriptomics
- Load and normalize gene expression data (TPM, CPM, FPKM)
- Identify **differentially expressed genes (DEGs)**
- Perform **PCA** and **hierarchical clustering**
- Generate **volcano plots**, **heatmaps**, and **boxplots**
- Parse **GTF/GFF3** files for gene, exon, and transcript features

### 🧬 Variant Analysis & Population Genomics
- Parse and filter **VCF** files for SNPs, indels, and genotypes
- Annotate variants with gene and functional impact
- Explore haplotype structure and mutation signatures

### 🧪 Data Wrangling & Feature Engineering
- Merge and reshape omics datasets using **Pandas/Numpy**
- Engineer features from sequence data for ML models
- Integrate sequence + metadata + phenotype for analysis

### 📊 Data Visualization
- Create plots with **Matplotlib**, **Seaborn**, and **Plotly**
- Plot GC content, k-mer frequencies, and sequence features
- Visualize dimensionality reduction (PCA, t-SNE)
- Build interactive notebooks for result exploration

### 🤖 Machine Learning in Biology
- Classify disease vs control using **SVM, logistic regression, random forest**
- Perform **feature selection** and interpret model outputs
- Apply **unsupervised clustering** and **embedding techniques**
- Build ML-ready datasets from biological inputs

### ⚙️ Workflow Automation & Reproducibility
- Batch-process genomic files via Python and shell
- Modularize pipelines for repeatable analysis
- Export results to CSV/Excel or Jupyter Notebooks
- Track code history with Git/GitHub

### 🌐 External Database Integration
- Fetch sequences/annotations from NCBI, Ensembl, UniProt, GEO
- Automate queries using Entrez or REST APIs
- Convert IDs using BioMart or Ensembl tools

---

## 💻 Requirements

- Python 3.12
- Recommended libraries:
  - `re` (built-in)
  - `matplotlib`
  - `pandas`
  - `seaborn`
  - `collections`
  - `numpy`

Install dependencies:
```bash
pip install matplotlib pandas seaborn numpy
````

---

## 🚀 Usage

### Run k-mer analysis:

```bash
python kmer_counter.py --input example_sequence.fasta --k 4
```

### Find motifs like TATA box:

```bash
python motif_finder.py --input example_sequence.fasta --pattern "TATA[AT]A[AT]"
```

---

## 📚 Learning Resources

* [Biopython Docs](https://biopython.org/)
* [Ensembl File Formats](https://www.ensembl.org/info/website/upload/index.html)
* [Rosalind Practice](http://rosalind.info)
* [GEO Datasets](https://www.ncbi.nlm.nih.gov/geo/)
* [NCBI Tools](https://www.ncbi.nlm.nih.gov/tools/)

---

## 👩‍💻 Author

**Fiona Githaiga**
Molecular Biologist | Software Developer | Bioinformatics Enthusiast
| Precision Medicine | Data-Driven Discovery

Connect with me:
[LinkedIn]([https://linkedin.com/infiona-githaiga-3282aa194] | [GitHub](https://github.com/FionaG26)
