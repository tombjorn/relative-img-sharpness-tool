import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

def main_hover():

    x = np.random.rand(15)
    y = np.random.rand(15)
    names = np.array(list("ABCDEFGHIJKLMNO"))
    c = np.random.randint(1,5,size=15)

    norm = plt.Normalize(1,4)
    cmap = plt.cm.RdYlGn

    fig,ax = plt.subplots()
    sc = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)

    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)




    def update_annot(ind):

        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                            " ".join([names[n] for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()


    def onClick(event):
        cont, ind = sc.contains(event)
        print(ind)
        print(names)
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                            " ".join([names[n] for n in ind["ind"]]))
        print(text)


    fig.canvas.mpl_connect("motion_notify_event", hover)
    fig.canvas.mpl_connect("button_press_event", onClick)
    return fig
    # plt.show()

fig = main_hover()
plt.show()