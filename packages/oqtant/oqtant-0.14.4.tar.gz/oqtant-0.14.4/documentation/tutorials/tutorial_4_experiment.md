# Oqtant Tutorial 3: BEC Experimentation

### This walkthrough covers best practices for conducting experiments on the Oqtant system, including submitting batches of jobs, tracking experiment progress, and handling output data for later analysis.

For more information about Oqtant refer to our documentation: https://albert-dev.coldquanta.com/oqtant/manual.md

# Sign into Oqtant

## Before you can view and submit jobs you must first sign into your Oqtant account

Run the below cell to be re-directed to our login page and provide you account credentials. Once authenticated you can safely close out that tab and return to this notebook.

```python
from matplotlib import pyplot as plt
from lmfit import Model
import numpy as np
import inspect
import copy
from oqtant.oqtant_client import get_oqtant_client
from oqtant.util.auth import get_user_token
from bert_schemas import job as JobSchema
from oqtant.schemas.job import (
    OqtantJob,
    Gaussian_dist_2D,
    TF_dist_2D,
    bimodal_dist_2D,
    round_sig
)
import csv

token = get_user_token()
```

## Creating a Oqtant Client Instance

### After successful login, create an authorized session with the Oqtant Client

- the oqtant_client interacts with the albert server to perform remote lab functions.
- the oqtant_client object also contains all the jobs which have been submitted, run, or loaded (from database or file) during this python session

```python
oqtant_client = get_oqtant_client(token)
```

## Design a simple experiment

For this example, we will investigate the effect of altering the final frequency of the RF knife on the evolution of the condensate and its temperature.

### Variables

1. **rf_e_mhz** - the final frequency of the rf knife (at t=1600ms)
2. **\*time_of_flight_ms** - the TOF interval in ms. varying the time will give us snapshots of the condensate as it expands

### Observables

- TOF images
- temperature (calculated from TOF images)
- condensate fraction (calculated from TOF images)

```python
rf_e_values = [0.07, 0.03, 0.05]
tof_interval_values = [10, 12, 15]
```

## Generate job parameters for the experiment with generate_albert_job

This experiment consists of 3 job inputs and no repeated trials. Below is an example BEC job with default parameters, here we update the **rf_e_mhz** and **time_of_flight_ms** values for each input. Review the input parameters before submitting the experiment jobs to run on the Oqtant hardware. Once a job is submitted, it can only be cancelled by contacting **albert@infleqtion.com**

```python
experiment = {
    "name": "RF Sweep Experiment",
    "job_type": "BEC",
    "inputs": [
        {
            "notes": "RF Sweep #1",
            "values": {
                "time_of_flight_ms": tof_interval_values[0],
                "image_type": "TIME_OF_FLIGHT",
                "end_time_ms": 0.0,
                "rf_evaporation": {
                    "frequencies_mhz": [17.0, 8.0, 4.0, 1.2, rf_e_values[0]],
                    "powers_mw": [500.0, 500.0, 475.0, 360.0, 220.0],
                    "interpolation": "LINEAR",
                    "times_ms": [-1600, -1200, -800, -400, 0],
                },
                "optical_barriers": None,
                "optical_landscape": None,
                "lasers": None,
            }
        },
        {
            "notes": "RF Sweep #2",
            "values": {
                "time_of_flight_ms": tof_interval_values[1],
                "image_type": "TIME_OF_FLIGHT",
                "end_time_ms": 0.0,
                "rf_evaporation": {
                    "frequencies_mhz": [17.0, 8.0, 4.0, 1.2, rf_e_values[1]],
                    "powers_mw": [500.0, 500.0, 475.0, 360.0, 220.0],
                    "interpolation": "LINEAR",
                    "times_ms": [-1600, -1200, -800, -400, 0],
                },
                "optical_barriers": None,
                "optical_landscape": None,
                "lasers": None,
            }
        },
        {
            "notes": "RF Sweep #3",
            "values": {
                "time_of_flight_ms": tof_interval_values[2],
                "image_type": "TIME_OF_FLIGHT",
                "end_time_ms": 0.0,
                "rf_evaporation": {
                    "frequencies_mhz": [17.0, 8.0, 4.0, 1.2, rf_e_values[2]],
                    "powers_mw": [500.0, 500.0, 475.0, 360.0, 220.0],
                    "interpolation": "LINEAR",
                    "times_ms": [-1600, -1200, -800, -400, 0],
                },
                "optical_barriers": None,
                "optical_landscape": None,
                "lasers": None,
            }
        },
    ],
}

experiment_job = oqtant_client.generate_albert_job(job=experiment)
print(experiment_job)
```

## Accessing fields of OqtantJob, BecInput and BarrierInput objects

