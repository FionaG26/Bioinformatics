"""
Sample FASTQ entries for demonstration and testing purposes.
"""

def get_sample_fastq_entries():
    """
    Return a list of sample FASTQ entries with different quality patterns.
    
    Returns:
        List of dictionaries containing sample FASTQ data
    """
    
    samples = [
        {
            'description': 'High Quality Read',
            'seq_id': 'SEQ_HIGH_QUALITY',
            'sequence': 'ATCGATCGATCGATCG',
            'quality_string': 'IIIIIIIIIIIIIIII',
            'notes': 'All bases have high quality scores (Phred ~40)'
        },
        {
            'description': 'Mixed Quality Read',
            'seq_id': 'SEQ_MIXED_QUALITY',
            'sequence': 'GATCTGAACTG',
            'quality_string': 'II?+',
            'notes': 'Quality decreases toward the end (common in sequencing)'
        },
        {
            'description': 'Low Quality Read',
            'seq_id': 'SEQ_LOW_QUALITY',
            'sequence': 'NNNNNNNNNN',
            'quality_string': '##########',
            'notes': 'Very low quality bases (Phred ~2)'
        },
        {
            'description': 'Illumina Style Quality',
            'seq_id': 'SEQ_ILLUMINA',
            'sequence': 'ACGTACGTACGTACGT',
            'quality_string': 'BBBBFFFFFHHHHHJJ',
            'notes': 'Typical Illumina quality profile'
        },
        {
            'description': 'Variable Quality',
            'seq_id': 'SEQ_VARIABLE',
            'sequence': 'TTTTAAAACCCCGGGG',
            'quality_string': 'IIAA++??BBBBFFFF',
            'notes': 'Highly variable quality across positions'
        },
        {
            'description': 'Short Read',
            'seq_id': 'SEQ_SHORT',
            'sequence': 'ATCG',
            'quality_string': 'IIBF',
            'notes': 'Short read with decreasing quality'
        },
        {
            'description': 'Quality Decline',
            'seq_id': 'SEQ_DECLINE',
            'sequence': 'ATCGATCGATCGATCGATCGATCG',
            'quality_string': 'IIIIHHHHGGGGFFFFDDDDCCCC',
            'notes': 'Gradual quality decline (typical of longer reads)'
        },
        {
            'description': 'Edge Case Characters',
            'seq_id': 'SEQ_EDGE_CASE',
            'sequence': 'ATCGATCG',
            'quality_string': '!"#$%&\'(',
            'notes': 'Low ASCII values (testing edge cases)'
        }
    ]
    
    return samples

def get_encoding_examples():
    """
    Return examples showing differences between Phred+33 and Phred+64 encoding.
    
    Returns:
        Dictionary with encoding comparison examples
    """
    
    examples = {
        'phred_33_examples': [
            {'char': '!', 'ascii': 33, 'phred': 0, 'error_prob': 1.0},
            {'char': '"', 'ascii': 34, 'phred': 1, 'error_prob': 0.794},
            {'char': '#', 'ascii': 35, 'phred': 2, 'error_prob': 0.631},
            {'char': '$', 'ascii': 36, 'phred': 3, 'error_prob': 0.501},
            {'char': '%', 'ascii': 37, 'phred': 4, 'error_prob': 0.398},
            {'char': '5', 'ascii': 53, 'phred': 20, 'error_prob': 0.01},
            {'char': '?', 'ascii': 63, 'phred': 30, 'error_prob': 0.001},
            {'char': 'I', 'ascii': 73, 'phred': 40, 'error_prob': 0.0001},
        ],
        'phred_64_examples': [
            {'char': '@', 'ascii': 64, 'phred': 0, 'error_prob': 1.0},
            {'char': 'A', 'ascii': 65, 'phred': 1, 'error_prob': 0.794},
            {'char': 'B', 'ascii': 66, 'phred': 2, 'error_prob': 0.631},
            {'char': 'C', 'ascii': 67, 'phred': 3, 'error_prob': 0.501},
            {'char': 'D', 'ascii': 68, 'phred': 4, 'error_prob': 0.398},
            {'char': 'T', 'ascii': 84, 'phred': 20, 'error_prob': 0.01},
            {'char': '^', 'ascii': 94, 'phred': 30, 'error_prob': 0.001},
            {'char': 'h', 'ascii': 104, 'phred': 40, 'error_prob': 0.0001},
        ]
    }
    
    return examples

def get_quality_interpretation_guide():
    """
    Return a guide for interpreting quality scores.
    
    Returns:
        Dictionary with quality interpretation information
    """
    
    guide = {
        'quality_categories': [
            {
                'range': '0-10',
                'description': 'Very Low Quality',
                'error_rate': '>10%',
                'accuracy': '<90%',
                'recommendation': 'Consider filtering out these bases'
            },
            {
                'range': '10-20',
                'description': 'Low Quality',
                'error_rate': '1-10%',
                'accuracy': '90-99%',
                'recommendation': 'Use with caution'
            },
            {
                'range': '20-30',
                'description': 'Good Quality',
                'error_rate': '0.1-1%',
                'accuracy': '99-99.9%',
                'recommendation': 'Generally acceptable'
            },
            {
                'range': '30-40',
                'description': 'High Quality',
                'error_rate': '0.01-0.1%',
                'accuracy': '99.9-99.99%',
                'recommendation': 'Very reliable'
            },
            {
                'range': '40+',
                'description': 'Very High Quality',
                'error_rate': '<0.01%',
                'accuracy': '>99.99%',
                'recommendation': 'Excellent quality'
            }
        ],
        'common_thresholds': {
            'q20': {
                'description': 'Standard quality threshold',
                'error_rate': '1%',
                'accuracy': '99%',
                'usage': 'Common cutoff for read filtering'
            },
            'q30': {
                'description': 'High quality threshold',
                'error_rate': '0.1%',
                'accuracy': '99.9%',
                'usage': 'Stringent quality requirement'
            }
        }
    }
    
    return guide
