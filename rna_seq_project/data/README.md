🧬 RNA-Seq Project: Differential Gene Expression in Tumor vs Normal Tissue
🎯 Project Overview
This RNA-Seq project aims to compare gene expression profiles between tumor and normal tissue samples in human colon tissue. The goal is to identify differentially expressed genes (DEGs) that may contribute to tumorigenesis and uncover the biological pathways they impact.

We will use raw FASTQ files as input and process them through a complete RNA-Seq analysis pipeline—including quality control, trimming, alignment, quantification, differential expression analysis, and functional enrichment.

📚 Glossary of Key Terms & Steps
🔬 Quality Control (QC)
Definition: Inspection of raw sequencing reads to assess data quality and detect issues such as low-quality scores, GC bias, adapter contamination, or overrepresented sequences.

🧰 Tools: FastQC, MultiQC
📌 Why: High-quality input ensures reliable downstream analysis.

✂️ Trimming
Definition: Removal of adapter sequences and low-quality bases from raw reads.

🧰 Tool: Trimmomatic
📌 Why: Improves mapping accuracy and reduces alignment artifacts.

🎯 Alignment
Definition: Mapping trimmed reads to a reference genome (e.g., GRCh38/hg38) to determine their genomic origin.

🧰 Tool: HISAT2
📌 Why: Essential for identifying which genes the RNA fragments come from.

📊 Expression Quantification
Definition: Counting reads that align to genes or transcripts to estimate expression levels.

🧰 Tool: featureCounts
📌 Why: Read counts reflect gene activity and are used for downstream comparisons.

📈 Differential Expression Analysis (DEA)
Definition: Statistical comparison of expression levels between tumor and normal samples to identify DEGs.

🧰 Tool: DESeq2
📌 Why: Highlights genes that may be involved in disease or therapeutic response.

🧠 Functional Enrichment Analysis
Definition: Identifying enriched biological processes, molecular functions, and pathways among the DEGs.

🧰 Tool: clusterProfiler
📌 Why: Adds biological meaning to the list of DEGs—e.g., highlighting cancer-related pathways.

📁 FASTQ Files
Definition: Text-based files containing raw sequencing reads and associated quality scores.

📌 Why: The foundational data for RNA-Seq analysis.

📊 Volcano Plot
Definition: A scatter plot visualizing significance (p-value) vs fold change of gene expression.

📌 Why: Helps quickly identify the most relevant DEGs.

🔥 Heatmap
Definition: A color-coded matrix showing expression levels of selected genes across multiple samples.

📌 Why: Highlights clustering patterns, such as clear separation between tumor and normal groups.

📍 Principal Component Analysis (PCA)
Definition: A statistical method for visualizing sample variation and clustering based on expression data.

📌 Why: Confirms whether tumor and normal samples form distinct biological groups.
