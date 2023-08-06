#!/usr/bin/env conda run -n base python

import json
import requests
import os
from xmlrpc.client import boolean
import mistletoe as md
from mistletoe.ast_renderer import ASTRenderer
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.logging import RichHandler
import logging
import argparse
from rootmd import RootHtmlRenderer
from rootmd import RootMdRenderer
from rootmd import Md2MacroRenderer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# watchdog observer
observer = Observer()


# setup our logger
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


"""
Entry point for RootMd
"""
parser = argparse.ArgumentParser(description='Convert Markdown with inline c++ code to ROOT output.', prog="rootmd")
parser.add_argument(
    'input', nargs="?", help='input Markdown file to execute and convert', default=""
)
parser.add_argument(
    '--output', help='output filename default <input>.<ext> where <ext> is determined by the chosen format, default html, output can include {input} to allow substitution of input filename, or {path} for full path, or {basepath} for path to input file, or {ext} for default output extension for format specified. TODO', default=""
)
parser.add_argument( 
    '--format', help='output format', default="html", 
    choices=["html", "md", "obsidian", "json", "terminal", "macro"]
)
parser.add_argument(
    '--embed', help='embed images as base 64', default=False, action="store_true"
)
parser.add_argument(
    '--asset-dir', 
    help='specify asset output directory, paths are NOTE re-written to support unless using obsidian format', default=""
)
parser.add_argument(
    '--asset-prefix', 
    help='specify prefix to add to attachments when re-writing (obsidian mode)', default=""
)
parser.add_argument( 
    '--watch', help='watch a file or directory for changes')
parser.add_argument( 
    '--run', 
    help='command to run after processing a file. The filename can be substituted into the command string with {{file}}. Example: --run="echo {{file}}"')
parser.add_argument( 
    '--clean', 
    help='clean artifacts, caution - should only use with embed or asset copy to <asset-dir>', action='store_true', default=False)
parser.add_argument( 
    '--no-exec', 
    help='Do not execute any code blocks, just process file (useful for viewing and testing conversion)', action='store_true', default=False)

parser.add_argument( 
    '--html-template', 
    help='Template HTML file should include {js}, {css}, {content} ... TODO', default="")
parser.add_argument( 
    '--css', 
    help='CSS used for the HTML output, overrides default ... TODO', default="")

parser.add_argument( 
    '--share', 
    help='Upload to sharing server, make sure ROOTMD_TOKEN is set', default=False, action='store_true')

parser.add_argument( '-log',
                     '--loglevel',
                     default='warning',
                     help='Provide logging level. Example --loglevel debug, default=warning' )

args = parser.parse_args()

# 

if "input" not in args and "watch" not in args :
    log.error( "Must provide one of [\"[input]\" or \"--watch\" to specify input files ]" )
    exit()

EXTENSIONS = {
    "html"     : ".html",
    "md"       : ".md",
    "obsidian" : ".md",
    "json"     : ".json",
    "terminal" : ".md",
    "macro"    : ".C"
}


console = Console()

log.info( 'Logging now setup with level %s ' % args.loglevel.upper() )
log.setLevel( args.loglevel.upper() )


ASSET_PREFIX=args.asset_prefix
EMBED = args.embed
ASSET_DIR = args.asset_dir
if args.output == "" and args.input != "":
    args.output = args.input  + EXTENSIONS[args.format] # ext will be added later

# if VERBOSITY <= 1:
#     inspect( args )

basename = os.path.basename( args.output )

# handle obsidian's way of removing the attachment/ (or whatever dir) from paths
if args.format == "obsidian":
    # ASSET_PREFIX = os.path.splitext(basename)[0]
    if args.asset_prefix == "": # default for obsidian
        ASSET_PREFIX = "attachments"
    else :
        ASSET_PREFIX = args.asset_prefix
        
    ASSET_DIR = os.path.join( ASSET_DIR, ASSET_PREFIX )
    if not os.path.isdir( ASSET_DIR ):
        log.info( "Making asset directory: %s" % ASSET_DIR )
        os.mkdir( ASSET_DIR )

