import numpy as np
import matplotlib.pyplot as plt
def plot_correlation_heatmap(self, corr_matrix, labels=None, 
                                 title="Correlation Matrix", 
                                 figsize=(10, 8), cmap='coolwarm', 
                                 annot=True, fmt='.2f', vmin=-1, vmax=1):
        """
        Plot a heatmap of a correlation matrix.
        
        Parameters:
        -----------
        corr_matrix : array-like or DataFrame
            The correlation matrix to plot
        labels : list, optional
            Labels for the axes. If None, uses DataFrame columns or default numbering
        title : str, optional
            Title for the plot
        figsize : tuple, optional
            Figure size (width, height)
        cmap : str, optional
            Colormap to use (default: 'coolwarm')
        annot : bool, optional
            Whether to annotate cells with values (default: True)
        fmt : str, optional
            Format string for annotations (default: '.2f')
        vmin, vmax : float, optional
            Min and max values for color scaling (default: -1, 1)
        
        Returns:
        --------
        fig, ax : matplotlib figure and axes objects
        """
        # Convert to numpy array if DataFrame
        try:
            import pandas as pd
            if isinstance(corr_matrix, pd.DataFrame):
                if labels is None:
                    labels = corr_matrix.columns.tolist()
                corr_matrix = corr_matrix.values
        except ImportError:
            pass
        
        # Ensure it's a numpy array
        corr_matrix = np.array(corr_matrix)
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=figsize)
        
        # Create the heatmap
        im = ax.imshow(corr_matrix, cmap=cmap, aspect='auto', 
                       vmin=vmin, vmax=vmax, interpolation='nearest')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Correlation', rotation=270, labelpad=20)
        
        # Set ticks and labels
        n = len(corr_matrix)
        if labels is None:
            labels = [f'Var {i}' for i in range(n)]
        
        ax.set_xticks(np.arange(n))
        ax.set_yticks(np.arange(n))
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_yticklabels(labels)
        
        # Add annotations if requested
        if annot:
            for i in range(n):
                for j in range(n):
                    text = ax.text(j, i, format(corr_matrix[i, j], fmt),
                                 ha="center", va="center", color="black" 
                                 if abs(corr_matrix[i, j]) < 0.5 else "white")
        
        # Set title
        ax.set_title(title, pad=20, fontsize=14, fontweight='bold')
        
        # Adjust layout
        plt.tight_layout()
        
        return fig, ax