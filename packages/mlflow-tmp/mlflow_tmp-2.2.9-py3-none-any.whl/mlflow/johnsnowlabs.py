import json
import sys
from pathlib import Path
import mlflow.spark

from johnsnowlabs import nlp
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
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
import logging
import os
from mlflow.utils.model_utils import (
    _add_code_from_conf_to_system_path,
    _get_flavor_configuration,
)

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


def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
    return [
        _get_pinned_requirement("johnsnowlabs"),
        "https://pypi.johnsnowlabs.com/4.4.2-f771e88dcf8e1535585c5531824a595e92c0305c/spark-nlp-jsl/spark_nlp_jsl-4.4.2-py3-none-any.whl",
        'pyspark==3.2.1',

    ]


FLAVOR_NAME = "johnsnowlabs"
MLMODEL_FILE_NAME = "MLmodel"
_MLFLOW_VERSION_KEY = "mlflow_version"


class MyModel(mlflow.pyfunc.PythonModel):
    def __init__(self, spell=None, pipe_path=None, jars_paths=None, license_path=None):
        os.environ['PYSPARK_PYTHON'] = sys.executable
        os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

        # TODO check if jsl-hoome exists, if not check if we find jar in Artifacts
        # TODO credentials?!
        if jars_paths:
            # load jar from disk
            os.environ.update({k: str(v) for k, v in json.load(open(license_path)).items() if v is not None})
            os.environ['JSL_NLP_LICENSE'] = json.load(open(license_path))['HC_LICENSE']
            self.spark = nlp.start(nlp=False, spark_nlp=False, jar_paths=jars_paths, json_license_path=license_path)
        else:
            # load jar from web
            if pipe_path:
                if os.path.exists(os.path.join(pipe_path,'jars.jsl')):
                    jars_paths, license_path = fetch_deps_from_path(pipe_path)
                    os.environ.update({k: str(v) for k, v in json.load(open(license_path)).items() if v is not None})
                    os.environ['JSL_NLP_LICENSE'] = json.load(open(license_path))['HC_LICENSE']

                    self.spark = nlp.start(nlp=False, spark_nlp=False, jar_paths=jars_paths, json_license_path=license_path)
            else:

                self.spark = nlp.start()
        if pipe_path:
            print(f'loading from disk {pipe_path}')
            self.pipe = nlp.to_nlu_pipe(PipelineModel.load(pipe_path))
            print('loading from disk done')
        else:
            self.pipe = nlp.load(spell)
        self.pipe.predict('Init NLU')

    def predict(self, model_input, output_level=None):
        return self.pipe.predict(model_input, output_level=output_level)


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
):  # TOdo make sure log shows up
    # todo make sure pass correct model type , its expected as kwarg in python_model
    print("LOG FROM log_mode")
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


def _load_pyfunc(path):
    # todo load jars ?
    print("LOAD FROM _load_pyfunc")
    return MyModel(pipe_path=path)


def fetch_deps_from_path(local_model_path):
    local_model_path = os.path.join(local_model_path,  'jars.jsl', )
    jar_paths = [os.path.join(local_model_path, file) for file in os.listdir(local_model_path) if '.jar' in file]
    license_path = [os.path.join(local_model_path, file) for file in os.listdir(local_model_path) if '.json' in file]
    license_path = license_path[0] if license_path else None
    return jar_paths, license_path

def load_model(model_uri):
    print("LOAD FROM load_model")
    local_model_path = _download_artifact_from_uri(artifact_uri=model_uri, output_path=None)
    jar_paths, license_path = fetch_deps_from_path(os.path.join(local_model_path,"model.jsl",))
    print("Found jars ", jar_paths)
    flavor_conf = _get_flavor_configuration(model_path=local_model_path, flavor_name=FLAVOR_NAME)
    _add_code_from_conf_to_system_path(local_model_path, flavor_conf)
    # Flavor configurations for models saved in MLflow version <= 0.8.0 may not contain a
    # `data` key; in this case, we assume the model artifact path to be `model.spacy`
    spacy_model_file_path = os.path.join(local_model_path, flavor_conf.get("data", "model.jsl"))
    return MyModel(pipe_path=spacy_model_file_path, jars_paths=jar_paths, license_path=license_path)


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
    deps_data_path = os.path.join(model_data_path, "jars.jsl")
    Path(model_data_path).mkdir(parents=True, exist_ok=True)

    if isinstance(python_model, MyModel):
        johnsnowlabs_model = python_model.pipe
    johnsnowlabs_model.vanilla_transformer_pipe.write().overwrite().save(model_data_path)
    Path(deps_data_path).mkdir(parents=True, exist_ok=True)

    from johnsnowlabs import nlp
    nlp.start()  # ?
    suite = get_install_suite_from_jsl_home(False)
    import shutil
    if suite.hc.get_java_path():
        shutil.copyfile(suite.hc.get_java_path(), os.path.join(deps_data_path, 'hc_jar.jar'))
    if suite.nlp.get_java_path():
        shutil.copyfile(suite.nlp.get_java_path(), os.path.join(deps_data_path, 'os_jar.jar'))

    secrets = JslSecrets.build_or_try_find_secrets()
    if secrets.HC_LICENSE:
        with open(os.path.join(deps_data_path, 'license.json'), 'w') as f:
            f.write(secrets.json())

    code_dir_subpath = _validate_and_copy_code_paths(code_paths, path)

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
