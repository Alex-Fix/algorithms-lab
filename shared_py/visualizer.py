import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

class AlgoVisualizer:
    def __init__(self):
        self.history = []

    def record_step(self, arr, highlight_indices=None, title=""):
        """Saves a snapshot of the current state."""
        self.history.append({
            'data': list(arr),
            'highlights': highlight_indices or [],
            'title': title
        })

    def render(self):
        """Displays the interactive slider and plot."""
        def plot_at_step(step):
            state = self.history[step]
            data = state['data']
            highlights = state['highlights']
            
            plt.figure(figsize=(10, 5))
            colors = ['#3498db' if i not in highlights else '#e74c3c' for i in range(len(data))]
            
            bars = plt.bar(range(len(data)), data, color=colors)
            
            # Add text labels on top of bars
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, yval, ha='center', va='bottom')
                
            plt.title(f"{state['title']} (Step {step})")
            plt.ylim(0, max(data) + 10)
            plt.show()

        slider = widgets.IntSlider(
            min=0, max=len(self.history) - 1, 
            step=1, description='Step:', 
            layout=widgets.Layout(width='80%')
        )
        
        widgets.interact(plot_at_step, step=slider)