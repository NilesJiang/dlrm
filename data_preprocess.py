import data_utils as d_util

def __init__(self, path):
  self.path = path;
   # process terabyte data
    d_util.getCriteoAdData(
     #datafile="<path-to-day_{0,...,23}>""
      datafile = "../dataset/day_4",
      o_filename=terabyte_processed.npz,
      max_ind_range=-1,
      sub_sample_rate=0.0,
      days=1,
      data_split='train',
      randomize='total',
      criteo_kaggle=False,
      memory_map=False
   )
