import os
import subprocess

def get_data(in_file, writer, debug=False):
    """Reads the gmt.xy file and writes coordinates to the KML file."""
    if debug:
        print(f'Reading from {in_file}')
    try:
        with open(in_file, 'r') as infile:
            for line in infile:
                lon, lat, time, date = line.split(',')
                if debug:
                    print(f'{lon},{lat}')
                writer.write(f'{lon.strip()},{lat.strip()}\n')
    except FileNotFoundError:
        print(f'No such file: {in_file}')
        return

def create_kml():
    debug = True

    in_file = "gmt.xy"
    dir = "/home/data/shiptrack"

    # Retrieve cruise ID
    cruiseid = subprocess.check_output(['cat', '/home/data/CRUISE_ID']).decode('utf-8').strip()

    outfile = f'{cruiseid}.kml'
    if debug:
        print(f'outfile = {outfile}')

    try:
        # Open the KML output file
        with open(os.path.join(dir, outfile), 'w') as writer:
            if debug:
                print(f'Creating KML file: {os.path.join(dir, outfile)}')

            # Write KML header
            writer.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            writer.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            writer.write('<Document>\n')
            writer.write('<Placemark>\n')
            writer.write(f'<name> {cruiseid} </name>\n')
            writer.write('<description>\n')
            writer.write('<![CDATA[\n')
            writer.write(f'<h5> {cruiseid} </h5>\n')
            writer.write(']]>\n')
            writer.write('</description>\n')
            writer.write('<Style>\n')
            writer.write('<LineStyle>\n')
            writer.write('<color>501400D2</color>\n')
            writer.write('</LineStyle>\n')
            writer.write('</Style>\n')
            writer.write('<LineString>\n')
            writer.write('<coordinates>\n')

            # Write data coordinates
            file_path = os.path.join(dir, in_file)
            get_data(file_path, writer, debug=debug)

            # Write KML footer
            writer.write('</coordinates>\n')
            writer.write('</LineString>\n')
            writer.write('</Placemark>\n')
            writer.write('</Document>\n')
            writer.write('</kml>\n')
    except IOError as e:
        print(f'Cannot create KML file: {e}')

if __name__ == '__main__':
    create_kml()