#input working dir
log.info( "I am %s" % __file__ )
inwdir = os.path.dirname(os.path.abspath(args.input))
log.info( "input working directory: %s" % inwdir )
if ASSET_DIR == "" and input != "":
    ASSET_DIR = inwdir


class RootMd :
    def __init__(self, *args, **kwargs) -> None:
        log.debug("args:")
        # inspect( args[0] )
        self.args = args[0]
        log.debug( self.args.input )
        self.title = ""
        self.last_run_input = ""
        self.last_run_time = 0
        

    def run(self, input):
        delta_time = time.time() - self.last_run_time
        self.args.input = input
        # log.info( "delta_time = %d" % delta_time )
        if self.args.input == self.last_run_input and delta_time < 1 :
            return
        self.last_run_input = self.args.input
        artifacts = []
        
        if not os.path.exists(self.args.input) :
            log.error("File %s does not exist" % ( self.args.input ) )
            return
        inwdir = os.path.dirname(os.path.abspath(self.args.input))
        log.info( "input working directory: %s" % inwdir )
        ASSET_DIR = self.args.asset_dir
        if ASSET_DIR == "":
            ASSET_DIR = inwdir
        
        log.info( "Processing %s to %s output format" % (self.args.input, self.args.format ) )
        self.title = args.input
        theRenderer = RootHtmlRenderer()
        theRenderer.set( embed=EMBED, asset_dir=ASSET_DIR, asset_prefix=ASSET_PREFIX )
        
        if args.format == "md" or args.format == "obsidian" or args.format == "terminal":
            theRenderer = RootMdRenderer()
            theRenderer.set( embed=EMBED, asset_dir=ASSET_DIR, asset_prefix=ASSET_PREFIX )
        if args.format == "ast" :
            theRenderer = ASTRenderer()
        if args.format == "macro" :
            theRenderer = Md2MacroRenderer()

        with open( args.input , 'r') as fin:
            html = theRenderer.render(md.Document(fin))
            artifacts = theRenderer.artifacts
        if args.format == "terminal" :
            console.print( Markdown(html) )
            return

        output = args.output
        # if "" == output :
        #     output = args.input + "." + args.format
        if output == "":
            output = input  + EXTENSIONS[args.format] # ext will be added later

        log.info( "Writing output to %s" % output )
        with open( output , "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html)
        

        token = os.environ.get( "ROOTMD_TOKEN", "" )
        if "share" in args and args.share and token != "":
            files = { output : html }
            for fn in artifacts:
                try :
                    with open( fn, 'rb' ) as f:
                        files[ fn ] = f.read()
                except Exception as e:
                    log.error( e )

            log.info( "SHARE:" )
            for fi in files :
                log.info( "file_name: %s" % fi )
            res = requests.post(
                "https://rootmd.jdbburg.com/upload",
                data={ "token": token},
                files = files )
            log.info( res.json() )
            if res.status_code == 200 and res.json()["status"] == True and len(res.json()["data"]) >= 1:
                url = res.json()["data"][0]["link"]
                # "https://rootmd.jdbburg.com/bfbf11835023423dd316586acb9fbbb3/confidenceintervals.md.html"
                log.info( "Uploaded to:" )
                print( url )
        
        self.last_run_time = time.time()


rootmd = RootMd(args)


class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'modified' :
            # inspect( event )
            # Event is modified, you can process it now
            log.info("Watchdog received modified event - % s" % event.src_path)
            rootmd.run(input=event.src_path)


if args.watch :
    event_handler = Handler()
    observer.schedule(event_handler, args.watch, recursive = True)
    log.info( 'Watching "%s" for changes' % args.watch )
    observer.start()
    try:
        while True:
            time.sleep(5)
    except:
        observer.stop()
        # print("Observer Stopped")

    observer.join()
    exit()


rootmd.run(args.input)


