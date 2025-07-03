import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from fastq_converter import FastqConverter
from sample_data import get_sample_fastq_entries
import io
import json

# Page configuration
st.set_page_config(
    page_title="FASTQ Quality String Converter",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the converter
converter = FastqConverter()

# Main title and description
st.title("🧬 FASTQ Quality String to Error Probability Converter")
st.markdown("""
This interactive tool converts FASTQ quality strings to base call error probabilities, 
helping you understand the relationship between Phred scores and sequencing accuracy.
""")

# Sidebar with educational content
with st.sidebar:
    st.header("📚 Educational Content")
    
    st.subheader("What are Phred Scores?")
    st.markdown("""
    Phred scores represent the quality of DNA base calls in sequencing data:
    - Higher scores = higher confidence
    - Lower scores = lower confidence
    - Logarithmic scale (base 10)
    """)
    
    st.subheader("Mathematical Formula")
    st.latex(r"P_{error} = 10^{-Q/10}")
    st.markdown("Where Q is the Phred score")
    
    st.subheader("Encoding Standards")
    st.markdown("""
    **Phred+33 (Sanger):**
    - ASCII 33-126
    - Quality scores 0-93
    - Most common format
    
    **Phred+64 (Illumina 1.3+):**
    - ASCII 64-126
    - Quality scores 0-62
    - Older Illumina format
    """)
    
    st.subheader("Quality Score Interpretation")
    quality_table = pd.DataFrame({
        'Phred Score': [10, 20, 30, 40, 50],
        'Error Probability': ['10⁻¹ (0.1)', '10⁻² (0.01)', '10⁻³ (0.001)', '10⁻⁴ (0.0001)', '10⁻⁵ (0.00001)'],
        'Accuracy': ['90%', '99%', '99.9%', '99.99%', '99.999%']
    })
    st.dataframe(quality_table, use_container_width=True)

# Initialize variables
df = None
offset = 33
results = None

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔧 Input & Configuration")
    
    # Encoding selection
    encoding = st.selectbox(
        "Select Encoding Standard:",
        ["Phred+33 (Sanger)", "Phred+64 (Illumina 1.3+)"],
        help="Choose the appropriate encoding standard for your FASTQ data"
    )
    
    # Quality string input
    quality_string = st.text_input(
        "Enter Quality String:",
        value="II?+",
        help="Enter the quality string from your FASTQ file (4th line)"
    )
    
    # Sample data selection
    st.subheader("📋 Or Choose a Sample")
    sample_entries = get_sample_fastq_entries()
    
    if st.button("Load Sample Data"):
        st.session_state['show_samples'] = True
    
    if st.session_state.get('show_samples', False):
        for i, entry in enumerate(sample_entries):
            if st.button(f"Sample {i+1}: {entry['description']}", key=f"sample_{i}"):
                quality_string = entry['quality_string']
                st.session_state['selected_quality'] = quality_string
                st.rerun()
    
    # Update input if sample was selected
    if 'selected_quality' in st.session_state:
        quality_string = st.session_state['selected_quality']
        del st.session_state['selected_quality']

with col2:
    st.header("📊 Results")
    
    if quality_string:
        try:
            # Convert quality string
            offset = 33 if "Phred+33" in encoding else 64
            results = converter.convert_quality_string(quality_string, offset)
            
            # Display results table
            st.subheader("Conversion Results")
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True)
            
            # Summary statistics
            st.subheader("📈 Summary Statistics")
            col2a, col2b, col2c = st.columns(3)
            
            with col2a:
                st.metric("Average Phred Score", f"{df['Phred Score'].mean():.2f}")
            with col2b:
                st.metric("Min Quality", f"{df['Phred Score'].min():.0f}")
            with col2c:
                st.metric("Max Quality", f"{df['Phred Score'].max():.0f}")
            
        except Exception as e:
            st.error(f"Error processing quality string: {str(e)}")
            df = None
            results = None
    else:
        st.info("Enter a quality string to see results")

