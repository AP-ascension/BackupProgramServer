
import csv
import os
import shutil
import zipfile

source_directories = [
    
        r"\\120.245.176.74\mtxuser\da",
        r"\\120.245.176.75\mtxuser\da",
        r"\\120.245.176.68\mtxuser\da",
        r"\\120.245.176.70\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.55\mtxuser\da",
        r"\\120.245.176.56\mtxuser\da",
        r"\\120.245.176.76\mtxuser\da",
        r"\\120.245.176.71\mtxuser\da",
        r"\\120.245.176.72\mtxuser\da",
        r"\\120.245.176.73\mtxuser\da",
        r"\\120.245.176.32\mtxuser\da",
        r"\\120.245.176.33\mtxuser\da",
        r"\\120.245.176.34\mtxuser\da",
        r"\\120.245.176.35\mtxuser\da",
        r"\\120.245.176.77\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.37\mtxuser\da",
        r"\\120.245.176.38\mtxuser\da",
        r"\\120.245.176.39\mtxuser\da",
        r"\\120.245.176.40\mtxuser\da",
        r"\\120.245.176.107\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.43\mtxuser\da",
        r"\\120.245.176.36\mtxuser\da",
    


        r"\\120.245.176.124\mtxuser\da",
        r"\\120.245.176.125\mtxuser\da",
        r"\\120.245.176.118\mtxuser\da",
        r"\\120.245.176.120\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.105\mtxuser\da",
        r"\\120.245.176.106\mtxuser\da",
        r"\\120.245.176.126\mtxuser\da",
        r"\\120.245.176.121\mtxuser\da",
        r"\\120.245.176.122\mtxuser\da",
        r"\\120.245.176.123\mtxuser\da",
        r"\\120.245.176.82\mtxuser\da",
        r"\\120.245.176.83\mtxuser\da",
        r"\\120.245.176.84\mtxuser\da",
        r"\\120.245.176.85\mtxuser\da",
        r"\\120.245.176.104\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.87\mtxuser\da",
        r"\\120.245.176.88\mtxuser\da",
        r"\\120.245.176.89\mtxuser\da",
        r"\\120.245.176.90\mtxuser\da",
        r"\\120.245.176.111\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.93\mtxuser\da",
        r"\\120.245.176.86\mtxuser\da",
        


        r"\\120.245.176.174\mtxuser\da",
        r"\\120.245.176.175\mtxuser\da",
        r"\\120.245.176.168\mtxuser\da",
        r"\\120.245.176.170\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.155\mtxuser\da",
        r"\\120.245.176.156\mtxuser\da",
        r"\\120.245.176.176\mtxuser\da",
        r"\\120.245.176.171\mtxuser\da",
        r"\\120.245.176.172\mtxuser\da",
        r"\\120.245.176.173\mtxuser\da",
        r"\\120.245.176.132\mtxuser\da",
        r"\\120.245.176.133\mtxuser\da",
        r"\\120.245.176.134\mtxuser\da",
        r"\\120.245.176.135\mtxuser\da",
        r"\\120.245.176.141\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.137\mtxuser\da",
        r"\\120.245.176.138\mtxuser\da",
        r"\\120.245.176.139\mtxuser\da",
        r"\\120.245.176.140\mtxuser\da",
        r"\\120.245.176.157\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.143\mtxuser\da",
        r"\\120.245.176.136\mtxuser\da",
        
        r"\\120.245.176.224\mtxuser\da",
        r"\\120.245.176.225\mtxuser\da",
        r"\\120.245.176.218\mtxuser\da",
        r"\\120.245.176.220\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.205\mtxuser\da",
        r"\\120.245.176.206\mtxuser\da",
        r"\\120.245.176.226\mtxuser\da",
        r"\\120.245.176.221\mtxuser\da",
        r"\\120.245.176.222\mtxuser\da",
        r"\\120.245.176.223\mtxuser\da",
        r"\\120.245.176.182\mtxuser\da",
        r"\\120.245.176.183\mtxuser\da",
        r"\\120.245.176.184\mtxuser\da",
        r"\\120.245.176.185\mtxuser\da",
        r"\\120.245.176.159\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.187\mtxuser\da",
        r"\\120.245.176.188\mtxuser\da",
        r"\\120.245.176.189\mtxuser\da",
        r"\\120.245.176.190\mtxuser\da",
        r"\\120.245.176.191\Matrox Design Assistant\9.1\Projects",
        r"\\120.245.176.193\mtxuser\da",
        r"\\120.245.176.186\mtxuser\da"
    ]
