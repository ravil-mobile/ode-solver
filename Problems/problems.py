class Problem:
    def __init__(self, time_start, time_end, tinterpol):
        self.time_init = time_start
        self.time_end = time_end
        self.time_interval = [time_start, time_end]
        self.tinterpol = tinterpol

        self.h0 = []
        self.h0auto = 1
        self.p = [2.0, 1e0, .8, 1]
        self.y0 = [2, 1]
        self.linSys = 0
        self.tolsbyprob = 0
        self.spSys = 0

    def get_method_structure(self):
        return {'h0': self.h0,
                'h0auto': self.h0auto,
                'p': self.p,
                'y0': self.y0,
                'time_interval': self.time_interval,
                'tinterpol': self.tinterpol,
                'linSys': self.linSys,
                'spSys': self.spSys,
                'tolsbyprob': self.tolsbyprob}