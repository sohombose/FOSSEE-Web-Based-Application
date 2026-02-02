from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartCanvas(FigureCanvas):
    def __init__(self, title):
        self.fig = Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.ax.set_title(title)

    def plot_bar(self, labels, values):
        self.ax.clear()
        self.ax.bar(labels, values)
        self.ax.set_title(self.ax.get_title())
        self.draw()
