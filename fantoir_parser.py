from typing import Optional
import logging
from tqdm import tqdm

from utils import (
    get_data,
    write_data,
    DEPARTEMENTS_REFERENCE,
    COMMUNES_REFERENCE,
    VOIES_REFERENCE,
)


def parse_fantoir(
    input_file: str,
    limit: Optional[int] = None,
    verbose: bool = True,
    parse_communes: bool = True,
    parse_voies: bool = True,
    parse_departements: bool = True,
):
    logging.info(f"Opening {input_file}")

    counter = 0
    departements = []
    communes = []
    voies = []

    with open(input_file, "r") as file:
        if verbose:
            if limit:
                file_ = tqdm(file, total=limit)
            else:
                file_ = tqdm(file)
        else:
            file_ = file

        for line in file_:
            if limit and (counter == limit):
                break
            if counter > 0:
                if line[4] == " ":
                    if parse_departements:
                        departements.append(
                            get_data(
                                line,
                                include_keys=False,
                                reference=DEPARTEMENTS_REFERENCE,
                            )
                        )
                elif line[6] == " ":
                    if parse_communes:
                        communes.append(
                            get_data(
                                line,
                                include_keys=False,
                                reference=COMMUNES_REFERENCE,
                            )
                        )
                elif line[14] == " ":
                    if parse_voies:
                        voies.append(
                            get_data(
                                line,
                                include_keys=False,
                                reference=VOIES_REFERENCE,
                            )
                        )

            counter += 1

    return {
        "departements": departements,
        "communes": communes,
        "voies": voies,
    }


if __name__ == "__main__":
    from argparse import ArgumentParser

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        help="Name of the FANTOIR file",
        default="FANTOIR1022",
    )

    argument_parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        help="Name of the output files",
        default="data/parsed_{object_type}.csv",
    )

    argument_parser.add_argument(
        "--departements",
        action="store_true",
        help="Parse départements",
    )
    argument_parser.add_argument(
        "--communes",
        action="store_true",
        help="Parse communes",
    )
    argument_parser.add_argument(
        "--voies",
        action="store_true",
        help="Parse voies",
    )
    argument_parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=None,
        help="Number of objects to parse",
    )

    argument_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbosity",
    )

    arguments = argument_parser.parse_args()

    input_file = arguments.input_file
    output_file = arguments.output_file
    parse_departements = arguments.departements
    parse_communes = arguments.communes
    parse_voies = arguments.voies
    limit = arguments.limit

    verbose = arguments.verbose

    if verbose:
        logging.basicConfig(level=logging.INFO)

    data = parse_fantoir(
        input_file=input_file,
        limit=limit,
        verbose=verbose,
        parse_departements=parse_departements,
        parse_communes=parse_communes,
        parse_voies=parse_voies,
    )
    if parse_departements:
        departement_name = output_file.format(object_type="departements")
        logging.info(f"Writing departements data into {departement_name}")
        write_data(
            path=departement_name,
            data=data["departements"],
            keys=[f["short_name"] for f in DEPARTEMENTS_REFERENCE],
        )
    if parse_communes:
        commune_name = output_file.format(object_type="communes")
        logging.info(f"Writing communes data into {commune_name}")
        write_data(
            path=commune_name,
            data=data["communes"],
            keys=[f["short_name"] for f in COMMUNES_REFERENCE],
        )

    if parse_voies:
        voie_name = output_file.format(object_type="voies")
        logging.info(f"Writing voies data into {voie_name}")
        write_data(
            path=voie_name,
            data=data["voies"],
            keys=[f["short_name"] for f in VOIES_REFERENCE],
        )
