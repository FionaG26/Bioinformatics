!pip install biopython

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import os

# === SAFELY DEFINE FILE NAMES ===
input_file = r"BRCA1.fa"
reverse_output_file = "BRCA1_reverse_complement.fasta"

# === CHECK IF FILE EXISTS ===
if not os.path.isfile(input_file):
    raise FileNotFoundError(f"❌ File '{input_file}' not found. Please check path or filename.")

# === PARSE AND PROCESS ===
records = list(SeqIO.parse(input_file, "fasta"))

if not records:
    raise ValueError("❌ No sequences found in the file. Ensure it starts with '>' and is in FASTA format.")

for record in records:
    seq = record.seq
    gc = gc_fraction(seq) * 100
    rev = seq.reverse_complement()

    print(f"🧬 ID: {record.id}")
    print(f"📝 Description: {record.description}")
    print(f"📏 Length: {len(seq)} bp")
    print(f"🧪 GC Content: {gc:.2f}%")
    print(f"➡️ Forward Strand (first 100 bp):\n{seq[:100]}")
    print(f"⬅️ Reverse Strand (first 100 bp):\n{rev[:100]}")
    print("=" * 70)

# === SAVE REVERSE COMPLEMENT TO FASTA ===
rev_records = []
for record in records:
    rev_record = record[:]  # clone record
    rev_record.seq = record.seq.reverse_complement()
    rev_record.id += "_rev"
    rev_record.description = f"Reverse complement of {record.id}"
    rev_records.append(rev_record)

SeqIO.write(rev_records, reverse_output_file, "fasta")
print(f"\n✅ Reverse strand saved to: {reverse_output_file}")
