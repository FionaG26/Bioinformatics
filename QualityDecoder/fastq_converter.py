import math
import pandas as pd
from typing import List, Dict, Any

class FastqConverter:
    """
    A class to convert FASTQ quality strings to base call error probabilities.
    
    Supports both Phred+33 (Sanger) and Phred+64 (Illumina 1.3+) encoding standards.
    """
    
    def __init__(self):
        """Initialize the converter with encoding information."""
        self.encoding_info = {
            33: {
                'name': 'Phred+33 (Sanger)',
                'ascii_range': (33, 126),
                'quality_range': (0, 93),
                'description': 'Standard encoding used by most modern sequencers'
            },
            64: {
                'name': 'Phred+64 (Illumina 1.3+)',
                'ascii_range': (64, 126),
                'quality_range': (0, 62),
                'description': 'Older Illumina encoding format'
            }
        }
    
    def ascii_to_phred(self, ascii_char: str, offset: int = 33) -> int:
        """
        Convert ASCII character to Phred score.
        
        Args:
            ascii_char: Single ASCII character from quality string
            offset: Encoding offset (33 for Phred+33, 64 for Phred+64)
            
        Returns:
            Phred quality score
            
        Raises:
            ValueError: If character is invalid for the encoding
        """
        if not ascii_char or len(ascii_char) != 1:
            raise ValueError("Input must be a single character")
        
        ascii_value = ord(ascii_char)
        phred_score = ascii_value - offset
        
        # Validate the score is within reasonable bounds
        if offset == 33 and (ascii_value < 33 or ascii_value > 126):
            raise ValueError(f"ASCII value {ascii_value} out of range for Phred+33 encoding")
        elif offset == 64 and (ascii_value < 64 or ascii_value > 126):
            raise ValueError(f"ASCII value {ascii_value} out of range for Phred+64 encoding")
        
        if phred_score < 0:
            raise ValueError(f"Negative Phred score {phred_score} not allowed")
        
        return phred_score
    
    def phred_to_error_probability(self, phred_score: int) -> float:
        """
        Convert Phred score to error probability.
        
        Args:
            phred_score: Phred quality score
            
        Returns:
            Error probability (0.0 to 1.0)
        """
        if phred_score < 0:
            raise ValueError("Phred score cannot be negative")
        
        # Formula: P_error = 10^(-Q/10)
        return 10 ** (-phred_score / 10)
    
    def convert_quality_string(self, quality_string: str, offset: int = 33) -> List[Dict[str, Any]]:
        """
        Convert entire quality string to error probabilities.
        
        Args:
            quality_string: FASTQ quality string
            offset: Encoding offset (33 for Phred+33, 64 for Phred+64)
            
        Returns:
            List of dictionaries containing conversion results
        """
        if not quality_string:
            raise ValueError("Quality string cannot be empty")
        
        results = []
        
        for i, char in enumerate(quality_string):
            try:
                ascii_value = ord(char)
                phred_score = self.ascii_to_phred(char, offset)
                error_probability = self.phred_to_error_probability(phred_score)
                accuracy = 1 - error_probability
                
                result = {
                    'Position': i + 1,
                    'ASCII Character': char,
                    'ASCII Value': ascii_value,
                    'Phred Score': phred_score,
                    'Error Probability': error_probability,
                    'Accuracy': accuracy,
                    'Accuracy (%)': accuracy * 100
                }
                results.append(result)
                
            except Exception as e:
                raise ValueError(f"Error processing character '{char}' at position {i + 1}: {str(e)}")
        
        return results
    
    def get_quality_statistics(self, quality_string: str, offset: int = 33) -> Dict[str, Any]:
        """
        Get summary statistics for a quality string.
        
        Args:
            quality_string: FASTQ quality string
            offset: Encoding offset
            
        Returns:
            Dictionary with summary statistics
        """
        results = self.convert_quality_string(quality_string, offset)
        df = pd.DataFrame(results)
        
        stats = {
            'total_bases': len(quality_string),
            'encoding': self.encoding_info[offset]['name'],
            'min_phred': df['Phred Score'].min(),
            'max_phred': df['Phred Score'].max(),
            'mean_phred': df['Phred Score'].mean(),
            'median_phred': df['Phred Score'].median(),
            'std_phred': df['Phred Score'].std(),
            'min_error_prob': df['Error Probability'].min(),
            'max_error_prob': df['Error Probability'].max(),
            'mean_error_prob': df['Error Probability'].mean(),
            'mean_accuracy': df['Accuracy'].mean(),
            'bases_above_q20': sum(1 for score in df['Phred Score'] if score >= 20),
            'bases_above_q30': sum(1 for score in df['Phred Score'] if score >= 30),
            'quality_distribution': df['Phred Score'].value_counts().to_dict()
        }
        
        # Calculate percentages
        stats['percent_above_q20'] = (stats['bases_above_q20'] / stats['total_bases']) * 100
        stats['percent_above_q30'] = (stats['bases_above_q30'] / stats['total_bases']) * 100
        
        return stats
    
    def validate_quality_string(self, quality_string: str, offset: int = 33) -> Dict[str, Any]:
        """
        Validate quality string and return validation results.
        
        Args:
            quality_string: FASTQ quality string
            offset: Encoding offset
            
        Returns:
            Dictionary with validation results
        """
        validation = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }
        
        if not quality_string:
            validation['is_valid'] = False
            validation['errors'].append("Quality string is empty")
            return validation
        
        # Check for invalid characters
        encoding_info = self.encoding_info[offset]
        min_ascii, max_ascii = encoding_info['ascii_range']
        
        for i, char in enumerate(quality_string):
            ascii_val = ord(char)
            if ascii_val < min_ascii or ascii_val > max_ascii:
                validation['is_valid'] = False
                validation['errors'].append(
                    f"Character '{char}' at position {i + 1} (ASCII {ascii_val}) "
                    f"is outside valid range {min_ascii}-{max_ascii} for {encoding_info['name']}"
                )
        
        # Check for common issues
        if any(ord(char) < 32 for char in quality_string):
            validation['warnings'].append("Quality string contains control characters")
        
        # Calculate quality statistics for warnings
        if validation['is_valid']:
            try:
                stats = self.get_quality_statistics(quality_string, offset)
                
                if stats['mean_phred'] < 20:
                    validation['warnings'].append(
                        f"Average quality score ({stats['mean_phred']:.1f}) is below 20"
                    )
                
                if stats['percent_above_q20'] < 50:
                    validation['warnings'].append(
                        f"Only {stats['percent_above_q20']:.1f}% of bases have quality ≥ 20"
                    )
                
                validation['info'].append(f"Total bases: {stats['total_bases']}")
                validation['info'].append(f"Average Phred score: {stats['mean_phred']:.2f}")
                validation['info'].append(f"Bases with Q≥20: {stats['percent_above_q20']:.1f}%")
                validation['info'].append(f"Bases with Q≥30: {stats['percent_above_q30']:.1f}%")
                
            except Exception as e:
                validation['errors'].append(f"Error calculating statistics: {str(e)}")
        
        return validation
    
    def compare_encodings(self, quality_string: str) -> Dict[str, Any]:
        """
        Compare how the same quality string would be interpreted under different encodings.
        
        Args:
            quality_string: FASTQ quality string
            
        Returns:
            Dictionary comparing results from different encodings
        """
        comparison = {}
        
        for offset in [33, 64]:
            try:
                validation = self.validate_quality_string(quality_string, offset)
                if validation['is_valid']:
                    results = self.convert_quality_string(quality_string, offset)
                    stats = self.get_quality_statistics(quality_string, offset)
                    
                    comparison[f'phred_{offset}'] = {
                        'encoding': self.encoding_info[offset]['name'],
                        'valid': True,
                        'results': results,
                        'statistics': stats
                    }
                else:
                    comparison[f'phred_{offset}'] = {
                        'encoding': self.encoding_info[offset]['name'],
                        'valid': False,
                        'errors': validation['errors']
                    }
                    
            except Exception as e:
                comparison[f'phred_{offset}'] = {
                    'encoding': self.encoding_info[offset]['name'],
                    'valid': False,
                    'errors': [str(e)]
                }
        
        return comparison
