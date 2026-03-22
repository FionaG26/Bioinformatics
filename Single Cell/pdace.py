# ===================== IMPORT PACKAGES =====================
import subprocess
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
import umap
from joypy import joyplot
import webbrowser
import imageio

# ===================== 0. CHECK & INSTALL MISSING PACKAGES =====================
packages = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "scikit-learn": "sklearn",
    "umap-learn": "umap",
    "joypy": "joypy",
    "kaleido": "kaleido",  # Needed for static 3D export
    "imageio": "imageio"
}

for pkg, import_name in packages.items():
    try:
        __import__(import_name)
    except ModuleNotFoundError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# ===================== 1. PARAMETERS =====================
np.random.seed(42)
n_cells = 500
n_genes = 1000

# ===================== 2. SIMULATE DATA =====================
pseudotime = np.sort(np.random.rand(n_cells))
clones = np.random.choice([0, 1, 2], size=n_cells, p=[0.5, 0.3, 0.2])
mutation_load = clones * np.random.rand(n_cells) * 3

expr = np.random.negative_binomial(
    n=2, p=0.5, size=(n_genes, n_cells)).astype('float64')
expr += (pseudotime * 5)[None, :]
expr += mutation_load[None, :]

expr_df = pd.DataFrame(expr, index=[f"Gene{i+1}" for i in range(n_genes)],
                       columns=[f"Cell{i+1}" for i in range(n_cells)])

meta = pd.DataFrame({
    'Cell': expr_df.columns,
    'Pseudotime': pseudotime,
    'Clone': clones,
    'Mutation_Load': mutation_load
})

# ===================== 3. PCA + UMAP =====================
pca = PCA(n_components=10)
pcs = pca.fit_transform(expr_df.T)

reducer = umap.UMAP(n_components=2, random_state=42)
umap_coords = reducer.fit_transform(pcs)
meta['UMAP1'] = umap_coords[:, 0]
meta['UMAP2'] = umap_coords[:, 1]

# ===================== 4. 2D UMAP PLOT =====================
plt.figure(figsize=(6, 5))
sc = plt.scatter(meta['UMAP1'], meta['UMAP2'],
                 c=meta['Pseudotime'], cmap='plasma', s=20)
plt.colorbar(sc, label='Pseudotime')
plt.xlabel('UMAP1')
plt.ylabel('UMAP2')
plt.title('2D UMAP')
plt.tight_layout()
plt.savefig('UMAP.png', dpi=300)
plt.close()

# ===================== 5. RIDGELINE PLOT =====================
plt.figure(figsize=(6, 5))
joyplot(data=meta, by='Clone', column='Pseudotime', colormap=plt.cm.viridis)
plt.title('Ridgeline plot by Clone')
plt.tight_layout()
plt.savefig('Ridgeline.png', dpi=300)
plt.close()

# ===================== 6. HEATMAP =====================
top30_genes = expr_df.var(axis=1).sort_values(ascending=False).head(30).index
plt.figure(figsize=(10, 6))
sns.heatmap(expr_df.loc[top30_genes], cmap='viridis')
plt.title('Top 30 Variable Genes')
plt.tight_layout()
plt.savefig('Heatmap.png', dpi=300)
plt.close()

# ===================== 7. 3D INTERACTIVE PLOT + GIF =====================
pca3 = PCA(n_components=3)
umap3d = pca3.fit_transform(expr_df.T)
meta['PC1'], meta['PC2'], meta['PC3'] = umap3d[:, 0], umap3d[:, 1], umap3d[:, 2]

fig = px.scatter_3d(meta, x='PC1', y='PC2', z='PC3',
                    color='Pseudotime', size='Mutation_Load',
                    color_continuous_scale='plasma',
                    title='3D Interactive Plot')

# Save interactive HTML
html_file = "UMAP_3D.html"
fig.write_html(html_file)

# Save static PNG snapshot
fig.write_image("UMAP_3D.png")  # requires kaleido

# Generate rotating GIF
frames = []
frame_folder = "gif_frames"
os.makedirs(frame_folder, exist_ok=True)

for angle in range(0, 360, 10):
    camera = dict(eye=dict(
        x=2*np.sin(np.radians(angle)),
        y=2*np.cos(np.radians(angle)),
        z=1
    ))
    fig.update_layout(scene_camera=camera)
    frame_path = os.path.join(frame_folder, f"frame_{angle}.png")
    fig.write_image(frame_path)
    frames.append(imageio.imread(frame_path))

gif_file = "UMAP_3D_Rotating.gif"
imageio.mimsave(gif_file, frames, fps=5)

# Automatically open the interactive HTML in default browser
webbrowser.open('file://' + os.path.realpath(html_file))

print("All plots generated:")
print("- 2D UMAP: UMAP.png")
print("- Ridgeline: Ridgeline.png")
print("- Heatmap: Heatmap.png")
print("- 3D interactive: UMAP_3D.html")
print("- 3D static snapshot: UMAP_3D.png")
print("- 3D rotating GIF (LinkedIn-ready): UMAP_3D_Rotating.gif")
