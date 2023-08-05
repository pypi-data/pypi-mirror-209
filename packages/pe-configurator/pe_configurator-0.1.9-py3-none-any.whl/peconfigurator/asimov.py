import importlib
import os
import configparser
import json
import shutil

import h5py
from asimov.pipeline import Pipeline
from asimov import config
import htcondor
import yaml
from asimov.utils import set_directory

class AsimovPipeline(Pipeline):
    """
    An asimov pipeline for PE Configurator.
    """
    name = "peconfigurator"
    config_template = os.path.join(os.path.dirname(__file__), "asimov_template.yaml")
    #importlib.resources.path(__package__, "asimov_template.yaml")
    _pipeline_command = "peconfigurator"


    def _find_posterior(self):
        """
        Find the input posterior samples.
        """
        if self.production.dependencies:
            productions = {}
            for production in self.production.event.productions:
                productions[production.name] = production
            for previous_job in self.production.dependencies:
                print("assets", productions[previous_job].pipeline.collect_assets())
                try:
                    if "samples" in productions[previous_job].pipeline.collect_assets():
                        posterior_file = productions[previous_job].pipeline.collect_assets()['samples']
                        if "dataset" not in self.production.meta:
                            with h5py.File(posterior_file,'r') as f:
                                keys = list(f.keys())
                            keys.remove('version')
                            keys.remove('history')
                            self.production.meta['dataset'] = keys[0]
                        return posterior_file
                except Exception:
                    pass
        else:
            self.logger.error("Could not find an analysis providing posterior samples to analyse.")
    
    def build_dag(self, dryrun=False):
        """
        Create a condor submission description.
        """
        name = self.production.name
        ini = self.production.event.repository.find_prods(name,
                                                          self.category)[0]

        meta = self.production.meta
        posterior = self._find_posterior()

        executable = f"{os.path.join(config.get('pipelines', 'environment'), 'bin', self._pipeline_command)}"
        command = ["--dataset", f"{meta['dataset']}",
                   "--output_dir", "results",
                   "--json_file", "recommendations.json",
                   "--report_file", "report.html",
	           "--q-min", f"{meta['minimum mass ratio']}",
                   ]
        if "higher modes" in meta['checks']:
            command += ["--HM"]
        if "luminosity distance" in meta['checks']:
            command += ["--include_dL_recommendations"]
        if "no safety" in meta['checks']:
            command += ["--override_safeties"]
        command += [posterior]

        full_command = executable + " " + " ".join(command)
        self.logger.info(full_command)
        
        description = {
            "executable": executable,
            "arguments": " ".join(command),
            "output": f"{name}.out",
            "error": f"{name}.err",
            "log": f"{name}.log",
            "getenv": "True",
            "request_memory": "4096 MB",
            "batch_name": f"{self.name}/{self.production.event.name}/{name}",
            "accounting_group_user": config.get('condor', 'user'),
            "accounting_group": self.production.meta['scheduler']["accounting group"],
            "request_disk": "8192MB",
            "+flock_local": "True",
            "+DESIRED_Sites": htcondor.classad.quote("nogrid"),
        }

        job = htcondor.Submit(description)
        os.makedirs(self.production.rundir, exist_ok=True)
        with set_directory(self.production.rundir):
            os.makedirs("results", exist_ok=True)
            
            with open(f"{name}.sub", "w") as subfile:
                subfile.write(job.__str__())

            with open(f"{name}.sh", "w") as bashfile:
                bashfile.write(str(full_command))
                
        with set_directory(self.production.rundir):
            try:
                schedulers = htcondor.Collector().locate(htcondor.DaemonTypes.Schedd, config.get("condor", "scheduler"))
            except configparser.NoOptionError:
                schedulers = htcondor.Collector().locate(htcondor.DaemonTypes.Schedd)
            schedd = htcondor.Schedd(schedulers)
            with schedd.transaction() as txn:
                cluster_id = job.queue(txn)

        self.clusterid = cluster_id

    def submit_dag(self, dryrun=False):
        self.production.status = "running"
        self.production.job_id = int(self.clusterid)
        return self.clusterid

    def collect_assets(self):
        output = {}
        if os.path.exists(os.path.join(self.production.rundir, "results")):
            output['recommendations'] = os.path.join(self.production.rundir, "results", "recommendations.json")
            output['report'] = os.path.join(self.production.rundir, "results", "report.html")
        return output
    
    def detect_completion(self):
        self.logger.info("Checking for job completion.")
        results = self.collect_assets()
        if len(list(results.keys())) > 0:
            self.logger.info("Outputs detected, job complete.")
            return True
        else:
            self.logger.info("PE Configurator job completion was not detected.")
            return False

    def after_completion(self):
        """
        Add the recommendations to the ledger.
        """
        with open(self.collect_assets()['recommendations'], "r") as datafile:
            data = json.load(datafile)

        # Copy the report file to the pages directory.
        pages_dir = os.path.join(config.get("general", "webroot"), self.production.event.name, self.production.name)
        
        shutil.copy(self.collect_assets()['report'], os.path.join(pages_dir, "index.html"))
        
        meta = self.production.event.meta

        if "waveform" not in meta:
            meta['waveform'] = {}
        if "likelihood" not in meta:
            meta['likelihood'] = {}
        
        if 'srate' in data:
            meta['likelihood']['sample rate'] = data['srate']

        if 'f_start' in data:
            meta['likelihood']['start frequency'] = data['f_start']
            
        if 'f_ref' in data:
            meta['waveform']['reference frequency'] = data['f_ref']

        if 'seglen' in data and 'segment length' not in meta['data']:
            meta['data']['segment length'] = data['seglen']
        if 'window length' not in meta['likelihood']:
            meta['likelihood']['window length'] = meta['data']['segment length']
        if 'psd length' not in meta['likelihood']:
            meta['likelihood']['psd length'] = meta['data']['segment length']

        if "chirpmass_min" in data:
            if not "chirp mass" in meta['priors']:
                meta['priors']['chirp mass'] = {}
            meta['priors']['chirp mass']['minimum'] = data['chirpmass_min']
            meta['priors']['chirp mass']['maximum'] = data['chirpmass_max']

        if "q_min" in data:
            if not "mass ratio" in meta['priors']:
                meta['priors']['mass ratio'] = {}
                meta['priors']['mass ratio']['minimum'] = data["q_min"]
            else:
                if meta['priors']['mass ratio']['minimum'] > data["q_min"]:
                    meta['priors']['mass ratio']['minimum'] = data["q_min"]
        
        if "dL_max" in data:
            if not "luminosity distance" in meta['priors']:
                meta['priors']['luminosity distance'] = {}
                meta['priors']['luminosity distance']['maximum'] = data["dL_max"]
            else:
                if meta['priors']['luminosity distance']['maximum'] < data["dL_max"]:
                    meta['priors']['luminosity distance']['maximum'] = data["dL_max"]
                
        self.production.event.update_data()
        self.production.status = "uploaded"

    def html(self):
        """Return the HTML representation of this pipeline."""
        out = ""
        pages_dir = os.path.join(self.production.event.name, self.production.name)
        os.makedirs(pages_dir, exist_ok=True)
        if self.production.status in {"finished", "uploaded"}:
            out += """<div class="asimov-pipeline">"""
            out += f"""<a href="{pages_dir}/index.html">Report</a>"""
            out += """</div>"""

        return out
