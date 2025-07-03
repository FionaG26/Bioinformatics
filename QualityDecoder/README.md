# FASTQ Quality String Converter 🔬💻

An interactive, educational Streamlit web app to help users understand and convert FASTQ file quality strings into Phred scores and error probabilities.

---

## 🚀 Features

- 🔢 **ASCII to Phred Score Conversion**
- 📉 **Error Probability Calculation using**: `P(error) = 10^(-Q/10)`
- 🎓 **Educational Sidebar** with dynamic formula explanation
- 📊 **Interactive Visualizations** (bar charts with Plotly & Matplotlib)
- 🧪 **Built-in Sample Data** with 8 quality string patterns
- 🔁 **Phred+33 and Phred+64 encoding support**
- ⬇️ **Download Output** as CSV, JSON, or text
- 📤 **User Input** with real-time feedback and breakdowns

---

## 📂 Project Structure

```

fastq-quality-string-converter/
├── app.py                # Streamlit frontend & UI logic
├── fastq\_converter.py   # Core ASCII ↔ Phred ↔ Error Prob logic
├── sample\_data.py       # Sample FASTQ entries
├── pyproject.toml       # Dependencies (Streamlit, pandas, numpy, plotly, matplotlib)
├── .streamlit/config.toml  # Port and server configuration

````

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/fastq-quality-string-converter.git
cd fastq-quality-string-converter

# Install dependencies
pip install -e .

# Or manually install from pyproject.toml
pip install streamlit pandas numpy matplotlib plotly
````

---

## ▶️ Running the App

```bash
streamlit run app.py
```

By default, the app will run on `http://localhost:5000` as defined in `.streamlit/config.toml`.

---

## 🧬 Example Usage

* Input FASTQ quality string like: `5I%8*;<=`
* Choose Phred+33 or Phred+64
* View:

  * ASCII to Phred mapping
  * Step-by-step breakdown
  * Error probability for each base
  * Download options

---

## 📘 Sample Quality Patterns Included

* Perfect quality
* Mixed quality
* Low quality
* Increasing/decreasing scores
* Edge-case characters

---

## 📄 License

This project is licensed under the MIT License. Feel free to fork and modify!

---

## 👩‍🔬 Created By

Fiona Githaiga | [@pythonqueen](https://qualitydecoder-rvg83pedhrwzqxkmqdvmjs.streamlit.app/))

---
