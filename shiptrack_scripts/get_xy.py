import csv
import re
import os
import subprocess


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
    cruise_id.replace('b\'', '')
    cruise_id.replace('\'', '')
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
        

    # Start reading CSVs
    for csv_file in csv_file_list:
        try:
            with open(csv_file) as f, open(os.path.join(out_dir, out_file)) as writer:
                reader = csv.DictReader(f)

                # Discard title line
                skipping = next(f)
                if debug:
                    print(f'skipping title: {skipping}')

                # Read content
                a = True
                for row in reader:
                    lat = row.get('Dec_LAT')
                    lon = row.get('Dec_LON')
                    date = row.get('DATE_GMT')
                    time = row.get('TIME_GMT')
                    # Check for valid lat/lon
                    if isinstance(lon, float) and isinstance(lat, float):
                        print('writing')
                        writer.write(f'{lon}, {lat}, {time}, {date}')
                        lats.append(lat)
                        lons.append(lon)
        except FileNotFoundError:
            print(f'Unable to open file \'{csv_file}.\'')

    if lats and lons:

         # Write min and max values
        lats = sorted(lats)
        lah = lats[-1]
        lal = lats[0]

        lons = sorted(lons)
        lol = lons[0]
        loh = lons[-1]

        with open(f"{output_dir}/{minmax}", "w") as minmax_file:
            minmax_file.write(f"{lal}, {lah}, {lol}, {loh}\n")

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
