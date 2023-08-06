import sys

from johnsnowlabs import nlp
from pyspark.ml import PipelineModel

"""
The ``mlflow.spacy`` module provides an API for logging and loading spaCy models.
This module exports spacy models with the following flavors:

spaCy (native) format
    This is the main flavor that can be loaded back into spaCy.
:py:mod:`mlflow.pyfunc`
    Produced for use by generic pyfunc-based deployment tools and batch inference, this
    flavor is created only if spaCy's model pipeline has at least one
    `TextCategorizer <https://spacy.io/api/textcategorizer>`_.
"""
import os
from mlflow.utils.model_utils import (
    _get_flavor_configuration,
    _add_code_from_conf_to_system_path,
)

import logging
import os
import pickle

import mlflow
import numpy as np
import pandas as pd
import yaml
from mlflow import pyfunc
from mlflow.exceptions import MlflowException
from mlflow.models import Model
from mlflow.models.model import MLMODEL_FILE_NAME
from mlflow.models.utils import _save_example
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR, INVALID_PARAMETER_VALUE
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
from mlflow.utils.environment import (
    _CONDA_ENV_FILE_NAME,
    _CONSTRAINTS_FILE_NAME,
    _PYTHON_ENV_FILE_NAME,
    _REQUIREMENTS_FILE_NAME,
    _mlflow_conda_env,
    _process_conda_env,
    _process_pip_requirements,
    _PythonEnv,
    _validate_env_arguments,
)
from mlflow.utils.file_utils import write_to
from mlflow.utils.model_utils import (
    _add_code_from_conf_to_system_path,
    _get_flavor_configuration,
    _validate_and_copy_code_paths,
    _validate_and_prepare_target_save_path,
)
from mlflow.utils.requirements_utils import _get_pinned_requirement

_logger = logging.getLogger(__name__)

import yaml
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
import mlflow
from mlflow import pyfunc
from mlflow.models import Model, ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME
from mlflow.models.utils import ModelInputExample, _save_example
from mlflow.utils.environment import (
    _process_pip_requirements,
    _process_conda_env,
    _CONDA_ENV_FILE_NAME,
    _REQUIREMENTS_FILE_NAME,
    _CONSTRAINTS_FILE_NAME,
    _PYTHON_ENV_FILE_NAME,
    _PythonEnv,
)
from mlflow.utils.file_utils import write_to
from mlflow.utils.model_utils import (
    _validate_and_copy_code_paths,
)
from mlflow.utils.requirements_utils import _get_pinned_requirement


# TODO HARDCODE I NTERNAL!!?
def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
    return [
        _get_pinned_requirement("johnsnowlabs"),
        "https://pypi.johnsnowlabs.com/4.4.2-f771e88dcf8e1535585c5531824a595e92c0305c/spark-nlp-jsl/spark_nlp_jsl-4.4.2-py3-none-any.whl",

            ]


FLAVOR_NAME = "johnsnowlabs"
MLMODEL_FILE_NAME = "MLmodel"
_MLFLOW_VERSION_KEY = "mlflow_version"



class MyModel(mlflow.pyfunc.PythonModel):
    def __init__(self, spell=None, pipe_path=None):
        os.environ['PYSPARK_PYTHON'] = sys.executable
        os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

        self.spark = nlp.start()
        if pipe_path:
            print(f'loading from disk {pipe_path}')
            self.pipe = nlp.to_nlu_pipe(PipelineModel.load(pipe_path))
            print('loading from disk done')


        else:
            self.pipe = nlp.load(spell)
        self.pipe.predict('Init NLU')

    def predict(self, model_input, groupy=None):
        # return 1
        return self.pipe.predict(model_input) #,groupy=groupy)







def log_model(
        johnsnowlabs_model,
        artifact_path,
        conda_env=None,
        code_paths=None,
        registered_model_name=None,
        signature: ModelSignature = None,
        input_example: ModelInputExample = None,
        pip_requirements=None,
        extra_pip_requirements=None,
        metadata=None,
        **kwargs,
):
    # todo make sure pass correct model type , its expected as kwarg in python_model
    return Model.log(
        artifact_path=artifact_path,
        flavor=mlflow.johnsnowlabs,
        registered_model_name=registered_model_name,
        python_model=johnsnowlabs_model,
        johnsnowlabs_model=johnsnowlabs_model,
        conda_env=conda_env,
        code_paths=code_paths,
        signature=signature,
        input_example=input_example,
        pip_requirements=pip_requirements,
        extra_pip_requirements=extra_pip_requirements,
        metadata=metadata,
        **kwargs,
    )




