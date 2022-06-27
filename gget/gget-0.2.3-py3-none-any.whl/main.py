import argparse
import sys
import logging

# Add and format time stamp in logging messages
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%c",
)
# Mute numexpr threads info
logging.getLogger("numexpr").setLevel(logging.WARNING)

import os
import json

# Custom functions
from .__init__ import __version__
from .gget_ref import ref
from .gget_search import search
from .gget_info import info
from .gget_seq import seq
from .gget_muscle import muscle
from .gget_blast import blast
from .gget_blat import blat
from .gget_enrichr import enrichr
from .gget_archs4 import archs4

from .utils import ref_species_options, find_latest_ens_rel


def main():
    """
    Function containing argparse parsers and arguments to allow the use of gget from the terminal.
    """
    # Define parent parser
    parent_parser = argparse.ArgumentParser(
        description=f"gget v{__version__}", add_help=False
    )
    # Initiate subparsers
    parent_subparsers = parent_parser.add_subparsers(dest="command")
    # Define parent (not sure why I need both parent parser and parent, but otherwise it does not work)
    parent = argparse.ArgumentParser(add_help=False)

    # Add custom help argument to parent parser
    parent_parser.add_argument(
        "-h", "--help", action="store_true", help="Print manual."
    )
    # Add custom version argument to parent parser
    parent_parser.add_argument(
        "-v", "--version", action="store_true", help="Print version."
    )

    ## gget ref subparser
    ref_desc = "Fetch FTPs for reference genomes and annotations by species."
    parser_ref = parent_subparsers.add_parser(
        "ref", parents=[parent], description=ref_desc, help=ref_desc, add_help=True
    )
    # ref parser arguments
    parser_ref.add_argument(
        "species",
        type=str,
        nargs="?",
        default=None,
        help="Species for which the FTPs will be fetched, e.g. homo_sapiens.",
    )
    parser_ref.add_argument(
        "-l",
        "--list_species",
        default=False,
        action="store_true",
        required=False,
        help=(
            """
            List all available species. 
            (Combine with `--release` to get the available species from a specific Ensembl release.)
            """
        ),
    )
    parser_ref.add_argument(
        "-w",
        "--which",
        default="all",
        type=str,
        required=False,
        help=(
            """
        Defines which results to return. \n
        Default: 'all' -> Returns all available results. \n
        Possible entries are one or a combination (as a comma-separated list) of the following: \n
        'gtf' - Returns the annotation (GTF). \n
        'cdna' - Returns the trancriptome (cDNA). \n
        'dna' - Returns the genome (DNA). \n
        'cds - Returns the coding sequences corresponding to Ensembl genes. (Does not contain UTR or intronic sequence.) \n
        'cdrna' - Returns transcript sequences corresponding to non-coding RNA genes (ncRNA). \n
        'pep' - Returns the protein translations of Ensembl genes. \n
        Example: '-w dna,gtf'
        """
        ),
    )
    parser_ref.add_argument(
        "-r",
        "--release",
        default=None,
        type=int,
        required=False,
        help="Ensembl release the FTPs will be fetched from, e.g. 104 (default: latest Ensembl release).",
    )
    parser_ref.add_argument(
        "-ftp",
        "--ftp",
        default=False,
        action="store_true",
        required=False,
        help="Return only the FTP link(s).",
    )
    parser_ref.add_argument(
        "-d",
        "--download",
        default=False,
        action="store_true",
        required=False,
        help="Download FTPs to the current directory using curl.",
    )
    parser_ref.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the file the results will be saved in, e.g. path/to/directory/results.json.\n"
            "Default: Standard out."
        ),
    )
    parser_ref.add_argument(
        "-s",
        "--species",
        type=str,
        required=False,
        dest="species_deprecated",
        help="DEPRECATED - use positional argument instead. Species for which the FTPs will be fetched, e.g. homo_sapiens.",
    )

    ## gget search subparser
    search_desc = (
        "Fetch gene and transcript IDs from Ensembl using free-form search terms."
    )
    parser_gget = parent_subparsers.add_parser(
        "search",
        parents=[parent],
        description=search_desc,
        help=search_desc,
        add_help=True,
    )
    # Search parser arguments
    parser_gget.add_argument(
        "searchwords",
        type=str,
        nargs="*",
        default=None,
        help="One or more free form search words, e.g. gaba, nmda.",
    )
    parser_gget.add_argument(
        "-s",
        "--species",
        type=str,
        required=True,
        help="Species to be queried, e.g. homo_sapiens.",
    )
    parser_gget.add_argument(
        "-t",
        "--id_type",
        choices=["gene", "transcript"],
        default="gene",
        type=str,
        required=False,
        help=(
            "'gene': Returns genes that match the searchwords. (default).\n"
            "'transcript': Returns transcripts that match the searchwords. \n"
        ),
    )
    parser_gget.add_argument(
        "-ao",
        "--andor",
        choices=["and", "or"],
        default="or",
        type=str,
        required=False,
        help=(
            "'or': Gene descriptions must include at least one of the searchwords (default).\n"
            "'and': Only return genes whose descriptions include all searchwords.\n"
        ),
    )
    parser_gget.add_argument(
        "-l",
        "--limit",
        type=int,
        default=None,
        required=False,
        help="Limits the number of results, e.g. 10 (default: None).",
    )
    parser_gget.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_gget.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the file the results will be saved in, e.g. path/to/directory/results.json.\n"
            "Default: Standard out."
        ),
    )
    parser_gget.add_argument(
        "-sw",
        "--searchwords",
        type=str,
        nargs="+",
        required=False,
        dest="sw_deprecated",
        help="DEPRECATED - use positional argument instead. One or more free form search words, e.g. gaba, nmda.",
    )
    parser_gget.add_argument(
        "--seqtype",
        default=None,
        type=str,
        required=False,
        help="DEPRECATED - use argument 'id_type' instead.",
    )
    parser_gget.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ## gget info subparser
    info_desc = "Fetch gene and transcript metadata using Ensembl IDs."
    parser_info = parent_subparsers.add_parser(
        "info", parents=[parent], description=info_desc, help=info_desc, add_help=True
    )
    # info parser arguments
    parser_info.add_argument(
        "ens_ids",
        type=str,
        nargs="*",
        default=None,
        help="One or more Ensembl, WormBase or FlyBase IDs).",
    )
    parser_info.add_argument(
        "-e",
        "--expand",
        default=False,
        action="store_true",
        required=False,
        help=("DEPRECATED - gget info now always returns all available information."),
    )
    parser_info.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_info.add_argument(
        "-q",
        "--quiet",
        default=True,
        action="store_false",
        required=False,
        help="Do not print progress information.",
    )
    parser_info.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to file the results will be saved as, e.g. path/to/directory/results.json.\n"
            "Default: Standard out."
        ),
    )
    parser_info.add_argument(
        "-id",
        "--ens_ids",
        type=str,
        nargs="+",
        required=False,
        dest="id_deprecated",
        help="DEPRECATED - use positional argument instead. One or more Ensembl, WormBase or FlyBase IDs).",
    )
    parser_info.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ## gget seq subparser
    seq_desc = "Fetch nucleotide or amino acid sequence (FASTA) of a gene (and all isoforms) or transcript by Ensembl, WormBase or FlyBase ID. "
    parser_seq = parent_subparsers.add_parser(
        "seq", parents=[parent], description=seq_desc, help=seq_desc, add_help=True
    )
    # seq parser arguments
    parser_seq.add_argument(
        "ens_ids",
        type=str,
        nargs="*",
        default=None,
        help="One or more Ensembl, WormBase or FlyBase IDs.",
    )
    parser_seq.add_argument(
        "-t",
        "--translate",
        default=False,
        action="store_true",
        required=False,
        help=(
            "Returns amino acid sequences from UniProt. (Otherwise returns nucleotide sequences from Ensembl.)"
        ),
    )
    parser_seq.add_argument(
        "-iso",
        "--isoforms",
        default=False,
        action="store_true",
        required=False,
        help="Returns sequences of all known transcripts (default: False). (Only for gene IDs.)",
    )
    parser_seq.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the FASTA file the results will be saved in, e.g. path/to/directory/results.fa.\n"
            "Default: Standard out."
        ),
    )
    parser_seq.add_argument(
        "-id",
        "--ens_ids",
        type=str,
        nargs="+",
        required=False,
        dest="id_deprecated",
        help="DEPRECATED - use positional argument instead. One or more Ensembl, WormBase or FlyBase IDs.",
    )
    parser_seq.add_argument(
        "--seqtype",
        default=None,
        type=str,
        required=False,
        help="DEPRECATED - use True/False flag 'translate' instead.",
    )
    parser_seq.add_argument(
        "--transcribe",
        default=None,
        action="store_true",
        required=False,
        help="DEPRECATED - use True/False flag 'translate' instead.",
    )

    ## gget muscle subparser
    muscle_desc = "Align multiple nucleotide or amino acid sequences against each other (using the Muscle v5 algorithm)."
    parser_muscle = parent_subparsers.add_parser(
        "muscle",
        parents=[parent],
        description=muscle_desc,
        help=muscle_desc,
        add_help=True,
    )
    # muscle parser arguments
    parser_muscle.add_argument(
        "fasta",
        type=str,
        nargs="?",
        default=None,
        help="Path to fasta file containing the sequences to be aligned.",
    )
    parser_muscle.add_argument(
        "-s5",
        "--super5",
        default=False,
        action="store_true",
        required=False,
        help="If True, align input using Super5 algorithm instead of PPP algorithm to decrease time and memory. Use for large inputs (a few hundred sequences).",
    )
    parser_muscle.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        default=None,
        help=(
            "Path to save an 'aligned FASTA' (.afa) file with the results, e.g. path/to/directory/results.afa."
            "Default: 'None' -> Standard out in Clustal format."
        ),
    )
    parser_muscle.add_argument(
        "-fa",
        "--fasta",
        type=str,
        required=False,
        dest="fasta_deprecated",
        help="DEPRECATED - use positional argument instead. Path to fasta file containing the sequences to be aligned.",
    )

    ## gget blast subparser
    blast_desc = "BLAST a nucleotide or amino acid sequence against any BLAST database."
    parser_blast = parent_subparsers.add_parser(
        "blast",
        parents=[parent],
        description=blast_desc,
        help=blast_desc,
        add_help=True,
    )
    # blast parser arguments
    parser_blast.add_argument(
        "sequence",
        type=str,
        nargs="?",
        default=None,
        help="Sequence (str) or path to fasta file.",
    )
    parser_blast.add_argument(
        "-p",
        "--program",
        choices=["blastn", "blastp", "blastx", "tblastn", "tblastx"],
        default="default",
        type=str,
        required=False,
        help=(
            "'blastn', 'blastp', 'blastx', 'tblastn', or 'tblastx'. "
            "Default: 'blastn' for nucleotide sequences; 'blastp' for amino acid sequences."
        ),
    )
    parser_blast.add_argument(
        "-db",
        "--database",
        choices=[
            "nt",
            "nr",
            "refseq_rna",
            "refseq_protein",
            "swissprot",
            "pdbaa",
            "pdbnt",
        ],
        default="default",
        type=str,
        required=False,
        help=(
            "'nt', 'nr', 'refseq_rna', 'refseq_protein', 'swissprot', 'pdbaa', or 'pdbnt'. "
            "Default: 'nt' for nucleotide sequences; 'nr' for amino acid sequences. "
            "More info on BLAST databases: https://ncbi.github.io/blast-cloud/blastdb/available-blastdbs.html"
        ),
    )
    parser_blast.add_argument(
        "-l",
        "--limit",
        type=int,
        default=50,
        required=False,
        help="int or None. Limits number of hits to return. Default 50.",
    )
    parser_blast.add_argument(
        "-e",
        "--expect",
        type=float,
        default=10.0,
        required=False,
        help="float or None. An expect value cutoff. Default 10.0.",
    )
    parser_blast.add_argument(
        "-lcf",
        "--low_comp_filt",
        default=False,
        action="store_true",
        required=False,
        help="Turn on low complexity filter. Default off.",
    )
    parser_blast.add_argument(
        "-mbo",
        "--megablast_off",
        default=True,
        action="store_false",
        required=False,
        help="Turn off MegaBLAST algorithm. Default on (blastn only).",
    )
    parser_blast.add_argument(
        "-q",
        "--quiet",
        default=True,
        action="store_false",
        required=False,
        help="Do not print progress information.",
    )
    parser_blast.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_blast.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the csv file the results will be saved in, e.g. path/to/directory/results.csv.\n"
            "Default: Standard out."
        ),
    )
    parser_blast.add_argument(
        "-seq",
        "--sequence",
        type=str,
        required=False,
        dest="seq_deprecated",
        help="DEPRECATED - use positional argument instead. Sequence (str) or path to fasta file.",
    )
    parser_blast.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ## gget blat subparser
    blat_desc = (
        "BLAT a nucleotide or amino acid sequence against any BLAT UCSC assembly."
    )
    parser_blat = parent_subparsers.add_parser(
        "blat", parents=[parent], description=blat_desc, help=blat_desc, add_help=True
    )
    # blat parser arguments
    parser_blat.add_argument(
        "sequence",
        type=str,
        nargs="?",
        default=None,
        help="Sequence (str) or path to fasta file.",
    )
    parser_blat.add_argument(
        "-st",
        "--seqtype",
        choices=["DNA", "protein", "translated%20RNA", "translated%20DNA"],
        default="default",
        type=str,
        required=False,
        help=(
            "'DNA', 'protein', 'translated%%20RNA', or 'translated%%20DNA'. "
            "Default: 'DNA' for nucleotide sequences; 'protein' for amino acid sequences."
        ),
    )
    parser_blat.add_argument(
        "-a",
        "--assembly",
        default="human",
        type=str,
        required=False,
        help=(
            "'human' (assembly hg38) (default), 'mouse' (assembly mm39), "
            "or any of the species assemblies available at https://genome.ucsc.edu/cgi-bin/hgBlat "
            "(use short assembly name as listed after the '/'). "
        ),
    )
    parser_blat.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_blat.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the csv file the results will be saved in, e.g. path/to/directory/results.csv."
            "Default: Standard out."
        ),
    )
    parser_blat.add_argument(
        "-seq",
        "--sequence",
        type=str,
        required=False,
        dest="seq_deprecated",
        help="DEPRECATED - use positional argument instead. Sequence (str) or path to fasta file.",
    )
    parser_blat.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ## gget enrichr subparser
    enrichr_desc = "Perform an enrichment analysis on a list of genes using Enrichr."
    parser_enrichr = parent_subparsers.add_parser(
        "enrichr",
        parents=[parent],
        description=enrichr_desc,
        help=enrichr_desc,
        add_help=True,
    )
    # enrichr parser arguments
    parser_enrichr.add_argument(
        "genes",
        type=str,
        nargs="*",
        default=None,
        help="List of gene symbols or Ensembl gene IDs to perform enrichment analysis on.",
    )
    parser_enrichr.add_argument(
        "-db",
        "--database",
        type=str,
        required=True,
        help=(
            "'pathway', 'transcription', 'ontology', 'diseases_drugs', 'celltypes', 'kinase_interactions'"
            "or any database listed at: https://maayanlab.cloud/Enrichr/#libraries"
        ),
    )
    parser_enrichr.add_argument(
        "-e",
        "--ensembl",
        default=False,
        action="store_true",
        required=False,
        help="Add this flag if genes are given as Ensembl gene IDs.",
    )
    parser_enrichr.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_enrichr.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the csv file the results will be saved in, e.g. path/to/directory/results.csv."
            "Default: Standard out."
        ),
    )
    parser_enrichr.add_argument(
        "-g",
        "--genes",
        type=str,
        nargs="+",
        required=False,
        dest="genes_deprecated",
        help="DEPRECATED - use positional argument instead. List of gene symbols or Ensembl gene IDs to perform enrichment analysis on.",
    )
    parser_enrichr.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ## gget archs4 subparser
    archs4_desc = "Find the most correlated genes or the tissue expression atlas of a gene using data from the human and mouse RNA-seq database ARCHS4 (https://maayanlab.cloud/archs4/)."
    parser_archs4 = parent_subparsers.add_parser(
        "archs4",
        parents=[parent],
        description=archs4_desc,
        help=archs4_desc,
        add_help=True,
    )
    # archs4 parser arguments
    parser_archs4.add_argument(
        "gene",
        type=str,
        nargs="?",
        default=None,
        help="Gene symbol or Ensembl gene ID of gene of interest (str), e.g. 'STAT4'.",
    )
    parser_archs4.add_argument(
        "-e",
        "--ensembl",
        default=False,
        action="store_true",
        required=False,
        help="Add this flag if gene is given as an Ensembl gene ID.",
    )
    parser_archs4.add_argument(
        "-w",
        "--which",
        choices=[
            "correlation",
            "tissue",
        ],
        default="correlation",
        type=str,
        required=False,
        help=(
            """
            'correlation' (default) or 'tissue'.
            - 'correlation' returns a gene correlation table that contains the
            100 most correlated genes to the gene of interest. The Pearson
            correlation is calculated over all samples and tissues in ARCHS4.
            - 'tissue' returns a tissue expression atlas calculated from
            human or mouse samples (as defined by 'species') in ARCHS4.
            """
        ),
    )
    parser_archs4.add_argument(
        "-gc",
        "--gene_count",
        default=100,
        type=int,
        required=False,
        help=(
            """
            Number of correlated genes to return (default: 100).
            (Only for gene correlation.)
            """
        ),
    )
    parser_archs4.add_argument(
        "-s",
        "--species",
        choices=[
            "human",
            "mouse",
        ],
        default="human",
        type=str,
        required=False,
        help="'human' (default) or 'mouse'. (Only for tissue expression atlas.)",
    )
    parser_archs4.add_argument(
        "-csv",
        "--csv",
        default=True,
        action="store_false",
        required=False,
        help="Returns results in csv format instead of json.",
    )
    parser_archs4.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        help=(
            "Path to the csv file the results will be saved in, e.g. path/to/directory/results.csv.\n"
            "Default: Standard out."
        ),
    )
    parser_archs4.add_argument(
        "-g",
        "--gene",
        type=str,
        required=False,
        dest="gene_deprecated",
        help="DEPRECATED - use positional argument instead. Gene symbol or Ensembl gene ID of gene of interest (str), e.g. 'STAT4'.",
    )
    parser_archs4.add_argument(
        "-j",
        "--json",
        default=False,
        action="store_true",
        required=False,
        help="DEPRECATED - json is now the default output format (convert to csv using flag [--csv]).",
    )

    ### Define return values
    args = parent_parser.parse_args()

    # Help return
    if args.help:
        # Retrieve all subparsers from the parent parser
        subparsers_actions = [
            action
            for action in parent_parser._actions
            if isinstance(action, argparse._SubParsersAction)
        ]
        for subparsers_action in subparsers_actions:
            # Get all subparsers and print help
            for choice, subparser in subparsers_action.choices.items():
                print("Subparser '{}'".format(choice))
                print(subparser.format_help())
        sys.exit(1)

    # Version return
    if args.version:
        print(f"gget version: {__version__}")
        sys.exit(1)

    # Show help when no arguments are given
    if len(sys.argv) == 1:
        parent_parser.print_help(sys.stderr)
        sys.exit(1)

    # Show  module specific help if only module but no further arguments are given
    command_to_parser = {
        "muscle": parser_muscle,
        "ref": parser_ref,
        "search": parser_gget,
        "seq": parser_seq,
        "info": parser_info,
        "blast": parser_blast,
        "blat": parser_blat,
        "enrichr": parser_enrichr,
        "archs4": parser_archs4,
    }

    if len(sys.argv) == 2:
        if sys.argv[1] in command_to_parser:
            command_to_parser[sys.argv[1]].print_help(sys.stderr)
        else:
            parent_parser.print_help(sys.stderr)
        sys.exit(1)

    ## blat return
    if args.command == "blat":
        # Handle deprecated flags for backwards compatibility
        if args.seq_deprecated and args.sequence:
            logging.warning(
                "The [-seq][--sequence] argument is deprecated, using positional argument [sequence] instead."
            )
        if args.seq_deprecated and not args.sequence:
            args.sequence = args.seq_deprecated
            logging.warning(
                "The [-seq][--sequence] argument is deprecated, please use positional argument [sequence] instead."
            )
        if not args.seq_deprecated and not args.sequence:
            parser_blat.error("the following arguments are required: sequence")

        # Run gget blast function
        blat_results = blat(
            sequence=args.sequence,
            seqtype=args.seqtype,
            assembly=args.assembly,
            json=args.csv,
        )

        # Check if the function returned something
        if not isinstance(blat_results, type(None)):
            # Save blat results if args.out specified
            if args.out and not args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save to csv
                blat_results.to_csv(args.out, index=False)

            if args.out and args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save json
                with open(args.out, "w", encoding="utf-8") as f:
                    json.dump(blat_results, f, ensure_ascii=False, indent=4)

            # Print results if no directory specified
            if not args.out and not args.csv:
                blat_results.to_csv(sys.stdout, index=False)
            if not args.out and args.csv:
                print(json.dumps(blat_results, ensure_ascii=False, indent=4))

    ## blast return
    if args.command == "blast":
        # Handle deprecated flags for backwards compatibility
        if args.seq_deprecated and args.sequence:
            logging.warning(
                "The [-seq][--sequence] argument is deprecated, using positional argument [sequence] instead."
            )
        if args.seq_deprecated and not args.sequence:
            args.sequence = args.seq_deprecated
            logging.warning(
                "The [-seq][--sequence] argument is deprecated, please use positional argument [sequence] instead."
            )
        if not args.seq_deprecated and not args.sequence:
            parser_blast.error("the following arguments are required: sequence")

        # Run gget blast function
        blast_results = blast(
            sequence=args.sequence,
            program=args.program,
            database=args.database,
            limit=args.limit,
            expect=args.expect,
            low_comp_filt=args.low_comp_filt,
            megablast=args.megablast_off,
            verbose=args.quiet,
            json=args.csv,
        )

        # Check if the function returned something
        if not isinstance(blast_results, type(None)):
            # Save blast results if args.out specified
            if args.out and not args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save to csv
                blast_results.to_csv(args.out, index=False)

            if args.out and args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save json
                with open(args.out, "w", encoding="utf-8") as f:
                    json.dump(blast_results, f, ensure_ascii=False, indent=4)

            # Print results if no directory specified
            if not args.out and not args.csv:
                blast_results.to_csv(sys.stdout, index=False)
            if not args.out and args.csv:
                print(json.dumps(blast_results, ensure_ascii=False, indent=4))

    ## archs4 return
    if args.command == "archs4":
        # Handle deprecated flags for backwards compatibility
        if args.gene_deprecated and args.gene:
            logging.warning(
                "The [-g][--gene] argument is deprecated, using positional argument [gene] instead."
            )
        if args.gene_deprecated and not args.gene:
            args.gene = args.gene_deprecated
            logging.warning(
                "The [-g][--gene] argument is deprecated, please use positional argument [gene] instead."
            )
        if not args.gene_deprecated and not args.gene:
            parser_archs4.error("the following arguments are required: gene")

        # Run gget archs4 function
        archs4_results = archs4(
            gene=args.gene,
            ensembl=args.ensembl,
            which=args.which,
            gene_count=args.gene_count,
            species=args.species,
            json=args.csv,
        )

        # Check if the function returned something
        if not isinstance(archs4_results, type(None)):
            # Save archs4 results if args.out specified
            if args.out and not args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save to csv
                archs4_results.to_csv(args.out, index=False)

            if args.out and args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save json
                with open(args.out, "w", encoding="utf-8") as f:
                    json.dump(archs4_results, f, ensure_ascii=False, indent=4)

            # Print results if no directory specified
            if not args.out and not args.csv:
                archs4_results.to_csv(sys.stdout, index=False)
            if not args.out and args.csv:
                print(json.dumps(archs4_results, ensure_ascii=False, indent=4))

    ## muscle return
    if args.command == "muscle":
        # Handle deprecated flags for backwards compatibility
        if args.fasta_deprecated and args.fasta:
            logging.warning(
                "The [-fa][--fasta] argument is deprecated, using positional argument [fasta] instead."
            )
        if args.fasta_deprecated and not args.fasta:
            args.fasta = args.fasta_deprecated
            logging.warning(
                "The [-fa][--fasta] argument is deprecated, please use positional argument [fasta] instead."
            )
        if not args.fasta_deprecated and not args.fasta:
            parser_muscle.error("the following arguments are required: fasta")

        muscle(fasta=args.fasta, super5=args.super5, out=args.out)

    ## ref return
    if args.command == "ref":
        # Return all available species
        if args.list_species:
            species_list = ref(
                species=None, release=args.release, list_species=args.list_species
            )
            for species in species_list:
                print(species)

        # Handle deprecated flags for backwards compatibility
        if args.species_deprecated and args.species:
            logging.warning(
                "The [-s][--species] argument is deprecated, using positional argument [species] instead."
            )
        if args.species_deprecated and not args.species:
            args.species = args.species_deprecated
            logging.warning(
                "The [-s][--species] argument is deprecated, please use positional argument [species] instead."
            )

        # Raise error if neither species nor list flag passed
        if args.species is None and args.list_species is False:
            parser_ref.error(
                "the following arguments are required: species \n"
                "'gget ref --list_species' -> lists out all available species. \n"
                "Combine with '-r [int]' to define a specific Ensembl release (default: latest release). "
            )

        ## Clean up 'which' entry if passed
        # Split by comma
        which_clean = args.which.split(",")

        if args.species:

            # Query Ensembl for requested FTPs using function ref
            ref_results = ref(
                species=args.species,
                which=which_clean,
                release=args.release,
                ftp=args.ftp,
            )

            # Print or save list of URLs (ftp=True)
            if args.ftp:
                # Save in specified directory if -o specified
                if args.out:
                    directory = "/".join(args.out.split("/")[:-1])
                    if directory != "":
                        os.makedirs(directory, exist_ok=True)
                    with open(args.out, "w", encoding="utf-8") as f:
                        json.dump(ref_results, f, ensure_ascii=False, indent=4)

                    if args.download == True:
                        # Download list of URLs
                        for link in ref_results:
                            # command = "wget " + link
                            command = "curl -O " + link
                            os.system(command)
                #                     else:
                #                         logging.info(
                #                             "To download the FTPs to the current directory, add flag [-d]."
                #                         )

                # Print results if no directory specified
                else:
                    # Print results
                    for ref_res in ref_results:
                        print(ref_res)

                    if args.download == True:
                        # Download list of URLs
                        for link in ref_results:
                            # command = "wget " + link
                            command = "curl -O " + link
                            os.system(command)
            #                     else:
            #                         logging.info(
            #                             "To download the FTPs to the current directory, add flag [-d]."
            #                         )

            # Print or save json file (ftp=False)
            else:
                # Save in specified directory if -o specified
                if args.out:
                    directory = "/".join(args.out.split("/")[:-1])
                    if directory != "":
                        os.makedirs(directory, exist_ok=True)
                    with open(args.out, "w", encoding="utf-8") as f:
                        json.dump(ref_results, f, ensure_ascii=False, indent=4)

                    if args.download == True:
                        # Download the URLs from the dictionary
                        for link in ref_results:
                            for sp in ref_results:
                                for ftp_type in ref_results[sp]:
                                    link = ref_results[sp][ftp_type]["ftp"]
                                    #                                     command = "wget " + link
                                    command = "curl -O " + link
                                    os.system(command)
                #                     else:
                #                         logging.info(
                #                             "To download the FTPs to the current directory, add flag [-d]."
                #                         )

                # Print results if no directory specified
                else:
                    print(json.dumps(ref_results, ensure_ascii=False, indent=4))

                    if args.download == True:
                        # Download the URLs from the dictionary
                        for link in ref_results:
                            for sp in ref_results:
                                for ftp_type in ref_results[sp]:
                                    link = ref_results[sp][ftp_type]["ftp"]
                                    #                                     command = "wget " + link
                                    command = "curl -O " + link
                                    os.system(command)
    #                     else:
    #                         logging.info(
    #                             "To download the FTPs to the current directory, add flag [-d]."
    #                         )

    ## search return
    if args.command == "search":
        # Handle deprecated flags for backwards compatibility
        if args.sw_deprecated and args.searchwords:
            logging.warning(
                "The [-sw][--searchwords] argument is deprecated, using positional argument [searchwords] instead."
            )
        if args.sw_deprecated and not args.searchwords:
            args.searchwords = args.sw_deprecated
            logging.warning(
                "The [-sw][--searchwords] argument is deprecated, please use positional argument [searchwords] instead."
            )
        if not args.sw_deprecated and not args.searchwords:
            parser_gget.error("the following arguments are required: searchwords")

        ## Clean up args.searchwords
        sw_clean = []
        # Split by comma (spaces are automatically split by nargs:"+")
        for sw in args.searchwords:
            sw_clean.append(sw.split(","))
        # Flatten which_clean
        sw_clean_final = [item for sublist in sw_clean for item in sublist]
        # Remove empty strings resulting from split
        while "" in sw_clean_final:
            sw_clean_final.remove("")

        # Query Ensembl for genes based on species and searchwords using function search
        gget_results = search(
            sw_clean_final,
            args.species,
            id_type=args.id_type,
            seqtype=args.seqtype,
            andor=args.andor,
            limit=args.limit,
            json=args.csv,
        )

        # Save search results if args.out specified
        if args.out and not args.csv:
            # Create saving directory
            directory = "/".join(args.out.split("/")[:-1])
            if directory != "":
                os.makedirs(directory, exist_ok=True)
            # Save to csv
            gget_results.to_csv(args.out, index=False)

        if args.out and args.csv:
            # Create saving directory
            directory = "/".join(args.out.split("/")[:-1])
            if directory != "":
                os.makedirs(directory, exist_ok=True)
            # Save json
            with open(args.out, "w", encoding="utf-8") as f:
                json.dump(gget_results, f, ensure_ascii=False, indent=4)

        # Print results if no directory specified
        if not args.out and not args.csv:
            gget_results.to_csv(sys.stdout, index=False)
        if not args.out and args.csv:
            print(json.dumps(gget_results, ensure_ascii=False, indent=4))

    ## enrichr return
    if args.command == "enrichr":
        # Handle deprecated flags for backwards compatibility
        if args.genes_deprecated and args.genes:
            logging.warning(
                "The [-g][--genes] argument is deprecated, using positional argument [genes] instead."
            )
        if args.genes_deprecated and not args.genes:
            args.genes = args.genes_deprecated
            logging.warning(
                "The [-g][--genes] argument is deprecated, please use positional argument [genes] instead."
            )
        if not args.genes_deprecated and not args.genes:
            parser_enrichr.error("the following arguments are required: genes")

        ## Clean up args.genes
        genes_clean = []
        # Split by comma (spaces are automatically split by nargs:"+")
        for gene in args.genes:
            genes_clean.append(gene.split(","))
        # Flatten genes_clean
        genes_clean_final = [item for sublist in genes_clean for item in sublist]
        # Remove empty strings resulting from split
        while "" in genes_clean_final:
            genes_clean_final.remove("")

        # Submit Enrichr query
        enrichr_results = enrichr(
            genes=genes_clean_final,
            database=args.database,
            ensembl=args.ensembl,
            json=args.csv,
        )

        # Check if the function returned something
        if not isinstance(enrichr_results, type(None)):
            # Save enrichr results if args.out specified
            if args.out and not args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save to csv
                enrichr_results.to_csv(args.out, index=False)

            if args.out and args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save json
                with open(args.out, "w", encoding="utf-8") as f:
                    json.dump(enrichr_results, f, ensure_ascii=False, indent=4)

            # Print results if no directory specified
            if not args.out and not args.csv:
                enrichr_results.to_csv(sys.stdout, index=False)
            if not args.out and args.csv:
                print(json.dumps(enrichr_results, ensure_ascii=False, indent=4))

    ## info return
    if args.command == "info":
        # Handle deprecated flags for backwards compatibility
        if args.id_deprecated and args.ens_ids:
            logging.warning(
                "The [-id][--ens_ids] argument is deprecated, using positional argument [ens_ids] instead."
            )
        if args.id_deprecated and not args.ens_ids:
            args.ens_ids = args.id_deprecated
            logging.warning(
                "The [-id][--genes] argument is deprecated, please use positional argument [ens_ids] instead."
            )
        if not args.id_deprecated and not args.ens_ids:
            parser_info.error("the following arguments are required: ens_ids")

        ## Clean up args.ens_ids
        ids_clean = []
        # Split by comma (spaces are automatically split by nargs:"+")
        for id_ in args.ens_ids:
            ids_clean.append(id_.split(","))
        # Flatten which_clean
        ids_clean_final = [item for sublist in ids_clean for item in sublist]
        # Remove empty strings resulting from split
        while "" in ids_clean_final:
            ids_clean_final.remove("")

        # Look up requested Ensembl IDs
        info_results = info(
            ids_clean_final, expand=args.expand, json=args.csv, verbose=args.quiet
        )

        # Check if the function returned something
        if not isinstance(info_results, type(None)):
            # Save info results if args.out specified
            if args.out and not args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save to csv
                info_results.to_csv(args.out, index=False)

            if args.out and args.csv:
                # Create saving directory
                directory = "/".join(args.out.split("/")[:-1])
                if directory != "":
                    os.makedirs(directory, exist_ok=True)
                # Save json
                with open(args.out, "w", encoding="utf-8") as f:
                    json.dump(info_results, f, ensure_ascii=False, indent=4)

            # Print results if no directory specified
            if not args.out and not args.csv:
                info_results.to_csv(sys.stdout, index=False)
            if not args.out and args.csv:
                print(json.dumps(info_results, ensure_ascii=False, indent=4))

    ## seq return
    if args.command == "seq":
        # Handle deprecated flags for backwards compatibility
        if args.id_deprecated and args.ens_ids:
            logging.warning(
                "The [-id][--ens_ids] argument is deprecated, using positional argument [ens_ids] instead."
            )
        if args.id_deprecated and not args.ens_ids:
            args.ens_ids = args.id_deprecated
            logging.warning(
                "The [-id][--ens_ids] argument is deprecated, please use positional argument [ens_ids] instead."
            )
        if not args.id_deprecated and not args.ens_ids:
            parser_seq.error("the following arguments are required: ens_ids")

        ## Clean up args.ens_ids
        ids_clean = []
        # Split by comma (spaces are automatically split by nargs:"+")
        for id_ in args.ens_ids:
            ids_clean.append(id_.split(","))
        # Flatten which_clean
        ids_clean_final = [item for sublist in ids_clean for item in sublist]
        # Remove empty strings resulting from split
        while "" in ids_clean_final:
            ids_clean_final.remove("")

        # Look up requested Ensembl IDs
        seq_results = seq(
            ids_clean_final,
            translate=args.translate,
            seqtype=args.seqtype,
            isoforms=args.isoforms,
            transcribe=args.transcribe,
        )

        # Save in specified directory if -o specified
        if args.out and seq_results != None:
            directory = "/".join(args.out.split("/")[:-1])
            if directory != "":
                os.makedirs(directory, exist_ok=True)
            file = open(args.out, "w")
            for element in seq_results:
                file.write(element + "\n")
            file.close()

        # Print results if no directory specified
        else:
            if seq_results != None:
                for seq_res in seq_results:
                    print(seq_res)
