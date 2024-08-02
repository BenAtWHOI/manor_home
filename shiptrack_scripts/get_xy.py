import csv
import re
import os
import subprocess
from datetime import datetime

def strip(s):
    """Helper function to strip leading and trailing whitespace"""
    return s.strip()

if __name__ == '__main__':
    debug = True

    out_file = 'gmt.xy'
    out_dir = '/home/data/shiptrack'
    data_dir = '/home/data/underway/proc'
    last_out = f'{out_dir}/last.xy'
    label = f'{out_dir}/gmt.label'
    minmax = f'{out_dir}/minmax'

    #########################################
    # out_dir='/home/atlas/WHOI/ship_tracker'
    #########################################

    cmd = subprocess.check_output(['cat', '/home/data/CRUISE_ID'])
    cruise_id = cmd.decode('utf-8').strip()
    ship_id = cruise_id[:2]

    if debug:
        print(f'out_file = {out_file}')
        print(f'out_dir = {out_dir}')
        print(f'data_dir = {data_dir}')
        print(f'last_out = {last_out}')
        print(f'label = {label}')
        print(f'minmax = {minmax}')
        print(f'cruise_id = {cruise_id}')
        print(f'ship_id = {ship_id}')

    lats, lons = [], []
    
    # Find all CSVs in the data directory
    csv_file_list = []
    for filename in os.listdir(data_dir):
        if re.search(rf"{ship_id}(\d{{6}})_.*\.csv", filename, flags=re.IGNORECASE):
            csv_file_list.append(os.path.join(data_dir, filename))

    if debug:
        print(f'csv_file_list = {csv_file_list}')
        
    try:
        # Open the output file once outside the loop
        with open(os.path.join(out_dir, out_file), 'w') as writer:
            # Start reading CSVs
            for csv_file in csv_file_list:
                try:
                    with open(csv_file) as f:
                        reader = csv.DictReader(f)

                        # Discard title line
                        skipping = next(f)
                        if debug:
                            print(f'skipping title: {skipping}')

                        # Read content
                        for row in reader:
                            lat_str = strip(row.get('Dec_LAT', ''))
                            lon_str = strip(row.get('Dec_LON', ''))
                            date = strip(row.get('DATE_GMT', ''))
                            time = strip(row.get('TIME_GMT', ''))

                            if lat_str and lon_str:  # check for non-empty strings
                                try:
                                    lat = float(lat_str)
                                    lon = float(lon_str)
                                    # Check for valid lat/lon
                                    writer.write(f'{lon}, {lat}, {time}, {date}\n')
                                    lats.append(lat)
                                    lons.append(lon)
                                except ValueError:
                                    # Handle conversion error
                                    print(f'Invalid lat/lon data: {lat_str}, {lon_str}')
                except FileNotFoundError:
                    print(f'Unable to open file \'{csv_file}\'.')

        if lats and lons:
            # Write min and max values
            lats = sorted(lats)
            lah = lats[-1]
            lal = lats[0]

            lons = sorted(lons)
            lol = lons[0]
            loh = lons[-1]

            with open(f"{out_dir}/{minmax}", "w") as minmax_file:
                minmax_file.write(f"{lal}, {lah}, {lol}, {loh}\n")

            # Current time as placeholders for now and now_t
            now = datetime.now().strftime('%Y-%m-%d')
            now_t = datetime.now().strftime('%H:%M:%S')

            # Write last out values
            with open(last_out, "w") as last_out_file:
                last_out_file.write(f"{lons[-1]} {lats[-1]} {now} {now_t} \n")

            # Write label values
            with open(label, "w") as label_file:
                label_file.write(f"{lons[-1]} {lats[-1]} 16 0 6 1 {cruise_id}\n")

                if lats[-1] < 0:
                    latc = abs(lats[-1])
                    NS = "S"
                else:
                    latc = lats[-1]
                    NS = "N"

                if lons[-1] < 0:
                    lonc = abs(lons[-1])
                    EW = "W"
                else:
                    lonc = lons[-1]
                    EW = "E"

                lastmsg = f"Last position: {latc} {NS}, {lonc} {EW} at {now_t} gmt on {now}\n"
                label_file.write(f"{lons[-1]} {lats[-1]} 14 0 4 1 {lastmsg}\n")
    except IOError as e:
        print(f"Error opening output file: {e}")