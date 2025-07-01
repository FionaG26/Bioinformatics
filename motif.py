import re

def read_fasta(filepath):
    """Reads the first sequence from a FASTA file and returns it as a string."""
    sequence = ""
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith(">"):
                continue  # Skip header
            sequence += line.strip().upper()
    return sequence

def find_motifs(sequence, motif_pattern="TATA[AT]A[AT]"):
    """Finds motif matches using regex and returns positions + sequences."""
    matches = []
    for match in re.finditer(motif_pattern, sequence):
        matches.append({
            'position': match.start(),
            'match': match.group()
        })
    return matches

# === Main execution ===
if __name__ == "__main__":
    fasta_path = "BRCA1.fa"  # Replace with your actual file name
    dna_sequence = read_fasta(fasta_path)
    
    # Define motif pattern: TATA box
    motif_regex = "TATA[AT]A[AT]"
    
    results = find_motifs(dna_sequence, motif_regex)

    if results:
        print(f"Found {len(results)} motif(s):")
        for r in results:
            print(f" - {r['match']} at position {r['position']}")
    else:
        print("No motifs found.")
