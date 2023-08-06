import os 
import monai
from monai.apps import download_and_extract

#Dataset Location
resource = "https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar"

root_folder = "/Users/dr.shakeel/PostDocWork/Datasets/"
data_dst_dir  = os.path.join(root_folder, "Spleen3D")

compressed_data = os.path.join(root_folder, "Spleen3D.tar")

if not os.path.exists(data_dst_dir):
	download_and_extract(resource, compressed_data, root_folder)



