from pathlib import Path
from .core import run_binary


def img2dcm(
        imgfile_in: Path = Path(),
        dcmfile_out: Path = Path(),
        options: list = [],
    ):

    """
    SYNOPSIS

        img2dcm [options] imgfile-in dcmfile-out

    DESCRIPTION

        The img2dcm tool serves as a conversion tool from a standard image format like JPEG or BMP
        to DICOM. Different output  SOP  Classes  can  be  selected.  The  additional  information
        (regarding  patients,  series, etc.) stored in the DICOM output file can be extracted from
        other DICOM files which serve as a 'template' for the resulting DICOM object. img2dcm  can
        also  be  configured  to  invent  missing  DICOM type 1 and type 2 attributes to work even
        without any template dataset.

    PARAMETERS

        imgfile-in   image file to be imported

        dcmfile-out  DICOM output file

    OPTIONS

        general options
        
        -h    --help
             print this help text and exit

        --version
             print version information and exit

        --arguments
             print expanded command line arguments

        -q    --quiet
             quiet mode, print no warnings and errors

        -v    --verbose
             verbose mode, print processing details

        -d    --debug
             debug mode, print debug information

        -ll   --log-level  [l]evel: string constant
             (fatal, error, warn, info, debug, trace)
             use level l for the logger

        -lc   --log-config  [f]ilename: string
             use config file f for the logger

        input options
        
        general:

        -i    --input-format  [i]nput file format: string
             supported formats: JPEG (default), BMP

        -df   --dataset-from  [f]ilename: string
             use dataset from DICOM file f

        -stf  --study-from  [f]ilename: string
             read patient/study from DICOM file f

        -sef  --series-from  [f]ilename: string
             read patient/study/series from DICOM file f

        -ii   --instance-inc
             increase instance number read from DICOM file

        JPEG format:

        -dp   --disable-progr
             disable support for progressive JPEG

        -de   --disable-ext
             disable support for extended sequential JPEG

        -jf   --insist-on-jfif
             insist on JFIF header existence

        -ka   --keep-appn
             keep APPn sections (except JFIF)

        processing options
            
        attribute checking:

        --do-checks
             enable attribute validity checking (default)

        --no-checks
             disable attribute validity checking

        +i2   --insert-type2
             insert missing type 2 attributes (default)
             (only with --do-checks)

        -i2   --no-type2-insert
             do not insert missing type 2 attributes
             (only with --do-checks)

        +i1   --invent-type1
             invent missing type 1 attributes
             (only with --do-checks)

        -i1   --no-type1-invent
             do not invent missing type 1 attributes
             (only with --do-checks)

        character set:

        +l1   --latin1
             set latin-1 as standard character set (default)

        -l1   --no-latin1
             keep 7-bit ASCII as standard character set

        other processing options:

        -k    --key  [k]ey: gggg,eeee="str", path or dictionary name="str"
             add further attribute

    output options
 
    target SOP class:

        -sc   --sec-capture
             write Secondary Capture SOP class

        -nsc  --new-sc
             write new Secondary Capture SOP classes

        -vlp  --vl-photo
             write Visible Light Photographic SOP class (default)

    output file format:

        +F    --write-file
                 write file format (default)

        -F    --write-dataset
             write data set without file meta information

    group length encoding:

        +g=   --group-length-recalc
             recalculate group lengths if present (default)

        +g    --group-length-create
             always write with group length elements

        -g    --group-length-remove
             always write without group length elements

    length encoding in sequences and items:

        +e    --length-explicit
             write with explicit lengths (default)

        -e    --length-undefined
             write with undefined lengths

    data set trailing padding (not with --write-dataset):

        -p    --padding-off
             no padding (implicit if --write-dataset)

        +p    --padding-create  [f]ile-pad [i]tem-pad: integer
             align file on multiple of f bytes
             and items on multiple of i bytes
    """

    parameters = [
        str(imgfile_in),
        str(dcmfile_out)
    ]

    return run_binary('img2dcm', parameters + options)
