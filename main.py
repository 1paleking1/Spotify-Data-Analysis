import numpy as np
from matplotlib import legend, pyplot as plt
import getting_data


def create_3d(title, xlabel, ylabel, zlabel, data=None):
    
    fig = plt.figure(figsize=plt.figaspect(0.5))
    
    plt.rcParams['figure.figsize'] = (8,6) # configuring size styles for all plots


    axes = fig.add_subplot(1, 2, 1, projection='3d')

    for point in np.array(data):
        xs, ys, zs, mode = point
        # print(point)
        if mode == 1:
            major_point = axes.plot(xs, ys, zs, marker='.', color='blue', label='major')
        elif mode == 0:
            minor_point = axes.plot(xs, ys, zs, marker='.', color='green', label='minor')

    
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_zlabel(zlabel)

    axes.set_title(title)

    plt.show()



playlist_id = getting_data.POP

create_3d(
    title='Pop',
    xlabel='speechiness',
    ylabel='danceability',
    zlabel='acousticness',
    data=getting_data.get_audio_features(playlist_id, 180)
)
