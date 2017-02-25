from surprise import AlgoBase
from surprise import Dataset
from surprise import evaluate
import numpy

class PredictMean(AlgoBase):

    def __init__(self):

        # Always call base method before doing anything.
        AlgoBase.__init__(self)

    def train(self, trainset):

        # Here again: call base method before doing anything.
        AlgoBase.train(self, trainset)

        # Compute the average rating. We might as well use the
        # trainset.global_mean attribute ;)
        self.the_mean = numpy.mean(
                        [r for (_, _, r) in self.trainset.all_ratings()])

    def estimate(self, u, i):

        return self.the_mean