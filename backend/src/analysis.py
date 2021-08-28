import matplotlib.pyplot as plt

def show_distribution_likes(likes_by_user):
  values, keys = likes_by_user.values(), likes_by_user.keys()
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax.bar(values, keys)
  plt.show()
