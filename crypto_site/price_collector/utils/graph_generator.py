import matplotlib.pyplot as plt
import base64
from io import BytesIO

def graph_maker(dates, prices):
    # Create a new figure and plot some data
    plt.figure()
    plt.plot(dates, prices)

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')
