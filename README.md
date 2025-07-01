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
├── example\_sequence.fasta    # Sample FASTA input
├── notebooks/
│   ├── sequence\_analysis.ipynb   # Jupyter notebook for interactive analysis
│   └── motif\_visualization.ipynb
└── README.md                 # You're here!

````

---

## 🔬 Features

- **FASTA & FASTQ parsing**  
  Cleanly read biological sequences and quality scores

- **Regex-based motif detection**  
  Find motifs like `TATA[AT]A[AT]` in promoter regions

- **Variant parsing from VCF**  
  Extract and filter SNPs, indels, and genotypes

- **Gene annotation parsing**  
  Load and explore gene features from GTF/GFF files

- **k-mer frequency analysis**  
  Build frequency dictionaries of short DNA patterns

- **Sliding window GC content plots**  
  Visualize GC% along genome or contig regions

---

## 💻 Requirements

- Python 3.7+
- Libraries:
  - `re` (built-in)
  - `matplotlib`
  - `collections`
  - `pandas` *(optional for some notebooks)*

Install dependencies:
```bash
pip install matplotlib pandas
````

---

## 🚀 Usage

### Example: Run k-mer analysis

```bash
python kmer_counter.py --input example_sequence.fasta --k 4
```

### Example: Detect motifs

```bash
python motif_finder.py --input example_sequence.fasta --pattern "TATA[AT]A[AT]"
```

---

## 📚 Learning Resources

* [NCBI](https://www.ncbi.nlm.nih.gov/)
* [Biopython](https://biopython.org/)
* [Ensembl GTF format](https://www.ensembl.org/info/website/upload/gff.html)
* [Rosalind Exercises](http://rosalind.info)

---

## 👩‍💻 Author

**Fiona Githaiga**
Software Developer & Molecular Biologist
| 🧪 Precision Medicine | 💻 Data-Driven Research

Let’s connect!
[LinkedIn](https://www.linkedin.com/in/fiona-githaiga-3282aa194/) | [GitHub](https://github.com/FionaG26)
