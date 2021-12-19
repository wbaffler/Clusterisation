from error_codes import Error_codes as errors
from file_parser import File_parser
import matplotlib.pyplot as plt
from clusterisation import Clusterisation

def main():
    url = "http://cs.joensuu.fi/sipu/datasets/s1.txt"
    n_clusters = 15
    parser = File_parser(url)
    parser.parse()
    print(parser.get_error_code())
    if parser.get_error_code() == errors.ok:
        plt.figure(figsize=(15, 10))
        X = parser.get_matrix()
        cl = Clusterisation(X, n_clusters)
        cl.kmeans(plt)
        cl.afprop(plt)
        cl.mean_shift(plt)
        cl.agglomerative_clustering(plt)
        cl.dbscan(plt)
        plt.xticks([])
        plt.yticks([])
        plt.show()
    elif parser.get_error_code() == errors.url_error:
        print('Url error')
    elif parser.get_error_code() == errors.read_error:
        print('Matrix error')
    

##def draw_graphics():


if __name__ == "__main__":
    main()