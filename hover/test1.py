import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]

names = np.array(list("ABCDE"))
#is names just an array for linking up original data 
# when hover'd?
print(list("ABCDE"))
print(names)

# create fig and ax objects
# returns array of ax obj if given more in argument
fig, ax = plt.subplots()
# print(fig)
# print(ax)

sc = plt.scatter(x, y)

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points")
# print(dir(annot))

annot.set_visible(False)

# now I guess we need to link the annot with a hover function
# scrap a hover, i really just want a click at first
#  ind : {'ind': array([2], dtype=int32)}

def onClick(event):
    cont, ind = sc.contains(event)
    print(f'cont : {cont}')
    print(f' ind : {ind}')
    #cont represents if mouse is over point?
    if cont:
        update_annot(ind)
        annot.set_visible(True)

def update_annot(ind):
    #get offsets returns coord data of every point?
    index_of_clicked_point = ind["ind"][0]
    pos = sc.get_offsets()[index_of_clicked_point]
    # set annot coord to the point clicked
    annot.xy = pos
    text = "FUCK"
    annot.set_text(text)

fig.canvas.mpl_connect("button_press_event", onClick)
plt.show()
