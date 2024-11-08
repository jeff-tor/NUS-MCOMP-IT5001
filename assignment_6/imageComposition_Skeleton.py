import imageio
import matplotlib.pyplot as plt



def image_composition(filename1, filename2):

    pic = imageio.imread_v2(filename1)
    plt.imshow(pic)
    plt.show()

#Uncomment the following for your own testing

image_composition('avengers_green.jpg','background.jpg')


#image_composition('avengers green triangle.jpg','background.jpg')


