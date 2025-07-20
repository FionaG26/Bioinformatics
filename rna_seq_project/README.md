# 🧬 RNA-Seq Analysis Project: Tumor vs Normal Tissue

## 📌 Project Description

In this project, we analyze RNA-Seq data to identify differentially expressed genes (DEGs) between **tumor** and **normal** tissue samples. The objective is to understand molecular changes in cancer and uncover potential biomarkers or therapeutic targets.

### 🔬 Workflow Overview

The analysis pipeline involves:

1. **Quality Control (QC)** of raw FASTQ files
2. **Trimming** of low-quality bases and adapters
3. **Read Alignment** to a reference genome
4. **Expression Quantification** at the gene level
5. **Differential Expression Analysis** to detect DEGs
6. **Functional Enrichment Analysis** to explore biological significance

---

## 📚 Glossary of Key Terms

### FASTQ File
A text-based format for storing both a biological sequence (usually nucleotide) and its corresponding quality scores.

### Quality Control (QC)
A step to assess the quality of raw sequencing data. Common QC tools include:

- **FastQC**: generates per-base quality statistics
- **MultiQC**: aggregates reports across samples

### Trimming
The process of removing adapter sequences and low-quality bases from reads using tools like **Trimmomatic** or **Cutadapt**.

### Alignment
Mapping sequencing reads to a reference genome using aligners such as:

- **HISAT2**: a fast and sensitive alignment tool
- **STAR**: another high-performance RNA-seq aligner

### Expression Quantification
Counting how many reads map to each gene using tools like:

- **featureCounts**
- **HTSeq**
- **Salmon/Kallisto** (for lightweight, alignment-free quantification)

### TPM / FPKM / RPKM
Methods for normalizing gene expression levels:
- **TPM** (Transcripts Per Million)
- **FPKM** (Fragments Per Kilobase Million)
- **RPKM** (Reads Per Kilobase Million)

### Differential Expression Analysis (DEA)
Statistical testing to determine genes that are significantly upregulated or downregulated between two conditions (e.g., tumor vs normal).

- Tool: **DESeq2**, **edgeR**, or **limma-voom**
- Output: log2 fold changes and adjusted p-values

### Log2 Fold Change
Measures the magnitude of change in gene expression on a log base 2 scale. A value of +2 means 4x higher expression.

### Adjusted p-value / False Discovery Rate (FDR)
Corrects for multiple testing. An adjusted p-value < 0.05 indicates significant differential expression.

### Volcano Plot
A scatter plot that displays both the magnitude of change (log2 fold change) and statistical significance (−log10 p-value) for each gene.

### Heatmap
A color-coded grid showing gene expression patterns across samples. Useful for visualizing clusters of upregulated/downregulated genes.

### PCA (Principal Component Analysis)
A dimensionality reduction technique that shows how samples group based on gene expression patterns.

### Functional Enrichment Analysis
Identifies biological functions, pathways, or gene sets enriched in the list of DEGs.

#### Gene Ontology (GO)
A framework for classifying gene function into:
- **Biological Processes**
- **Cellular Components**
- **Molecular Functions**

#### KEGG Pathway
A collection of pathway maps representing known molecular interactions and reaction networks.

#### clusterProfiler
An R package used to perform statistical analysis and visualization of functional profiles.

---

## 📁 Suggested Tools and Libraries

| Step | Tool |
|------|------|
| Quality Control | FastQC, MultiQC |
| Trimming | Trimmomatic |
| Alignment | HISAT2, STAR |
| Quantification | featureCounts, Salmon |
| DEA | DESeq2 |
| Enrichment | clusterProfiler |

---

## 🧪 Outcome

This project will yield a ranked list of differentially expressed genes and their associated pathways—offering insights into molecular drivers of tumor biology.
