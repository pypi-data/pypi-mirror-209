import yaml


class DataContainer:
    pass


class Observation:
    pass


class XRayObservation(Observation):
    pass


class PhotometricObservation(Observation):
    pass


class XRTObservation(XRayObservation):
    pass


class NuStarObservation(XRayObservation):

    pass


class UVOTObservation(PhotometricObservation):
    pass


class GRONDObservation(PhotometricObservation):
    pass


class DataSet:
    pass
