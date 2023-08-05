from pathlib import Path
from .core import run_binary

def cda2dcm(
        cdafile_in: Path = Path(),
        dcmfile_out: Path = Path(),
        options: list = []
    ):
    """
    SYNOPSIS

        cda2dcm [options] cdafile-in dcmfile-out

    DESCRIPTION

        The cda2dcm utility reads a CDA file (cdafile-in), converts it to a DICOM Encapsulated CDA Storage SOP instance and stores the converted data to an output file (dcmfile-out).

    PARAMETERS

        cdafile-in   CDA input filename to be encapsulated

        dcmfile-out  DICOM output filename

    OPTIONS

        general options

        -h   --help
             print this help text and exit

        --version
             print version information and exit

        --arguments
             print expanded command line arguments

        -q   --quiet
             quiet mode, print no warnings and errors

        -v   --verbose
             verbose mode, print processing details

        -d   --debug
             debug mode, print debug information

        -ll  --log-level  [l]evel: string constant
             (fatal, error, warn, info, debug, trace)
             use level l for the logger

        -lc  --log-config  [f]ilename: string
             use config file f for the logger

        DICOM document options

        document title:

        +t   --title  [t]itle: string (default: empty)
             document title

        +cn  --concept-name  [CSD] [CV] [CM]: string (default: empty)
             coded representation of document title defined by coding
             scheme designator CSD, code value CV and code meaning CM

        patient data:

        +pn  --patient-name  [n]ame: string
             patient's name in DICOM PN syntax

        +pi  --patient-id  [i]d: string
             patient identifier

        +pb  --patient-birthdate  [d]ate: string (YYYYMMDD)
             patient's birth date

        +ps  --patient-sex  [s]ex: string (M, F or O)
             patient's sex

        study and series:

        +sg  --generate
             generate new study and series UIDs (default)

        +st  --study-from  [f]ilename: string
             read patient/study data from DICOM file

        +se  --series-from  [f]ilename: string
             read patient/study/series data from DICOM file

        instance number:

        +i1  --instance-one
             use instance number 1 (default, not with +se)

        +ii  --instance-inc
             increment instance number (only with +se)

        +is  --instance-set [i]nstance number: integer
             use instance number i

        burned-in annotation:

        +an  --annotation-yes
             document contains patient identifying data (default)

        -an  --annotation-no
             document does not contain patient identifying data

        override CDA file data:

        -ov  --no-override
             CDA patient and document data must match study,
             series or manually entered information (default)

        +ov  --override
             data obtained from the CDA file will be overwritten
             by study, series, or manually entered information

        processing options

        other processing options:

        -k   --key  [k]ey: gggg,eeee="str", path or dictionary name="str"
             add further attribute

        output options

        output file format:

        +F   --write-file
             write file format (default)

        -F   --write-dataset
             write data set without file meta information

        group length encoding:

        +g=  --group-length-recalc
             recalculate group lengths if present (default)

        +g   --group-length-create
             always write with group length elements

        -g   --group-length-remove
             always write without group length elements

        length encoding in sequences and items:

        +e   --length-explicit
             write with explicit lengths (default)

        -e   --length-undefined
             write with undefined lengths

        data set trailing padding (not with --write-dataset):

        -p   --padding-off
             no padding (implicit if --write-dataset)

        +p   --padding-create  [f]ile-pad [i]tem-pad: integer
             align file on multiple of f bytes
             and items on multiple of i bytes

    """

    parameters = [
        str(cdafile_in),
        str(dcmfile_out)
    ]

    return run_binary('cda2dcm', parameters + options)
