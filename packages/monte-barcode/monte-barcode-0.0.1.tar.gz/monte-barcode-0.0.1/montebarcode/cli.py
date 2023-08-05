"""Command-line interface for monte-barcode."""

from typing import TextIO
from collections.abc import Callable, Mapping, Sequence
import argparse
import csv
from functools import reduce
from itertools import permutations
from math import factorial
import operator
import sys

import nemony as nm
import streq as sq
from tqdm import tqdm

from .generate import codon_barcodes, infinite_barcodes
from . import checks
from .utils import pprint_dict, _CODONS


def _reader(input: TextIO, 
            field: int) -> Sequence[str]:

    infile = csv.reader(input, delimiter='\t')
    barcode_list = [row[field - 1] for row in infile]
    alphabet_used = set(letter for bc in barcode_list for letter in list(bc))

    assert all(letter in sq.sequences.DNA for letter in alphabet_used),\
               (f"ERROR: Letters other than {sq.sequences.DNA} are "
                f"used in column {field} of {input.name}")
    
    return barcode_list


def _writer(output: TextIO, 
            barcodes: Sequence[str], 
            levenshtein: bool = False) -> None:

    barcode_set_name = nm.encode(barcodes)

    outfile = csv.writer(output, 
                         delimiter='\t')
    min_distance, max_distance = checks.minmax_distance(barcodes, levenshtein)
    n = len(barcodes)
    
    try:

        for i, barcode in enumerate(barcodes):
            row = (f'{barcode_set_name}:'
                   f'l{len(barcode)}-n{n}-d{min_distance}:'
                   f'x{i}:{nm.encode(barcode)}'), barcode
            outfile.writerow(row)

    except BrokenPipeError:

        pass

    distance = 'Levenshtein' if levenshtein else 'Hamming'
        
    print(f'Wrote barcode set called {barcode_set_name},',
          f'with minimum {distance} distance {min_distance} and',
          f'maximum {distance} distance {max_distance}.', 
          file=sys.stderr)
    
    return None


def _checker(args: argparse.Namespace, 
             barcode_list: Sequence[str]) -> Sequence[str]:

    checklist = [checks.Identities(), 
                 checks.Palindrome(),
                 checks.Distance(min_distance=args.distance,
                                 use_levenshtein=args.levenshtein),
                 checks.GCcontent(min=args.gc_min, 
                                  max=args.gc_max),
                 checks.Homopolymer(length=args.homopolymer),
                 checks.RestrictionSites()]
    
    if args.color:
        checklist += [checks.IlluminaColorBalance()]

    try:
        n = len(barcode_list)
        max_rejection_rate = 1.
    except TypeError:
        n = args.number
        max_rejection_rate = args.rejection_rate

    _, _, barcodes = checks.make_checks(barcode_list,
                                 n=n, 
                                 max_rejection_rate=max_rejection_rate,
                                 checks=checklist)
    
    if len(barcodes) < n:

        print(f'Could only generate {len(barcodes)} barcodes,',
              f'but {n} were requested.',
              'You might need to try different settings.',
              file=sys.stderr)
    
    _writer(args.output, barcodes, args.levenshtein)

    return barcodes


def _check_permutations(barcodes: Sequence[str], 
                        checklist: Sequence[Callable[[str, Sequence[str]], bool]],
                        constant: Sequence[str] = [],
                        n: int = None) -> Sequence[Mapping, Sequence[str]]:

    n = n or len(barcodes)
    n_permutations = int(factorial(len(barcodes)) / 
                         factorial(len(barcodes) - n))
   
    result = None

    for permutation in tqdm(permutations(barcodes, n), 
                            total=n_permutations):

        try:
            fail_tally, _, result = checks.make_checks(constant + list(permutation),
                                                n=len(permutation),
                                                max_rejection_rate=0.,
                                                checks=checklist,
                                                max_tries=0,
                                                quiet=True)
        except ValueError:

            pass

        else:

            break

    if result is None:

        raise ValueError('Ordering could not be found to satisfy checks.')
    
    return fail_tally, result


def sort_barcodes(args: argparse.Namespace) -> None:

    pprint_dict(vars(args), 
                'Sorting barcodes with the following parameters') 
    
    barcode_list = _reader(args.input, args.field)
    
    checklist = [checks.IlluminaColorBalance()]

    try:
        
        _, _, barcodes = checks.make_checks(barcode_list,
                                              n=len(barcode_list),
                                              max_rejection_rate=0.,
                                              checks=checklist,
                                              max_tries=0,
                                              quiet=True)
        
    except ValueError:
        
        _, starter_barcodes = _check_permutations(barcode_list, 
                                                  checklist, n=6)
        remaining_barcodes = list(set(barcode_list) - 
                                  set(starter_barcodes))

        _, barcodes = _check_permutations(remaining_barcodes, 
                                          checklist,
                                          constant=list(starter_barcodes))
        # barcodes = list(starter_barcodes) + list(barcodes)

    if len(barcodes) < len(barcode_list):

        print(f'Could only generate {len(barcodes)} barcodes,',
              f'but {len(barcode_list)} were provided.',
              'You might need to try different settings.',
              file=sys.stderr)

    _writer(args.output, barcodes)
    
    return None