# Visualization section
if quality_string and df is not None:
    st.header("📊 Visualization")
    
    tab1, tab2, tab3 = st.tabs(["Error Probabilities", "Phred Scores", "Step-by-Step"])
    
    with tab1:
        # Error probability plot
        fig_error = px.bar(
            df, 
            x='Position', 
            y='Error Probability',
            title='Base Call Error Probabilities by Position',
            labels={'Error Probability': 'Error Probability', 'Position': 'Base Position'}
        )
        fig_error.update_layout(showlegend=False)
        st.plotly_chart(fig_error, use_container_width=True)
    
    with tab2:
        # Phred score plot
        fig_phred = px.bar(
            df, 
            x='Position', 
            y='Phred Score',
            title='Phred Scores by Position',
            labels={'Phred Score': 'Phred Score', 'Position': 'Base Position'}
        )
        fig_phred.update_layout(showlegend=False)
        st.plotly_chart(fig_phred, use_container_width=True)
    
    with tab3:
        # Step-by-step calculation
        st.subheader("🔍 Step-by-Step Calculation")
        
        for i, row in df.iterrows():
            with st.expander(f"Position {row['Position']} - Character '{row['ASCII Character']}'"):
                st.markdown(f"""
                **Step 1:** ASCII Character = `{row['ASCII Character']}`
                
                **Step 2:** ASCII Value = `{row['ASCII Value']}`
                
                **Step 3:** Phred Score = ASCII Value - {offset} = {row['ASCII Value']} - {offset} = `{row['Phred Score']}`
                
                **Step 4:** Error Probability = 10^(-Q/10) = 10^(-{row['Phred Score']}/10) = `{row['Error Probability']:.2e}`
                
                **Step 5:** Accuracy = 1 - Error Probability = 1 - {row['Error Probability']:.2e} = `{1 - row['Error Probability']:.6f}` ({(1 - row['Error Probability']) * 100:.4f}%)
                """)

# Download section
if quality_string and df is not None:
    st.header("💾 Download Results")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        # CSV download
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download as CSV",
            data=csv_buffer.getvalue(),
            file_name="fastq_quality_conversion.csv",
            mime="text/csv"
        )
    
    with col4:
        # JSON download
        json_data = df.to_json(orient='records', indent=2)
        if json_data:
            st.download_button(
                label="Download as JSON",
                data=json_data,
                file_name="fastq_quality_conversion.json",
                mime="application/json"
            )
    
    with col5:
        # Text summary download
        summary_text = f"""FASTQ Quality String Conversion Summary
=====================================

Input Quality String: {quality_string}
Encoding Standard: {encoding}
Total Bases: {len(quality_string)}

Results:
--------
"""
        for _, row in df.iterrows():
            summary_text += f"Position {row['Position']}: '{row['ASCII Character']}' -> Phred {row['Phred Score']} -> Error Prob {row['Error Probability']:.2e}\n"
        
        summary_text += f"""
Statistics:
-----------
Average Phred Score: {df['Phred Score'].mean():.2f}
Minimum Phred Score: {df['Phred Score'].min():.0f}
Maximum Phred Score: {df['Phred Score'].max():.0f}
Average Error Probability: {df['Error Probability'].mean():.2e}
"""
        
        st.download_button(
            label="Download Summary",
            data=summary_text,
            file_name="fastq_quality_summary.txt",
            mime="text/plain"
        )

# Additional educational content
st.header("🎓 Learn More")

with st.expander("Understanding FASTQ Format"):
    st.markdown("""
    FASTQ format consists of 4 lines per sequence:
    
    1. **Header line**: Starts with `@` followed by sequence identifier
    2. **Sequence line**: The actual DNA/RNA sequence
    3. **Plus line**: Starts with `+` (may repeat identifier)
    4. **Quality line**: Quality scores for each base (same length as sequence)
    
    Example:
    ```
    @SEQ_ID
    GATCTGAACTG
    +
    II?+
    ```
    """)

with st.expander("Common Quality Score Ranges"):
    st.markdown("""
    | Quality Score | Error Rate | Accuracy | Typical Use |
    |---------------|------------|----------|-------------|
    | 0-10          | >10%       | <90%     | Very low quality |
    | 10-20         | 1-10%      | 90-99%   | Low quality |
    | 20-30         | 0.1-1%     | 99-99.9% | Good quality |
    | 30-40         | 0.01-0.1%  | 99.9-99.99% | High quality |
    | 40+           | <0.01%     | >99.99%  | Very high quality |
    """)

with st.expander("Troubleshooting"):
    st.markdown("""
    **Common Issues:**
    
    1. **Invalid characters**: Quality strings should only contain printable ASCII characters
    2. **Wrong encoding**: Make sure to select the correct encoding standard
    3. **Empty input**: Quality string cannot be empty
    4. **Special characters**: Some characters may not be valid in certain encoding schemes
    
    **Tips:**
    - Most modern sequencing uses Phred+33 encoding
    - Older Illumina data may use Phred+64 encoding
    - Quality scores below 20 are generally considered low quality
    """)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by [Fiona Githaiga](https://www.linkedin.com/in/fiona-githaiga-3282aa194/) | Connect on LinkedIn")
