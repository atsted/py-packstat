import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA 
from sklearn.cluster import KMeans


def animate(t, df, dt):
  ts = t / 10
  te = ts + 10
  x = df.iloc[dt[(ts < dt['TIME']) & (dt['TIME'] < te)].index, :].values
  x = StandardScaler().fit_transform(x)
  pca = PCA(n_components=2)
  principalComponents = pca.fit_transform(x)
  principalDf = pd.DataFrame(data=principalComponents, columns=['pc1', 'pc2'])
  kmeans = KMeans(n_clusters=2, random_state=0).fit(principalDf)
  plt.clf()
  plt.title('%.1f-%.1f sec, %d packs\n' % (ts, te, principalDf.shape[0]))
  plt.scatter(principalDf['pc1'], principalDf['pc2'], c=kmeans.labels_)  

if __name__ == '__main__':
  df = pd.read_csv('dump.csv', sep=';')
  dt = df[['TIME']]
  df = df[['INTERVAL', 'SRC_PORT', 'DEST_PORT', 'PROTOCOL', 'FLAGS', 'LENGTH']]
  fig = plt.figure()
  anim = animation.FuncAnimation(fig, animate, fargs=(df, dt), frames=10000, interval=100, repeat=False)
  plt.show()