def check_barcodes(args: argparse.Namespace) -> None:

    pprint_dict(vars(args), 
                 'Checking barcodes with the following parameters') 
    
    barcode_list = _reader(args.input, args.field)
    
    barcodes = _checker(args, barcode_list)
    
    return None


def generate(args: argparse.Namespace) -> None:

    pprint_dict(vars(args), 
                'Generating barcodes with the following parameters')
    
    if args.amino_acid is not None:

        invalid_aa = [aa for aa in args.amino_acid if aa not in _CODONS]

        assert len(invalid_aa) == 0, "The following amino acids are invalid: {}".format(", ".join(invalid_aa))

        length = len(args.amino_acid) * 3
        combinations = reduce(operator.mul, (len(_CODONS[aa]) for aa in args.amino_acid))
        print(f'Using amino acid sequence {args.amino_acid} with',
              f'length {length} and {combinations} possible combinations.',
              file=sys.stderr)
        
        barcodes = codon_barcodes(args.amino_acid)

    else:

        length = args.length
        alphabet_length = len(sq.sequences.DNA)
        combinations = alphabet_length ** args.length

        print(f'Requested barcodes with length {length},',
              f'and {combinations} possible combinations.',
              file=sys.stderr)
        
        barcodes = infinite_barcodes(length)
    
    assert combinations > args.number,\
            f'There are not {args.number} unique {length}-mers. '\
            f'Maximum is {combinations}.'

    barcodes = _checker(args, barcodes)

    return None
    

def main() -> None:

    parser = argparse.ArgumentParser(description='''
    Generate random DNA barcodes conforming to contraints, or 
    check sets of barcodes for their conformance.
    ''')

    subcommands = parser.add_subparsers(title='Sub-commands', 
                                        dest='subcommand',
                                        help='Use these commands to specify the action you want.')
    
    barcode = subcommands.add_parser('barcode', 
                                      help='Generate random barcodes.')
    barcode.set_defaults(func=generate)
    check = subcommands.add_parser('check', 
                                    help='Check barcode list.')
    check.set_defaults(func=check_barcodes)
    sort = subcommands.add_parser('sort', 
                                  help='Sort barcode list for optimal color balance.')
    sort.set_defaults(func=sort_barcodes)
    
    barcode.add_argument('--number', '-n', 
                         type=int, required=True,
                         help='Number of barcodes to generate. Required.')
    barcode.add_argument('--length', '-l', 
                         type=int, default=12,
                         help='Barcode length. Default: %(default)s')
    barcode.add_argument('--rejection-rate', '-r', 
                         type=float, default=.85,
                         help='Rate of rejection before aborting. Default: %(default)s')
    barcode.add_argument('--amino-acid', '-a', 
                         type=str, 
                         default=None,
                         help='Generate barcodes encoding this amino acid sequence. Default: do not use.')
    
    for p in (barcode, check):
    
        p.add_argument('--distance', '-d', 
                       type=int, default=1,
                       help='Minimum distance between barcodes. Default: %(default)s')
        p.add_argument('--homopolymer', '-p', 
                       type=int, default=3,
                       help='Maximum homopolymer length. Default: %(default)s')
        p.add_argument('--levenshtein', '-e', 
                       action='store_true',
                       help='Use Levenshtein distance. Otherwise '
                            'using Hamming diatnce. Default: %(default)s')
        p.add_argument('--color', '-c', 
                       action='store_true',
                       help='Check optimal Illumina color balance. Default: %(default)s')
        p.add_argument('--gc_min', '-g', 
                       type=float, default=.4,
                       help='Minimum GC content. Default: %(default)s')
        p.add_argument('--gc_max', '-j', 
                       type=float, default=.6,
                       help='Maximum GC content. Default: %(default)s')
        
    for p in (check, sort):

        p.add_argument('input',
                    type=argparse.FileType('r'),
                    nargs='?',
                    default=sys.stdin,
                    help='Input file. Default: STDIN.')
        p.add_argument('--field', '-f',
                    type=int,
                    default=1,
                    help='Column number for barcode sequences. Default: %(default)s')
        
    for p in (barcode, check, sort):

        p.add_argument('--output', '-o', 
                       type=argparse.FileType('w'),
                       default=sys.stdout,
                       help='Output file. Default: STDOUT')
        
    args = parser.parse_args()
    args.func(args)

    return None


if __name__ == "__main__":

    main()