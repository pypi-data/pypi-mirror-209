from pathlib import Path
from .core import run_binary

def dcmdjpeg(
        dcmfile_in: Path = Path(),
        dcmfile_out: Path = Path(),
        options: list = []
    ):
    """
    SYNOPSIS

        dcmdjpeg [options] dcmfile-in dcmfile-out

    DESCRIPTION

        The dcmdjpeg utility reads a JPEG-compressed DICOM image (dcmfile-in), decompresses the JPEG data (i. e. conversion to a native DICOM transfer syntax) and writes the converted image to an output file (dcmfile-out).
    
    PARAMETERS

        dcmfile-in   DICOM input filename to be converted

        dcmfile-out  DICOM output filename

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

        input file format:

        +f    --read-file
             read file format or data set (default)

        +fo   --read-file-only
             read file format only

        -f    --read-dataset
          read data set without file meta information

        This option allows one to decompress JPEG compressed DICOM objects that
        have been stored as dataset without meta-header. Such a thing should
        not exist since the transfer syntax cannot be reliably determined,
        without meta-header but unfortunately it does.

        processing options

        color space conversion:

        +cp   --conv-photometric
             convert if YCbCr photometric interpretation (default)

        If the compressed image uses YBR_FULL or YBR_FULL_422 photometric
        interpretation, convert to RGB during decompression.

        +cl   --conv-lossy
             convert YCbCr to RGB if lossy JPEG

        If the compressed image is encoded in lossy JPEG, assume YCbCr
        color model and convert to RGB.

        +cg   --conv-guess
             convert to RGB if YCbCr is guessed by library

        If the underlying JPEG library "guesses" the color space of the
        compressed image to be YCbCr, convert to RGB.

        +cgl  --conv-guess-lossy
             convert to RGB if lossy JPEG and YCbCr is
             guessed by the underlying JPEG library

        If the compressed image is encoded in lossy JPEG and the underlying
        JPEG library "guesses" the color space to be YCbCr, convert to RGB.

        +ca   --conv-always
             always convert YCbCr to RGB

        If the compressed image is a color image, assume YCbCr color model
        and convert to RGB.

        +cn   --conv-never
             never convert YCbCr to RGB

        Never convert color space from YCbCr to RGB during decompression.
        Note that a conversion from YBR_FULL_422 to YBR_FULL will still take
        place if the source images has been compressed with subsampling.

        planar configuration:

        +pa   --planar-auto
             automatically determine planar configuration
             from SOP class and color space (default)

        If the compressed image is a color image, store in color-by-plane
        planar configuration if required by the SOP class and photometric
        interpretation. Hardcopy Color images are always stored color-by-
        plane, and the revised Ultrasound image objects are stored color-by-
        plane if the color model is YBR_FULL.  Everything else is stored
        color-by-pixel.

        +px   --color-by-pixel
             always store color-by-pixel

        If the compressed image is a color image, store in color-by-pixel
        planar configuration.

        +pl   --color-by-plane
             always store color-by-plane

        If the compressed image is a color image, store in color-by-plane
        planar configuration.

        SOP Instance UID:

        +ud   --uid-default
             keep same SOP Instance UID (default)

        Never assigns a new SOP instance UID.

        +ua   --uid-always
             always assign new UID

        Always assigns a new SOP instance UID.

        workaround options for incorrect JPEG encodings:

        +w6   --workaround-pred6
             enable workaround for JPEG lossless images
             with overflow in predictor 6

        DICOM images with 16 bits/pixel have been observed "in the wild"
        that are compressed with lossless JPEG and need special handling
        because the encoder produced an 16-bit integer overflow in predictor
        6, which needs to be compensated (reproduced) during decompression.
        This flag enables a correct decompression of such faulty images, but
        at the same time will cause an incorrect decompression of correctly
        compressed images. Use with care.

        +wi   --workaround-incpl
             enable workaround for incomplete JPEG data

        This option causes dcmjpeg to ignore incomplete JPEG data
        at the end of a compressed fragment and to start decompressing
        the next frame from the next fragment (if any). This permits
        images with incomplete JPEG data to be decoded.

        +wc   --workaround-cornell
             enable workaround for 16-bit JPEG lossless
             Cornell images with Huffman table overflow

        One of the first open-source implementations of lossless JPEG
        compression, the "Cornell" library, has a well-known bug that leads
        to invalid values in the Huffmann table when images with 16 bit/sample
        are compressed. This flag enables a workaround that permits such
        images to be decoded correctly.

        output options

        output file format:

        +F    --write-file
             write file format (default)

        -F    --write-dataset
             write data set without file meta information

        output transfer syntax:

        +te   --write-xfer-little
             write with explicit VR little endian (default)

        +tb   --write-xfer-big
             write with explicit VR big endian TS

        +ti   --write-xfer-implicit
             write with implicit VR little endian TS

        post-1993 value representations:

        +u    --enable-new-vr
             enable support for new VRs (UN/UT) (default)

        -u    --disable-new-vr
             disable support for new VRs, convert to OB

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

        -p=   --padding-retain
             do not change padding (default if not --write-dataset)

        -p    --padding-off
             no padding (implicit if --write-dataset)

        +p    --padding-create  [f]ile-pad [i]tem-pad: integer
             align file on multiple of f bytes
             and items on multiple of i bytes

    TRANSFER SYNTAXES

        dcmdjpeg supports the following transfer syntaxes for input (dcmfile-in):

        LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
        LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
        DeflatedExplicitVRLittleEndianTransferSyntax   1.2.840.10008.1.2.1.99 (*)
        BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
        JPEGProcess1TransferSyntax                     1.2.840.10008.1.2.4.50
        JPEGProcess2_4TransferSyntax                   1.2.840.10008.1.2.4.51
        JPEGProcess6_8TransferSyntax                   1.2.840.10008.1.2.4.53
        JPEGProcess10_12TransferSyntax                 1.2.840.10008.1.2.4.55
        JPEGProcess14TransferSyntax                    1.2.840.10008.1.2.4.57
        JPEGProcess14SV1TransferSyntax                 1.2.840.10008.1.2.4.70

        (*) if compiled with zlib support enabled

        dcmdjpeg supports the following transfer syntaxes for output (dcmfile-out):

        LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
        LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
        BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
    """

    parameters = [
        str(dcmfile_in),
        str(dcmfile_out)
    ]

    return run_binary('dcmdjpeg', parameters + options)
