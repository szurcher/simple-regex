"""simple_regex.regex: provides entry point to main()."""

__version__ = "0.1.0"

import argparse, logging, mmap, re, sys

def main():
    # Process command line arguments
    parser = argparse.ArgumentParser(
        description="Regular expression find and replace."
        )
    parser.add_argument('-x', '--debug', nargs='?', default='ERROR',
                        help=("Specify debug output level (results in "
                              "regex.log)"))
    parser.add_argument('find', help="Pattern to use in searches.")
    parser.add_argument('replace',
                        help=("Python format string to use for replacing "
                              "matches."))
    parser.add_argument('infile', type=argparse.FileType('r+'),
                        help='File to be searched.')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='File to output modified result.')

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        filename="regex.log",
        format='%(asctime)s: %(message)s',
        datefmt="%F %T%z",
        level=args.debug # if not given on command line, defaults to ERROR
        )

    final = args.find

    p = re.compile(final.encode('utf-8'))

    rep = args.replace

    logging.info("Find:    " + final)
    logging.info("Replace: " + rep)

    out = args.outfile

    with args.infile as f:
        data = mmap.mmap(f.fileno(),0)
        lastLoc = 0

        # Iterate over matches, write out data from last location up to match,
        # then match replacement
        for m in p.finditer(data):
            mLen = m.end() - m.start()  # match length

            m.string.seek(m.start()) # m.string points into data mmap
            mStr = m.string.read(mLen)

            logging.info("Match found at {} of length {} in string: {}".format(
                str(m.start()),str(mLen),mStr.decode("utf-8")
            ))

            # Convert match results from binary strings
            a = [x.decode("utf-8") for x in m.groups(b"")]
            # format replacement string for match
            rStr = rep.format(*a)
            rLen = len(rStr)
            logging.info("Replacement: {}".format(rStr))

            # Get map offset for match
            offset = data.tell() - mLen

            data.seek(offset)
            sample = data.read(mLen)
            logging.info("Data read at offset {} of size {}: {}".format(
                str(offset), str(mLen), sample.decode("utf-8")
            ))

            # Shouldn't be possible
            if offset < 0:
                offset = 0

            # Move to end point of last write
            data.seek(lastLoc)
            out.write(data.read(offset - lastLoc).decode("utf-8"))
            out.write(rStr)

            # Update location offset value and move file pointer
            lastLoc = offset + mLen
            data.seek(lastLoc)

        # Output the remainder of the file (if any)
        data.seek(lastLoc)
        fSz = data.size()
        out.write(data.read(fSz - lastLoc).decode("utf-8"))
        data.close()

    f.close()
    out.close()

