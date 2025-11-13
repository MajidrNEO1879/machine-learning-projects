import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap(matrix, 
                 title="Heatmap", 
                 labels=None, 
                 cmap='coolwarm', 
                 figsize=(8, 6), 
                 annot=True, 
                 fmt='.2f'):
    """
    Plot a heatmap of a 2D matrix using Matplotlib, showing feature names on x and y axes.

    Parameters
    ----------
    matrix : array-like or pandas.DataFrame
        2D list, numpy array, or DataFrame representing the data.
    title : str, optional
        Title of the heatmap (default: "Heatmap")
    labels : list, optional
        Labels for both axes. If None and matrix is a DataFrame, uses its column names.
    cmap : str, optional
        Matplotlib colormap (default: 'coolwarm')
    figsize : tuple, optional
        Figure size (width, height)
    annot : bool, optional
        Whether to annotate cells with values
    fmt : str, optional
        Format for annotation text (default: '.2f')
    """

    # Convert DataFrame to numpy array and extract labels if available
    try:
        import pandas as pd
        if isinstance(matrix, pd.DataFrame):
            if labels is None:
                labels = matrix.columns.tolist()
            matrix = matrix.values
    except ImportError:
        pass

    # Ensure numpy array
    matrix = np.array(matrix)
    n = matrix.shape[0]

    # Default labels if none provided
    if labels is None:
        labels = [f'Var {i}' for i in range(n)]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=figsize)

    # Plot the heatmap
    im = ax.imshow(matrix, cmap=cmap, aspect='auto')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Value', rotation=270, labelpad=15)

    # Set axis ticks and labels
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels(labels)

    # Annotate cells
    if annot:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                ax.text(j, i, format(matrix[i, j], fmt),
                        ha="center", va="center",
                        color="white" if abs(matrix[i, j]) > 0.5 else "black")

    # Title and layout
    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.show()

    return fig, ax
