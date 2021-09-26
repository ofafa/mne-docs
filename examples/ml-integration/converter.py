"""
cli for converting TextGrid file to event array
"""
import pickle
import sys, re, io
import click
import pandas as pd
import loguru

logger = loguru.logger

def inputtextlines(filename):
    handle = open(filename,'r')
    linelist = handle.readlines()
    handle.close()
    return linelist

def converttextgrid2csv(textgridlines, textgridname):

    csvtext = "TierType,TierName,tLabel,Start,End,Duration\n"

    newtier = False
    for line in textgridlines[9:]:
        line = re.sub('\n','',line)
        line = re.sub('^ *','',line)
        linepair = line.split(' = ')
        if len(linepair) == 2:
            if linepair[0] == 'class':
                classname = linepair[1]
            if linepair[0] == 'name':
                tiername = linepair[1]
            if linepair[0] == 'xmin':
                xmin = linepair[1]
            if linepair[0] == 'xmax':
                xmax = linepair[1]
            if linepair[0] == 'text':
                text = linepair[1]
                diff = str(float(xmax)-float(xmin))
                csvtext += ",".join([classname, tiername, text, xmin, xmax, diff]) + '\n'
    return csvtext


@click.command()
@click.option("--textgrid_file", help="path to the TextGrid file")
@click.option("--sample_rate", help="the sample rate of the input file", type=int)
@click.option("--export_path", help="the output path for the array", default="output")
@click.option(
    "--output_type",
    help="choose the output format",
    default="csv",
    type=click.Choice(['csv', 'pickle', 'json']))
def export_dataset(
    textgrid_file: str,
    sample_rate: int,
    output_type: str,
    export_path: str):
    """
    parse the textgrid file, convert to array with sample rate
    """
    textgrid = inputtextlines(textgrid_file)
    text_csv = converttextgrid2csv(textgrid, textgrid_file)
    text_df = pd.read_csv(io.StringIO(text_csv))
    text_df["Start"] = text_df["Start"].apply(lambda x: round(x*sample_rate))
    text_df["End"] = text_df["End"].apply(lambda x: round(x*sample_rate))
    # todo: limit output only to the timestamp and event label
    if output_type.lower() == "csv":
        text_df.to_csv(export_path + '.csv')
    if output_type.lower() == "json":
        text_df.to_json(export_path + '.json', orient="records", indent=2)
    if output_type.lower() == "pickle":
        text_df.to_pickle(output_path + '.pickle')
    logger.info("convert file finished")


if __name__ == "__main__":
    export_dataset()
