import os
import subprocess

#################################################
def create_kml_file(data_file, data_dir, cruise_id, debug=False):
    """
    Create the output file for the xy data and write to it

    data_file: should be like gmt.xy
    data_dir: should be something like /home/data/shiptrack
    cruise_id: should be something like ar84-01
    """
    in_file = os.path.join(data_dir, data_file)
    if debug:
        print(f'in_file = {in_file}')

    out_file = os.path.join(data_dir, f"{cruise_id}.kml")
    if debug:
        print(f'out_file = {out_file}\n')

    with open(out_file, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write('<Document>\n')
        f.write('<Placemark>\n')
        f.write(f'<name> {cruise_id} </name>\n')
        f.write('<description>\n')
        f.write('<![CDATA[\n')
        f.write(f'<h5> {cruise_id} </h5>\n')
        f.write(']]>\n')
        f.write('</description>\n')
        f.write('<Style>\n')
        f.write('      <LineStyle>\n')
        f.write('      <color>501400D2</color>\n')
        f.write('      </LineStyle>\n')
        f.write(' </Style>\n')
        f.write('<LineString>\n')
        f.write('<coordinates>\n')

        process_data(os.path.join(data_dir, in_file), f)

        f.write('</coordinates>\n')
        f.write('</LineString>\n')
        f.write('</Placemark>\n')
        f.write('</Document>\n')
        f.write('</kml>\n')
    
#################################################
def process_data(in_file, out_file):
    """
    Process the data from in_file and write to out_file if exists
    
    in_file: should be something like gmt.xy
    out_file: should be something like ar84-01.kml
    """
    try:
        with open(in_file, 'r') as f:
            for line in f:
                lon, lat, *timestamp = line.strip().split(',')
                if isinstance(lon, float) and isinstance(lat, float):
                    out_file.write(f'{float(lon)},{float(lat)}\n')
    except FileNotFoundError:
        print(f'Invalid data file path: {in_file}')

#################################################
if __name__ == 'main':
    in_file = 'gmt.xy'
    data_dir = '/home/data/shiptrack'
    cruise_id = subprocess.check_output([f'cat /home/data/CRUISE_ID']).rstrip('\n')

    debug = True

    create_kml_file(in_file, data_dir, cruise_id, debug)