def _load_pyfunc(path): return MyModel(pipe_path=path)


def load_model(model_uri):
    local_model_path = _download_artifact_from_uri(artifact_uri=model_uri, output_path=None)
    flavor_conf = _get_flavor_configuration(model_path=local_model_path, flavor_name=FLAVOR_NAME)
    _add_code_from_conf_to_system_path(local_model_path, flavor_conf)
    # Flavor configurations for models saved in MLflow version <= 0.8.0 may not contain a
    # `data` key; in this case, we assume the model artifact path to be `model.spacy`
    spacy_model_file_path = os.path.join(local_model_path, flavor_conf.get("data", "model.jsl"))
    return MyModel(pipe_path=spacy_model_file_path)


def _save_model(sk_model, output_path, serialization_format):
    print('????SAVING!!')


def save_model(
        johnsnowlabs_model=None,
        path=None,
        conda_env=None,
        code_paths=None,
        mlflow_model=None,
        signature: ModelSignature = None,
        input_example: ModelInputExample = None,
        pip_requirements=None,
        extra_pip_requirements=None,
        metadata=None,
        loader_module=None,  # RM
        data_path=None,  # RM
        code_path=None,  # RM
        python_model=None,  # RM
        artifacts=None,  # RM
):
    print('Saving')

    model_data_subpath = "model.jsl"
    model_data_path = os.path.join(path, model_data_subpath)
    os.makedirs(model_data_path)
    code_dir_subpath = _validate_and_copy_code_paths(code_paths, path)
    if isinstance(python_model,MyModel ):
        johnsnowlabs_model = python_model.pipe
    johnsnowlabs_model.vanilla_transformer_pipe.write().overwrite().save(model_data_path)

    if mlflow_model is None:
        mlflow_model = Model()
    if signature is not None:
        mlflow_model.signature = signature
    if input_example is not None:
        _save_example(mlflow_model, input_example, path)
    if metadata is not None:
        mlflow_model.metadata = metadata

    mlflow_model.add_flavor(
        FLAVOR_NAME, jsl_version='69696969', data=model_data_subpath, code=code_dir_subpath
    )

    pyfunc.add_to_model(
        mlflow_model,
        loader_module="mlflow.johnsnowlabs",
        data=model_data_subpath,
        conda_env=_CONDA_ENV_FILE_NAME,
        python_env=_PYTHON_ENV_FILE_NAME,
        code=code_dir_subpath,
    )

    if conda_env is None:
        if pip_requirements is None:
            default_reqs = get_default_pip_requirements()
            # To ensure `_load_pyfunc` can successfully load the model during the dependency
            # inference, `mlflow_model.save` must be called beforehand to save an MLmodel file.
            inferred_reqs = mlflow.models.infer_pip_requirements(
                model_data_path,
                FLAVOR_NAME,
                fallback=default_reqs,
            )
            default_reqs = sorted(set(inferred_reqs).union(default_reqs))
        else:
            default_reqs = None
        conda_env, pip_requirements, pip_constraints = _process_pip_requirements(
            default_reqs,
            pip_requirements,
            extra_pip_requirements,
        )
    else:
        conda_env, pip_requirements, pip_constraints = _process_conda_env(conda_env)

    with open(os.path.join(path, _CONDA_ENV_FILE_NAME), "w") as f:
        yaml.safe_dump(conda_env, stream=f, default_flow_style=False)

    # Save `constraints.txt` if necessary
    if pip_constraints:
        write_to(os.path.join(path, _CONSTRAINTS_FILE_NAME), "\n".join(pip_constraints))

    # Save `requirements.txt`
    write_to(os.path.join(path, _REQUIREMENTS_FILE_NAME), "\n".join(pip_requirements))

    _PythonEnv.current().to_yaml(os.path.join(path, _PYTHON_ENV_FILE_NAME))
    mlflow_model.save(os.path.join(path, MLMODEL_FILE_NAME))



url="https://pypi.johnsnowlabs.com/4.4.2-f771e88dcf8e1535585c5531824a595e92c0305c/spark-nlp-jsl/spark_nlp_jsl-4.4.2-py3-none-any.whl",