source_names = [
        "EB330P1CAM1Y02", 
        "EB330P1CAM2Y02", 
        "EB349P1CAM1Y02",
        "EB349P1CAM2Y02", 
        "EB357T02P1CAM1Y02",
        "EB357T02P1CAM2Y02",
        "EB405T01P1CAM1Y02",
        "EB410T01P1CAM2Y02",
        "EB420P1CAM1Y02",
        "EB440P1CAM1Y02",
        "EB460P1CAM1Y02", 
        "EB460P1CAM2Y02", 
        "EB460P1CAM3Y02",
        "EB460P1CAM4Y02",
        "EB460P1CAM5Y02",
        "EB465P1CAM1Y02", 
        "EB465P1CAM2Y02", 
        "EB465P1CAM3Y02",
        "EB465P1CAM4Y02",
        "EB465P1CAM5Y02",
        "EB500P1CAM1Y02",
        "EB510P1CAM1Y02",
        "EB330P2CAM1Y02", 
        "EB330P2CAM2Y02", 
        "EB349P2CAM1Y02",
        "EB349P2CAM2Y02", 
        "EB357T02P2CAM1Y02",
        "EB357T02P2CAM2Y02",
        "EB405T01P2CAM1Y02",
        "EB410T01P2CAM2Y02",
        "EB420P2CAM1Y02",
        "EB440P2CAM1Y02",
        "EB460P2CAM1Y02", 
        "EB460P2CAM2Y02", 
        "EB460P2CAM3Y02",
        "EB460P2CAM4Y02",
        "EB460P2CAM5Y02",
        "EB465P2CAM1Y02", 
        "EB465P2CAM2Y02", 
        "EB465P2CAM3Y02",
        "EB465P2CAM4Y02",
        "EB465P2CAM5Y02",
        "EB500P2CAM1Y02",
        "EB510P2CAM1Y02",
        "EB330P3CAM1Y02", 
        "EB330P3CAM2Y02", 
        "EB349P3CAM1Y02",
        "EB349P3CAM2Y02", 
        "EB357T02P3CAM1Y02",
        "EB357T02P3CAM2Y02",
        "EB405T01P3CAM1Y02",
        "EB410T01P3CAM2Y02",
        "EB420P3CAM1Y02",
        "EB440P3CAM1Y02",
        "EB460P3CAM1Y02", 
        "EB460P3CAM2Y02", 
        "EB460P3CAM3Y02",
        "EB460P3CAM4Y02",
        "EB460P3CAM5Y02",
        "EB465P3CAM1Y02", 
        "EB465P3CAM2Y02", 
        "EB465P3CAM3Y02",
        "EB465P3CAM4Y02",
        "EB465P3CAM5Y02",
        "EB500P3CAM1Y02",
        "EB510P3CAM1Y02",
        "EB330P4CAM1Y02", 
        "EB330P4CAM2Y02", 
        "EB349P4CAM1Y02",
        "EB349P4CAM2Y02", 
        "EB357T02P4CAM1Y02",
        "EB357T02P4CAM2Y02",
        "EB405T01P4CAM1Y02",
        "EB410T01P4CAM2Y02",
        "EB420P4CAM1Y02",
        "EB440P4CAM1Y02",
        "EB460P4CAM1Y02", 
        "EB460P4CAM2Y02", 
        "EB460P4CAM3Y02",
        "EB460P4CAM4Y02",
        "EB460P4CAM5Y02",
        "EB465P4CAM1Y02", 
        "EB465P4CAM2Y02", 
        "EB465P4CAM3Y02",
        "EB465P4CAM4Y02",
        "EB465P4CAM5Y02",
        "EB500P4CAM1Y02",
        "EB510P4CAM1Y02",
    ]

destination_directory = r"C:\Users\andrew.poyton\Desktop\testingbackupprogram"


for directory, name in zip(source_directories, source_names):
        try:
            connect_to_network_share(directory)
        except subprocess.CalledProcessError as e:
            print(f"Failed to connect to {directory}: {e}")

        # Proceed with backup logic
        if os.path.exists(directory):
            destination = os.path.join(destination_directory, name)
            try:
                shutil.copytree(directory, destination)
                print(f"Directory '{directory}' copied to '{destination}'")
                # Zip the copied directory
                zip_file = os.path.join(destination_directory, f"{name}.zip")
                with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(destination):
                        for file in files:
                            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(destination, '..')))
                print(f"Directory '{name}' zipped to '{zip_file}'")

            except shutil.Error as e:
                print(f"Error during {name} -> Skipping and continuing with the rest of the directory")
        else:
            print(f"Directory '{directory}' does not exist, skipping...")



def connect_to_network_share(directory):
    # Replace these with your actual credentials and network path
    username = 'mtxuser'
    password = 'Matrox'

    # Use the 'net use' command to connect to the network share
    command = f"net use {directory} /user:{username} {password}"
    subprocess.run(command, shell=True, check=True)