To access the above input parameters of a job object:

**EXAMPLEJOB.inputs[desired-input-index].values.FIELD_FROM_BELOW_LIST**

Here, we review the experiment parameters by accessing the "input" object which has the following fields:

BarrierInput

- Type: "BARRIER"
- barrier_1_ht: list of barrier height (nK). min = 0, max = 5000. len = 11. **(default = [500, 1000, 1500, 2000, 2500, 2500, 2500, 2500, 2500, 2500, 2500])**
- barrier_1_pos: list of barrier position (um). min = -100, max = 100. len = 11. **([-20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20])**
- barrier_2_ht: list of barrier height (nK). min = 0, max = 5000. len = 11 **(default = [500, 1000, 1500, 2000, 2500, 2500, 2500, 2500, 2500, 2500, 2500])**
- barrier_2_pos: list of barrier position (um). min = -100, max = 100. len = 11. **(default = [-20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20])**
- barrier_duration: time (ms). min = 10, max = 100. **(default=50)**
- barrier_image: 0 (in-trap), 1 (tof). **default=0 (in-trap)**

BecInput

- Type: "BEC"
- time_of_flight_ms: time (ms). min = 1, max = 50. **(default = 20)**
- rf_a_mhz: rf knife freq (MHz) at t = 0ms. min = 0, max = 50. **(default = 17)**
- rf_b_mhz: rf knife freq (MHz) at t = 400ms. min = 0, max = 50. **(default = 8)**
- rf_c_mhz: rf knife freq (MHz) at t = 800ms. min = 0, max = 50. **(default = 4)**
- rf_d_mhz: rf knife freq (MHz) at t = 1200ms. min = 0, max = 50. **(default = 1.2)**
- rf_e_mhz: rf knife freq (MHz) at t = 1600ms. min = 0, max = 50. **(default = 0.07)**
- power_a_mw: rf knife power (mW) at t:[0,400) ms. min = 0, max = 1000. **(default = 500)**
- power_b_mw: rf knife power (mW) at t:[400,800) ms. min = 0, max = 1000. **(default = 475)**
- power_c_mw: rf knife power (mW) at t:[800,1200) ms. min = 0, max = 1000. **(default = 450)**
- power_d_mw: rf knife power (mW) at t:[1200,1600] ms. min = 0, max = 1000. **(default = 400)**
- time_of_flight_ms: time (ms). min = 1, max = 50. **(default = 20)**

```python
for i, experiment_input in enumerate(experiment_job.inputs):
    print(
        experiment_job.name,
        f"input run #{i + 1}",
        experiment_input.values.rf_evaporation.frequencies_mhz[4],
        experiment_input.values.time_of_flight_ms
    )
```

## Submit jobs and store the job IDs

Option to run the jobs and wait for results (**track_status=True**) OR submit the jobs and return later to retrieve the results (**track_status=False**). Either way, be sure to save the job ids to a file if you plan to retrieve the data for later processing.

```python
rf_sweep_experiment = oqtant_client.run_jobs(job_list=[experiment_job], track_status=False)

with open('bec_rf_sweep_experiment.txt', 'w') as filewriter:
    for listitem in rf_sweep_experiment:
        filewriter.write('%s\n' % listitem)
```

## Load results from completed jobs

Use **load_jobs_from_id** to retrieve jobs in any state from a previous run.

```python
with open('bec_rf_sweep_experiment.txt', 'r') as filereader:
    for line in filereader:
        # remove linebreak which is the last character of the string
        oqtant_client.load_job_from_id(line[:-1])

for job_id, job in oqtant_client.active_jobs.items():
    print("id: ", job_id, job.job_type, job.status)
```

## Plot completed jobs

When job status is COMPLETE above, plot the results

```python
for a, job in oqtant_client.active_jobs.items():
    if job.status == JobSchema.JobStatus.COMPLETE and job.job_type == JobSchema.JobType.BEC:
        job.atoms_2dplot()
        job.atoms_sliceplot()

# by default jobs that are loaded will only contain the first input/output entry
# if you have more than one input for a job you can view its details by specifying the 'run' like below
desired_input_run = 2 # here we are asking for the second input/output entry
with open('bec_rf_sweep_experiment.txt', 'r') as filereader:
    for line in filereader:
        # remove linebreak which is the last character of the string
        oqtant_client.load_job_from_id(line[:-1], run=desired_input_run)

# now we can display the second input/output entry results
for a, job in oqtant_client.active_jobs.items():
    if job.status == JobSchema.JobStatus.COMPLETE and job.job_type == JobSchema.JobType.BEC:
        job.atoms_2dplot()
        job.atoms_sliceplot()
```
