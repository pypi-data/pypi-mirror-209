from cleo.helpers import option
from cleo.commands.command import Command
# from deep_astro_uda.model.train import train
from deep_astro_uda.settings import DEFAULT_CONFIG_PATH
from deep_astro_uda.client.options import config_path
from deep_astro_uda.configs.config_functions import ConfigParser
from deep_astro_uda.data_utils.download_data import Downloader
import os

# TODO: Add docstrings.
class DemoCommand(Command):
    """
    Run demo pipeline for the client.
    """
    name = "demo"

    options = [
        config_path,
    ]
    
    #TODO: Write help command.
    help = ""

    def handle(self):        

        config_path = self.option('config-path')
        
        # parser = ConfigParser(file_path=output_path, filename="astroNN_10_train_config_open.yaml")

        output_path = os.path.join(os.getcwd(), "/deepastro_files")
        self.line(f"Running the DeepAstroUDA demo. All output will be saved here: {output_path}")

        # Download the Astro-nn data from the website. Save it in respective folders.
        download = Downloader(output_dir=os.path.join(output_path, "/data"))

        download.download_data(dataset_name="astro-nn")

        # Train the resnet model on the data using the default config file for astro-nn.
        train_parser = ConfigParser(config_path=config_path, filename="astroNN_10_train_config_open.yaml")

        # TODO: Implement function and add here.
        # Run inference using the test set.
            # Load saved model and attempt inference.
        self.line("Running training! Inference will proceed immediately after run. Training for DeepAstroUDA may take about an hour or two.")
        # train()









            
