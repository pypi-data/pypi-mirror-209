from mistletoe.base_renderer import BaseRenderer
import base64
from shutil import copyfile
import os
import logging


from .Executor import RootExecutor

from rich.logging import RichHandler
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


class RootMdRenderer(BaseRenderer, RootExecutor):
    def __init__(self, *extras):
        super().__init__(*extras)
        RootExecutor.__init__(self, *extras)
        
        self.blockid = 0
        self.foundyamlheader = False # TODO yaml as first class citizen
        self.embed = False
        self.asset_prefix = ""
        self.asset_dir = ""
        self.artifacts = []
        
    
    def set( self, **kwargs ) :
        if "embed" in kwargs :
            self.embed = kwargs.get( "embed" )
        if "asset_dir" in kwargs :
            self.asset_dir = kwargs.get( "asset_dir" )
        if "asset_prefix" in kwargs:
            self.asset_prefix = kwargs.get( "asset_prefix" )

    def process_image_output(self, path):
        path = path.strip()
        _, ext = os.path.splitext( path )
        ext = ext.replace( ".", "" )
        template = '![{src}]({src})'

        if self.asset_dir != "" and not self.embed:
            log.info( "cp %s %s" % (path, os.path.join(self.asset_dir, path ) ) )
            try :
                copyfile( path, os.path.join(self.asset_dir, path ) )
            except Exception as e:
                log.debug( e )

        if self.embed:
            with open(path, "rb") as image_file:
                b64_encoded = base64.b64encode(image_file.read())
                template = '![{text}](data:image/{ext};charset=utf-8;base64,{data})'
                
                if "svg" == ext:
                    ext = "svg+xml"
                return template.format( ext=ext, data=b64_encoded.decode(), text=_ )
        else:
            npath = path
            if self.asset_prefix != "":
                npath = os.path.join( self.asset_prefix, os.path.basename(path) )
                log.info( "rewriting asset path: %s -> %s" % ( path, npath ) )
            return "\n" + template.format( src=npath )

    def render_block_code(self, token):
        template = """```{lang}\n{content}\n```\n"""
        yamltemplate = '---\n{content}\n---\n'

        code =token.children[0].content
        output = template.format( lang = token.language if token.language else '', content= token.children[0].content )

        if token.language == "yaml" and self.foundyamlheader == False:
            self.foundyamlheader = True
            return yamltemplate.format( content = code )

        if not token.language or token.language != "cpp":
            return output

        if "//noexec" in code:
            log.debug( "Skipping execution" )
            return output

        routput, rerr, imgs = self.run_cmd( code )

        output = template.format( lang = token.language if token.language else '', content= token.children[0].content )
        output += template.format( lang="sh", content=( ("# Block [%d] stdout \n" % self.blockid) + routput ) )

        err = template.format( lang = token.language if token.language else '', content= token.children[0].content )
        err += template.format( lang="sh", content=( ("# Block [%d] stderr \n" % self.blockid) + rerr ) )


        # output controls
        if self.optionAsBool( token.options, "out", True) == False or self.optionAsBool( token.options, "stdout", True) == False:
            output = ""
        elif "out" in token.options or "stdout" in token.options:
            stdout_filename = token.options.get("out", token.options.get( "stdout", "stdout.dat" ))
            log.info( "Writing block %d stdout to file: %s" % ( self.blockid, stdout_filename ) )
            with open( stdout_filename, "w" ) as wf:
                wf.writelines( output.split() )
        if self.optionAsBool( token.options, "err", True) == False or self.optionAsBool( token.options, "stderr", True) == False:
            err = ""
        elif "err" in token.options or "stderr" in token.options:
            stderr_filename = token.options.get("err", token.options.get( "stderr", "stderr.dat" ))
            log.info( "Writing block %d stderr to file: %s" % ( self.blockid, stderr_filename ) )
            with open( stderr_filename, "w" ) as wf:
                wf.writelines( err.split() )
        
        if 'silent' in token.options or 'quiet' in token.options:
            output = ""
            err = ""

        # inject images
        imgout = ""
        for i in imgs:
            imgout += self.process_image_output( i )
        self.blockid = self.blockid + 1
        return output + err + imgout
    
    def render_thematic_break(self, token):
        # inspect( token )
        return "---"

    @staticmethod
    def render_line_break(token):
        log.debug( 'line break' )
        return '\n' if token.soft else '\n'

    def render_to_plain(self, token):
        if hasattr(token, 'children'):
            inner = [self.render_to_plain(child) for child in token.children]
            return ''.join(inner)
        return (token.content)

    def render_heading(self, token):
        inner = self.render_inner(token)
        out = "#" * int(token.level) + " " + inner
        return out

    def render_document(self, token):
        inner = '\n'.join([self.render(child) for child in token.children])
        return inner
